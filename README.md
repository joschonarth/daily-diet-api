# 🍽️ Daily Diet API

A Daily Diet API é uma solução completa para o controle de hábitos alimentares e de hidratação, permitindo que os usuários monitorem sua ingestão diária de alimentos e água. Com recursos para gerenciar informações nutricionais e estabelecer metas personalizadas, ela facilita o acompanhamento do progresso em direção a uma alimentação equilibrada e saudável. Desenvolvida em Python com Flask e SQLAlchemy, a API oferece uma maneira prática e eficiente de manter o controle sobre a dieta e o bem-estar.

## ⚙️ Funcionalidades

### 🥗 Refeições

- 🍴 **Adicionar Refeição**: Criação de novas refeições com nome, descrição, categoria, calorias e status de dieta.
- ✏️ **Atualizar Refeição**: Modificação dos dados de uma refeição existente.
- ❌ **Excluir Refeição**: Exclusão de uma refeição.
- 🔍 **Consultar Refeições**: Listagem de refeições com filtros por categoria, status de dieta, e período.
- ❤️ **Favoritar Refeição**: Marcação de refeições como favoritas.
- 📅 **Filtragem de Refeições**: Filtros por data (dia, semana, mês) ou intervalo de datas personalizadas.
- 📊 **Relatório de Refeições**: Geração de relatórios sobre as refeições registradas, com a possibilidade de filtrar por períodos (dia, semana, mês) e incluir informações como calorias totais e metas de consumo de calorias.
- 🎯 **Atualizar Meta de Calorias**: Atualização da meta diária de calorias com base no objetivo nutricional do usuário.
- 🔥 **Streak de Calorias**: Acompanhamento do número de dias consecutivos em que a meta de calorias foi atingida.

### 💧 Ingestão de Água

- 💦 **Adicionar Ingestão de Água**: Registrar quantidade de água ingerida.
- ❌ **Remover Ingestão de Água**: Excluir um registro específico de ingestão de água.
- 📅 **Consultar Ingestão de Água**: Consultar ingestões de água com filtros de dia, semana e mês.
- 📈 **Total de Água Consumida**: Obter o total de água consumida em um período, com progresso em relação à meta.
- 🎯 **Atualizar Meta de Ingestão de Água**: Ajustar a meta diária de ingestão de água.
- 🔥 **Streak de Ingestão de Água**: Acompanhamento do número de dias consecutivos em que a meta de ingestão de água foi alcançada.

## 🛠️ Tecnologias Utilizadas

- 🐍 **Python** - Linguagem de programação utilizada.
- 🔥 **Flask** - Framework web em Python.
- 💾 **SQLAlchemy** - ORM para banco de dados.
- 📂 **SQLite** - Banco de dados leve, utilizado para armazenar os dados da aplicação.

## 📚 Bibliotecas Utilizadas

- 🔗 [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/latest/) - Integração do SQLAlchemy com Flask.
- 🔑 [Flask-Login](https://flask-login.readthedocs.io/en/latest/) - Gerenciamento de sessão de login.
- ⚙️ [Werkzeug](https://werkzeug.palletsprojects.com/en/latest/) - Utilitário WSGI para Flask.
- 🛡️ [cryptography](https://cryptography.io/en/latest/) - Biblioteca de criptografia para Python.
- 🔒 [bcrypt](https://pypi.org/project/bcrypt/) - Para hashing seguro de senhas.

## 🚀 Como Rodar o Projeto

📌 1. Clone o repositório:

```bash
git clone https://github.com/joschonarth/flask-auth-project
```

📌 2. Entre na pasta do projeto:

```bash
cd flask-auth-project
```

📌 3. Crie um ambiente virtual:

```bash
python -m venv .venv
```

📌 4. Ative o ambiente ambiente virtual:

```bash
.venv\Scripts\activate
```

📌 5. Instale as dependências do projeto que estão no arquivo [`requirements.txt`](requirements.txt):

```bash
pip install -r requirements.txt
```

📌 6. Inicie o servidor de desenvolvimento:

```bash
python app.py
```

## 🌐 Acesso à API
A API estará disponível em: [http://127.0.0.1:5000](http://127.0.0.1:5000)

<!-- ## 📡 Estrutura de Endpoints

- **/meals**

    - ➕ **POST** `/api/meals/add` - Adicionar uma refeição.  
    - ✏️ **PUT** `/api/meals/update/{meal_id}` - Atualizar uma refeição.  
    - ❌ **DELETE** `/api/meals/delete/{meal_id}` - Excluir uma refeição.  
    - 🔍 **GET** `/api/meals` - Consultar lista de refeições com filtros.  
    - 📋 **GET** `/api/meals/{meal_id}` - Consultar detalhes de uma refeição específica.  
    - ⭐ **PATCH** `/api/meals/{meal_id}/favorite` - Favoritar ou desfavoritar uma refeição.  
    - ❤️ **GET** `/api/meals/favorites` - Consultar todas as refeições favoritas.  
    - 📊 **GET** `/api/meals/report` - Gerar relatório de refeições consumidas.  
    - 🎯 **PUT** `/api/meals/report/goal` - Atualizar meta diária de calorias.  

- **/water**

    - ➕ **POST** `/api/water/add` - Adicionar ingestão de água.  
    - ❌ **DELETE** `/api/water/delete/{water_id}` - Excluir ingestão de água.  
    - 🔍 **GET** `/api/water` - Consultar ingestões de água.  
    - 💧 **GET** `/api/water/total` - Consultar total de água consumida.  
    - 🎯 **POST** `/api/water/goal` - Atualizar meta diária de água.

- **/users**

    - 👤 **POST** `/api/users/add` - Criar um usuário.  
    - 🔑 **POST** `/api/users/login` - Login do usuário.  
    - 🚪 **GET** `/api/users/logout` - Logout do usuário.   -->

## 📡 Estrutura de Endpoints

### 🍴 Refeições
- **➕ Adicionar**: `POST /api/meals/add` - Adiciona uma refeição.  
- **✏️ Atualizar**: `PUT /api/meals/update/{meal_id}` - Atualiza uma refeição.  
- **❌ Excluir**: `DELETE /api/meals/delete/{meal_id}` - Exclui uma refeição.  
- **🔍 Consultar**: `GET /api/meals` - Lista refeições com filtros.  
- **📋 Consultar Refeição Específica**: `GET /api/meals/{meal_id}` - Detalha uma refeição específica.  
- **⭐ Favoritar**: `PATCH /api/meals/{meal_id}/favorite` - Marca ou desmarca uma refeição como favorita.  
- **❤️ Refeições Favoritas**: `GET /api/meals/favorites` - Lista todas as refeições favoritas.  
- **📊 Relatório de Refeições**: `GET /api/meals/report` - Geração de relatório com informações sobre refeições consumidas.  
- **🎯 Atualizar Meta de Calorias**: `PUT /api/meals/calorie-goal` - Atualiza a meta diária de calorias.  
- **🔥 Streak de Calorias**: `GET /api/meals/calorie-goal/streak` - Consulta o streak de dias consecutivos atingindo a meta de calorias.

### 💧 Ingestão de Água
- **➕ Adicionar**: `POST /api/water/add` - Registra ingestão de água.  
- **❌ Remover**: `DELETE /api/water/delete/{water_id}` - Exclui ingestão de água.  
- **🔍 Consultar**: `GET /api/water` - Lista ingestões de água.  
- **💧 Total Consumido**: `GET /api/water/total` - Consulta total de água consumida.  
- **🎯 Atualizar Meta**: `POST /api/water/goal` - Atualiza meta diária de água.
- **🔥 Streak de Ingestão de Água**: `GET /api/water/streak` - Consulta o streak de dias consecutivos atingindo a meta de ingestão de água.

### 👤 Usuários
- **👤 Criar Usuário**: `POST /api/users/add` - Criar um usuário.
- **🔑 Login**: `POST /api/users/login` - Login do usuário.
- **🚪 Logout**: `GET /api/users/logout` - Logout do usuário.

---

## 🔗 Endpoints

## 🍽️ Refeições (`/api/meals`)

### 🍴 Adicionar Refeição
- **Descrição**: Adiciona uma nova refeição.
- **Método**: `POST`
- **Endpoint**: `/api/meals/add`

🌐 **Exemplo de Requisição**: `http://localhost:5000/api/meals/add`

📝 **Corpo da Requisição:**

```json
{
    "name": "Grilled Chicken",
    "description": "A protein-packed grilled chicken breast",
    "in_diet": true,
    "category": "LUNCH",
    "calories": 300
}
```

📄 **Exemplo de Resposta:**

```json
{
    "message": "Meal added successfully"
}
```

### ✏️ Atualizar Refeição
- **Descrição**: Atualiza os dados de uma refeição existente.
- **Método**: `POST`
- **Endpoint**: `/api/meals/update/{meal_id}`

🌐 **Exemplo de Requisição**: `http://localhost:5000/api/meals/update/{meal_id}`

📝 **Corpo da Requisição:**

```json
{
    "name": "Green Salad",
    "description": "A healthy green salad",
    "in_diet": true,
    "category": "SALAD",
    "calories": 150
}
```

📄 **Exemplo de Resposta:**

```json
{
    "message": "Meal updated successfully"
}
```

### ❌ Excluir Refeição
- **Descrição**: Exclui uma refeição registrada.
- **Método**: `DELETE`
- **Endpoint**: `/api/meals/delete/{meal_id}`

🌐 **Exemplo de Requisição**: `http://localhost:5000/api/meals/delete/{meal_id}`

📄 **Exemplo de Resposta:**

```json
{
    "message": "Meal deleted successfully"
}
```

### 🔍 Consultar Refeições
- **Descrição**: Consulta as refeições registradas com filtros opcionais.
- **Método**: `GET`
- **Endpoint**: `/api/meals`
- **Parâmetros de consulta (opcionais)**:
  - `category`: Filtro por categoria (`LUNCH`, `SNACK`, `SALAD`, etc).
  - `in_diet`: Filtro por status de dieta (`true` ou `false`).
  - `period`: Período para filtragem (`day`, `week`, `month`).
  - `start_date`: Data de início (formato YYYY-MM-DD).
  - `end_date`: Data de fim (formato YYYY-MM-DD).

🌐 **Exemplo de Requisição**: `http://localhost:5000/api/meals?period=day&in_diet=true`

📄 **Exemplo de Resposta:**

```json
[
    {
        "calories": 300.0,
        "category": "LUNCH",
        "date_time": "Fri, 15 Nov 2024 14:42:47 GMT",
        "description": "A protein-packed grilled chicken breast",
        "favorite": false,
        "id": 1,
        "in_diet": true,
        "name": "Grilled Chicken"
    },
    {
        "calories": 150.0,
        "category": "SALAD",
        "date_time": "Fri, 15 Nov 2024 14:42:58 GMT",
        "description": "A healthy green salad",
        "favorite": false,
        "id": 2,
        "in_diet": true,
        "name": "Green Salad"
    }
]
```

### 🆔 Consultar Refeições por ID
- **Descrição**: Consulta uma refeição especifica pelo ID.
- **Método**: `GET`
- **Endpoint**: `/api/meals/{meal_id}`

🌐 **Exemplo de Requisição**: `http://localhost:5000/api/meals/{meal_id}`

📄 **Exemplo de Resposta:**

```json
{
    "calories": 300.0,
    "category": "LUNCH",
    "date_time": "Fri, 15 Nov 2024 14:42:47 GMT",
    "description": "A protein-packed grilled chicken breast",
    "favorite": false,
    "id": 1,
    "in_diet": true,
    "name": "Grilled Chicken"
}
```

### ❤️ Favoritar Refeição
- **Descrição**: Marca ou desmarca uma refeição como favorita.
- **Método**: `PATCH`
- **Endpoint**: `/api/meals/{meal_id}/favorite`

🌐 **Exemplo de Requisição**: `http://localhost:5000/api/meals/{meal_id}/favorite`

📄 **Exemplo de Resposta:**

```json
{
    "favorite": true,
    "meal_id": 1,
    "message": "Meal favorite status updated successfully"
}
```

### ⭐ Listar Refeições Favoritas
- **Descrição**: Lista as refeições marcadas como favorito.
- **Método**: `PATCH`
- **Endpoint**: `/api/meals/favorites`

🌐 **Exemplo de Requisição**: `http://localhost:5000/api/meals/favorites`

📄 **Exemplo de Resposta:**

```json
{
    "favorite_meals": [
        {
            "calories": 300.0,
            "date_time": "Fri, 15 Nov 2024 14:42:47 GMT",
            "id": 1,
            "in_diet": true,
            "name": "Grilled Chicken"
        }
    ]
}
```

### 📅 Relatório de Refeições
- **Descrição**: Gera um relatório das refeições por data (dia, semana, mês).
- **Método**: `GET`
- **Endpoint**: `/api/meals/report`
- **Parâmetros de consulta (opcionais)**:
  - `period`: Período para filtragem (`day`, `week`, `month`).
  - `start_date`: Data de início (formato YYYY-MM-DD).
  - `end_date`: Data de fim (formato YYYY-MM-DD).

🌐 **Exemplo de Requisição**: `http://localhost:5000/api/meals/report?period=day`

📄 **Exemplo de Resposta:**

```json
{
    "calorie_goal": 2000.0,
    "end_date": "2024-11-15",
    "meals_in_diet": 2,
    "meals_out_of_diet": 0,
    "progress": 22.5,
    "start_date": "2024-11-15",
    "total_calories": 450.0
}
```


### 🎯 Atualizar Meta de Calorias
- **Descrição**: Ajusta a meta diária de calorias.
- **Método**: `POST`
- **Endpoint**: `/api/meals/calorie-goal`

🌐 **Exemplo de Requisição**: `http://localhost:5000/api/meals/calorie-goal`

📝 **Corpo da Requisição:**

```json
{
  "daily_calorie_goal": 3000
}
```

📄 **Exemplo de Resposta:**

```json
{
    "message": "Daily calorie goal successfully updated to 3000"
}
```

### 🔥 Streak de Calorias
- **Descrição**: Calcula e exibe a sequência de dias em que o usuário atingiu sua meta diária de calorias.
- **Método**: `GET`
- **Endpoint**: `/api/meals/calorie-goal/streak`

🌐 **Exemplo de Requisição**: `http://localhost:5000/api/meals/calorie-goal/streak`

📄 **Exemplo de Resposta:**

```json
{
    "streak": 10
}
```

---

## 💧 Ingestão de Água (`/api/water`)

### 💧 Adicionar Ingestão de Água
- **Descrição**: Registra uma ingestão de água.
- **Método**: `POST`
- **Endpoint**: `/api/water/add`

🌐 **Exemplo de Requisição**: `http://localhost:5000/api/water/add`

📝 **Corpo da Requisição:**

```json
{
  "quantity": 250
}
```

📄 **Exemplo de Resposta:**

```json
{
    "date_time": "2024-11-15 15:53:28",
    "message": "Water intake recorded successfully",
    "quantity": 250.0
}
```

### ❌ Remover Ingestão de Água
- **Descrição**: Exclui um registro de ingestão de água.
- **Método**: `DELETE`
- **Endpoint**: `/api/water/delete/{water_id}`

🌐 **Exemplo de Requisição**: `http://localhost:5000/api/delete/{water_id}`

📄 **Exemplo de Resposta:**

```json
{
    "message": "Water intake removed successfully"
}
```

### 📅 Consultar Ingestão de Água
- **Descrição**: Consulta os registros de ingestão de água.
- **Método**: `GET`
- **Endpoint**: `/api/water`
- **Parâmetros de consulta (opcionais)**:
  - `period`: Período para filtragem (`day`, `week`, `month`).
  - `start_date`: Data de início (formato YYYY-MM-DD).
  - `end_date`: Data de fim (formato YYYY-MM-DD).

🌐 **Exemplo de Requisição**: `http://localhost:5000/api/water?period=day`

📄 **Exemplo de Resposta:**

```json
[
    {
        "date_time": "2024-11-15 15:54:48",
        "id": 1,
        "quantity": 250.0
    },
    {
        "date_time": "2024-11-15 15:54:57",
        "id": 2,
        "quantity": 500.0
    }
]
```

### 📈 Total de Água Consumida
- **Descrição**: Obtém o total de água consumida em um período específico.
- **Método**: `GET`
- **Endpoint**: `/api/water/total`
- **Parâmetros de consulta**:
  - `period`: Período para filtragem (`day`, `week`, `month`).
  - `start_date`: Data de início (formato YYYY-MM-DD).
  - `end_date`: Data de fim (formato YYYY-MM-DD).

🌐 **Exemplo de Requisição**: `http://localhost:5000/api/water/total`

📄 **Exemplo de Resposta:**

```json
{
    "period": "day",
    "progress": 37.5,
    "total_water": 750.0,
    "water_goal": 2000.0
}
```

### 🎯 Atualizar Meta de Ingestão de Água
- **Descrição**: Ajusta a meta diária de ingestão de água.
- **Método**: `POST`
- **Endpoint**: `/api/water/goal`

🌐 **Exemplo de Requisição**: `http://localhost:5000/api/water/goal`

📝 **Corpo da Requisição:**

```json
{
  "daily_water_goal": 3000
}
```

📄 **Exemplo de Resposta:**

```json
{
    "message": "Daily water intake goal successfully updated to 3000"
}
```

### 🔥 Streak de Ingestão de Água
- **Descrição**: Calcula e exibe a sequência de dias em que o usuário atingiu sua meta diária de ingestão de água.
- **Método**: `GET`
- **Endpoint**: `/api/water/streak`

🌐 **Exemplo de Requisição**: `http://localhost:5000/api/water/streak`

📄 **Exemplo de Resposta:**

```json
{
    "streak": 10
}
```

---

## 👤 Usuários (`/api/users`)

### 👤 Criar Usuário
- **Descrição**: Cria um novo usuário.
- **Método**: `POST`
- **Endpoint**: `/api/users/add`

🌐 **Exemplo de Requisição**: `http://localhost:5000/api/users/add`

📝 **Corpo da Requisição:**

```json
{
    "username": "joschonarth",
    "email": "joschonarth@gmail.com",
    "password": "123456"
}
```

📄 **Exemplo de Resposta:**

```json
{
    "message": "User successfully registered"
}
```

### 🔑 Login
- **Descrição**: Realiza o login do usuário.
- **Método**: `POST`
- **Endpoint**: `/api/users/login`

🌐 **Exemplo de Requisição**: `http://localhost:5000/api/users/login`

📝 **Corpo da Requisição:**

```json
{
    "email": "joschonarth@gmail.com",
    "password": "123456"
}
```

📄 **Exemplo de Resposta:**

```json
{
    "message": "Login successful",
    "user_id": 1
}
```

### 🚪 Logout
- **Descrição**: Realiza o logout do usuário.
- **Método**: `GET`
- **Endpoint**: `/api/users/logout`

🌐 **Exemplo de Requisição**: `http://localhost:5000/api/users/logout`

📄 **Exemplo de Resposta:**

```json
{
    "message": "Logout successful"
}
```

## Contribuições 🌟

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue com sugestões ou enviar um pull request com melhorias.

## 📜 Licença 

Este projeto está licenciado sob a [MIT License](LICENSE).

## 📞 Contato 

<div>
    <a href="https://www.linkedin.com/in/joschonarth/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
    <a href="mailto:joschonarth@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
</div>
