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

### 💧 Ingestão de Água

- 💦 **Adicionar Ingestão de Água**: Registrar quantidade de água ingerida.
- ❌ **Remover Ingestão de Água**: Excluir um registro específico de ingestão de água.
- 📅 **Consultar Ingestão de Água**: Consultar ingestões de água com filtros de dia, semana e mês.
- 📈 **Total de Água Consumida**: Obter o total de água consumida em um período, com progresso em relação à meta.
- 🎯 **Atualizar Meta de Ingestão de Água**: Ajustar a meta diária de ingestão de água.


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

## 📡 Estrutura de Endpoints

### 🍴 Refeições
- **Adicionar**: `POST /api/meals/add` - Adiciona uma refeição.
- **Atualizar**: `PUT /api/meals/update/{meal_id}>` - Atualiza uma refeição.
- **Excluir**: `DELETE /api/meals/delete/{meal_id}` - Exclui uma refeição.
- **Consultar**: `GET /api/meals` - Lista refeições com filtros.
- **Consultar Refeição Específica**: `GET /api/meals/{meal_id}` - Detalha uma refeição específica.
- **Favoritar**: `PATCH /api/meals/{meal_id}/favorite` - Marca ou desmarca uma refeição como favorita.
- **Refeições Favoritas**: `GET /api/meals/favorites` - Lista todas as refeições favoritas.
- **Relatório de Refeições**: `GET /api/meals/report` - Geração de relatório com informações sobre refeições consumidas no período selecionado (dia, semana ou mês).
- **Atualizar Meta de Calorias**: `PUT /api/meals/report/goal` - Atualiza a meta diária de calorias.

### 💧 Ingestão de Água
- **Adicionar**: `POST /api/water/add` - Registra ingestão de água.
- **Remover**: `DELETE /api/water/delete/{water_id}` - Exclui ingestão de água.
- **Consultar**: `GET /api/water` - Lista ingestões de água.
- **Total Consumido**: `GET /api/water/total` - Consulta total de água consumida.
- **Atualizar Meta**: `POST /api/water/goal` - Atualiza meta diária de água.

## 🔗 Endpoints

### 🍴 Adicionar Refeição
- **Descrição**: Adiciona uma nova refeição.
- **Método**: `POST`
- **Endpoint**: `/api/meals/add`
- **Campos**:
  - `name`: Nome da refeição (string).
  - `description`: Descrição da refeição (string).
  - `category`: Categoria da refeição (string).
  - `calories`: Quantidade de calorias (int).
  - `diet_status`: Status da dieta (string).

### ✏️ Atualizar Refeição
- **Descrição**: Atualiza os dados de uma refeição existente.
- **Método**: `POST`
- **Endpoint**: `/api/meals/update/{meal_id}`
- **Campos**:
  - `name`: Nome da refeição (string).
  - `description`: Descrição da refeição (string).
  - `category`: Categoria da refeição (string).
  - `calories`: Quantidade de calorias (int).
  - `diet_status`: Status da dieta (string).

### ❌ Excluir Refeição
- **Descrição**: Exclui uma refeição registrada.
- **Método**: `DELETE`
- **Endpoint**: `/api/meals/delete/{meal_id}`

### 🔍 Consultar Refeições
- **Descrição**: Consulta as refeições registradas com filtros opcionais.
- **Método**: `GET`
- **Endpoint**: `/api/meals`
- **Parâmetros de consulta**:
  - `category`: Filtro por categoria (opcional).
  - `diet_status`: Filtro por status de dieta (opcional).
  - `start_date`: Filtro por data inicial (opcional).
  - `end_date`: Filtro por data final (opcional).

### ❤️ Favoritar Refeição
- **Descrição**: Marca uma refeição como favorita.
- **Método**: `POST`
- **Endpoint**: `/api/meals/favorite/{meal_id}`

### 📅 Filtragem de Refeições
- **Descrição**: Filtra refeições por data (dia, semana, mês).
- **Método**: `GET`
- **Endpoint**: `/api/meals/filter`
- **Parâmetros de consulta**:
  - `period`: Período para filtragem (dia, semana, mês).
  - `start_date`: Data de início (opcional).
  - `end_date`: Data de fim (opcional).

---

### 💧 Adicionar Ingestão de Água
- **Descrição**: Registra uma ingestão de água.
- **Método**: `POST`
- **Endpoint**: `/api/water/add`
- **Campos**:
  - `amount`: Quantidade de água ingerida (float).

### ❌ Remover Ingestão de Água
- **Descrição**: Exclui um registro de ingestão de água.
- **Método**: `DELETE`
- **Endpoint**: `/api/water/delete/{water_id}`

### 📅 Consultar Ingestão de Água
- **Descrição**: Consulta os registros de ingestão de água.
- **Método**: `GET`
- **Endpoint**: `/api/water`
- **Parâmetros de consulta**:
  - `start_date`: Filtro por data inicial (opcional).
  - `end_date`: Filtro por data final (opcional).

### 📈 Total de Água Consumida
- **Descrição**: Obtém o total de água consumida em um período específico.
- **Método**: `GET`
- **Endpoint**: `/api/water/total`
- **Parâmetros de consulta**:
  - `start_date`: Filtro por data inicial (opcional).
  - `end_date`: Filtro por data final (opcional).

### 🎯 Atualizar Meta de Ingestão de Água
- **Descrição**: Ajusta a meta diária de ingestão de água.
- **Método**: `POST`
- **Endpoint**: `/api/water/goal`
- **Campos**:
  - `goal`: Nova meta diária de ingestão de água (float).

## Contribuições 🌟

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue com sugestões ou enviar um pull request com melhorias.

## 📜 Licença 

Este projeto está licenciado sob a [MIT License](LICENSE).

## 📞 Contato 

<div>
    <a href="https://www.linkedin.com/in/joschonarth/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
    <a href="mailto:joschonarth@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
</div>
