# 📊 Sistema de Gestão Inteligente

Este projeto é um sistema web construído com **FastAPI + Beanie (MongoDB)** para gerenciar:

- Funcionários
- Cargos
- Departamentos
- Cursos
- Conhecimentos
- Avaliações
- Certificados
- Referências Bibliográficas

---

## 🚀 Tecnologias

- Python 3.9+
- FastAPI
- Uvicorn
- Beanie (ODM para MongoDB)
- MongoDB local ou MongoDB Atlas
- Pydantic

---

## 🛠️ Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/gestaointeligente.git
cd gestaointeligente
```

### 2. Crie e ative um ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

> Se o arquivo não existir, use:
```bash
pip install fastapi uvicorn beanie motor pydantic
```

---

## 🗃️ Configuração do MongoDB

### Local (recomendado para testes)

Garanta que você tenha o MongoDB instalado e rodando com autenticação:

1. Inicie o serviço:

```bash
brew services start mongodb-community@6.0
```

2. Crie o usuário no banco:

```js
use gestao_db
db.createUser({
  user: "admin",
  pwd: "gestaointeligente",
  roles: [{ role: "readWrite", db: "gestao_db" }]
})
```

---

## ⚙️ Rodando o projeto

Com o Mongo rodando, execute:

```bash
uvicorn app.main:app --reload
```

A API estará disponível em:

🔗 `http://127.0.0.1:8000`

---

## 📘 Documentação automática

- **Swagger (UI interativa):**  
  `http://127.0.0.1:8000/docs`

- **ReDoc (visual alternativa):**  
  `http://127.0.0.1:8000/redoc`

---

## ✅ Rotas principais disponíveis

| Entidade                   | Método            | Rota                            |
|----------------------------|-------------------|---------------------------------|
| Funcionários               | GET/POST/DELETE   | `/funcionarios`                |
| Cargos                     | GET/POST/DELETE   | `/cargos`                      |
| Departamentos              | GET/POST/DELETE   | `/departamentos`               |
| Funcionário-Cargo          | POST              | `/funcionarios-cargos`         |
| Cursos                     | GET/POST/DELETE   | `/cursos`                      |
| Certificados               | GET/POST/DELETE   | `/certificados`                |
| Conhecimentos              | GET/POST/DELETE   | `/conhecimentos`               |
| Funcionario-Conhecimento   | POST              | `/funcionarios-conhecimentos`  |
| Avaliações                 | GET/POST/DELETE   | `/avaliacoes`                  |
| Referências Bibliográficas | GET/POST/DELETE   | `/referencias`                 |

---

## 👨‍💻 Contribuindo

1. Crie uma branch:
```bash
git checkout -b feature/nome-da-feature
```

2. Após implementar:
```bash
git add .
git commit -m "feat: descreva o que fez"
git push origin feature/nome-da-feature
```

3. Abra um Pull Request no GitHub.

---

## 🧪 Testes (a implementar)

- Por enquanto os testes estão manuais via Swagger.
- Futuros testes automatizados podem ser feitos com `pytest` e `httpx`.

---

## 🧠 Observações

- Projeto segue o padrão MVC (models, schemas, routes)
- Beanie é utilizado como ODM (Object Document Mapper)
- O MongoDB deve estar autenticado via `mongodb://admin:gestaointeligente@localhost:27017/?authSource=gestao_db`

---

## ✨ Autor

Desenvolvido por [@david-wolff](https://github.com/david-wolff) 
