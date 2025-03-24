# Api Livros Doados VnW

Essa é uma API simples feita com flask e
SQLite para fins de estudo na escola Vai na Web,
ela permite cadastrar e listar os livros doados.

## Como rodar o projeto?

1. Faça o clone do repositório:
```bash
git clone <LINK_DO_REPOSITÓRIO>
cd nome_do_projeto
```
2. Criar um ambiente virtual (Obrigatório)
```bash
python -m venv venv
source venv/Scripts/activate
```
```bash
**Linus/Mac**
python3 -m venv venv
source venv/bin/activate
```


3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Inicie o servidor:
```bash
python app.py
```

> A API estará disponivel em http://127.0.0.1:5000/

## Endpoints

### POST /doar

Endpoints para cadastro das informações do livro doado.

**Envio (JSON)**
```json
{
    "titulo":"Ainda estou devendo aqui",
    "categoria":"Drama/Finanças",
    "autor":"Fernando Polia",
    "imagem_url":"https://exemplo.com"
}

```