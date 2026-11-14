# Mercadinho API

Backend de um projeto de extensão universitária desenvolvido por estudantes do curso de Análise e Desenvolvimento de Sistemas.

A aplicação tem como objetivo fornecer uma API REST para gerenciamento de operações de um mercadinho, utilizando tecnologias modernas de desenvolvimento backend.

## Tecnologias utilizadas

- **Python:** linguagem principal.
- **FastAPI:** construção da API REST.
- **PostgreSQL:** banco de dados relacional.
- **SQLAlchemy:** ORM para comunicação com o banco de dados.
- **Psycopg:** driver de conexão com PostgreSQL.
- **Docker:** containerização da aplicação.
- **Docker Compose:** gerenciamento dos serviços.
- **Git:** controle de versão e colaboração.

##  Estrutura do projeto

```text
mercadinho-api/
│
├── database/
│   ├── __init__.py
│   ├── database.py
│   └── models.py
│
├── main.py
│
├── Dockerfile
├── compose.yaml
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

##  Pré-requisitos

Antes de executar o projeto, é necessário ter instalado:

- [Git](https://git-scm.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

Não é necessário instalar Python ou PostgreSQL diretamente na máquina para executar a versão containerizada.

##  Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/Sandro-Raphael/mercadinho-api
```

### 2. Entrar no diretório

```bash
cd le-mercado
```

### 3. Configurar as variáveis de ambiente

Crie um arquivo `.env` a partir do `.env.example`.

No Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Confira as variáveis disponíveis e configure os valores necessários.

**Importante:** não compartilhe o arquivo `.env` nem envie credenciais reais ao GitHub.

### 4. Construir e iniciar os containers

```bash
docker compose up --build
```

Esse comando constrói a imagem da aplicação, inicia os serviços definidos no Docker Compose e disponibiliza a API.

Para executar em segundo plano:

```bash
docker compose up --build -d
```

## Acessando a API

Após iniciar os serviços, a documentação interativa do FastAPI estará disponível em:

**Swagger UI:**

http://localhost:8000/docs

**ReDoc:**

http://localhost:8000/redoc

A documentação permite visualizar os endpoints, consultar parâmetros e testar as operações disponíveis.

## Comandos Docker úteis

| Comando | Finalidade |
|---|---|
| `docker compose up` | Inicia os serviços |
| `docker compose up --build` | Reconstrói e inicia os serviços |
| `docker compose up -d` | Inicia em segundo plano |
| `docker compose down` | Encerra e remove os containers |
| `docker compose ps` | Lista os serviços e seus estados |
| `docker compose logs` | Exibe os logs dos serviços |
| `docker compose logs -f api` | Acompanha os logs da API |
| `docker compose restart` | Reinicia os serviços |

**Atenção:** o comando abaixo remove também os volumes associados e pode apagar os dados persistidos do PostgreSQL:

```bash
docker compose down -v
```

Utilize somente quando realmente desejar reinicializar o banco de dados.

## Fluxo de colaboração

O desenvolvimento utiliza Git e GitHub para controle de versão e colaboração entre os integrantes.

Recomenda-se trabalhar com branches individuais ou por funcionalidade, evitando alterações diretas na branch principal.

### Criando uma branch

```bash
git switch -c feature/nome-da-funcionalidade
```

### Registrando alterações

```bash
git add .
git commit -m "feat: descrição da funcionalidade"
```

### Enviando alterações ao GitHub

```bash
git push -u origin feature/nome-da-funcionalidade
```

Após o envio, abra um Pull Request para revisão e integração das alterações na branch principal.

## Convenção de commits

Para manter o histórico organizado, recomenda-se utilizar mensagens padronizadas:

| Prefixo | Utilização |
|---|---|
| `feat` | Nova funcionalidade |
| `fix` | Correção de erro |
| `docs` | Alterações na documentação |
| `refactor` | Reestruturação do código |
| `test` | Criação ou alteração de testes |
| `chore` | Manutenção e configurações |

Exemplos:

```bash
git commit -m "feat: adiciona cadastro de produtos"
git commit -m "fix: corrige conexão com PostgreSQL"
git commit -m "docs: atualiza instruções de instalação"
```

## Licença

Projeto acadêmico desenvolvido para fins educacionais e de extensão universitária.

A definição de uma licença de distribuição deverá ser realizada pela equipe responsável.

---

**Mercadinho API**  
Projeto de extensão universitária | Análise e Desenvolvimento de Sistemas
