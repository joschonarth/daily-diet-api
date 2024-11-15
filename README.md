# 🍽️ Daily Diet API

A Daily Diet API é uma solução prática para registrar e acompanhar refeições e ingestão de água diária, oferecendo recursos para adicionar, atualizar e consultar refeições com detalhes como calorias e status de dieta. Também permite definir e monitorar metas de consumo de água, com filtros personalizados. Desenvolvida em Python com Flask e SQLAlchemy, esta API é ideal para quem deseja manter uma alimentação balanceada e controlar hábitos saudáveis.

## ⚙️ Funcionalidades

### 🥗 Refeições

- 🍴 **Adicionar Refeição**: Criação de novas refeições com nome, descrição, categoria, calorias e status de dieta.
- ✏️ **Atualizar Refeição**: Modificação dos dados de uma refeição existente.
- ❌ **Excluir Refeição**: Exclusão de uma refeição.
- 🔍 **Consultar Refeições**: Listagem de refeições com filtros por categoria, status de dieta, e período.
- ❤️ **Favoritar Refeição**: Marcação de refeições como favoritas.
- 📅 **Filtragem de Refeições**: Filtros por data (dia, semana, mês) ou intervalo de datas personalizadas.

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