from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy.orm import Session
from database.database import engine, Base, get_db
from database.models import Item

app = FastAPI(title="Mercadinho API")

# Criação inicial das tabelas
Base.metadata.create_all(bind=engine)


# Schemas
class ItemCreate(BaseModel):
    item_name: str = Field(min_length=1, max_length=150)
    quantity: int = Field(ge=0)


class ItemUpdate(BaseModel):
    item_name: str = Field(min_length=1, max_length=150)
    quantity: int = Field(ge=0)


class ItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    item_id: int
    item_name: str
    quantity: int

@app.get("/")
def root():
    return {"message": "API funcionando! Acesse /docs para a documentação."}

# GET: Listar todos os produtos
@app.get("/all_items", response_model=list[ItemResponse])
def read_all(db: Session = Depends(get_db)):
    return db.query(Item).all()


# GET: Consultar produto específico
@app.get("/items/{item_id}", response_model=ItemResponse)
def read_item(
    item_id: int,
    db: Session = Depends(get_db)
):
    item = db.query(Item).filter(
        Item.item_id == item_id
    ).first()

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    return item


# POST: Criar produto
@app.post("/create_item", response_model=ItemResponse, status_code=201)
def create_item(
    data: ItemCreate,
    db: Session = Depends(get_db)
):
    item = Item(
        item_name=data.item_name,
        quantity=data.quantity
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return item


# PUT: Atualizar produto
@app.put("/update_item/{item_id}", response_model=ItemResponse)
def update_item(
    item_id: int,
    data: ItemUpdate,
    db: Session = Depends(get_db)
):
    item = db.query(Item).filter(
        Item.item_id == item_id
    ).first()

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    item.item_name = data.item_name
    item.quantity = data.quantity

    db.commit()
    db.refresh(item)

    return item


# DELETE: Excluir produto
@app.delete("/delete_item/{item_id}")
def delete_item(
    item_id: int,
    db: Session = Depends(get_db)
):
    item = db.query(Item).filter(
        Item.item_id == item_id
    ).first()

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    db.delete(item)
    db.commit()

    return {
        "message": "Produto excluído com sucesso",
        "item_id": item_id
    }
