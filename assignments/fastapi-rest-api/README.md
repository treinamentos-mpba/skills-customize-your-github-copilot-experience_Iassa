# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST com FastAPI e pratique a definição de endpoints, a validação de dados com Pydantic e o uso de métodos HTTP e códigos de status. A API gerenciará tarefas em memória, sem banco de dados.

## 📝 Tasks

### 🛠️ Criar a API e listar tarefas

#### Description

Use o arquivo `starter-code.py` para executar uma aplicação FastAPI. Instale o FastAPI e o Uvicorn com `python -m pip install fastapi uvicorn` e inicie a aplicação com `python starter-code.py`.

#### Requirements

O programa concluído deve:

- Armazenar as tarefas em uma coleção mantida em memória.
- Disponibilizar `GET /health`, retornando `{"status": "ok"}`.
- Disponibilizar `GET /tasks`, retornando as tarefas em um array JSON, inclusive um array vazio quando não houver tarefas.

### 🛠️ Criar e consultar tarefas

#### Description

Adicione endpoints para criar uma tarefa e consultá-la pelo ID. Use os modelos Pydantic fornecidos como ponto de partida para validar os dados das requisições.

#### Requirements

O programa concluído deve:

- Aceitar um `title` não vazio e um campo opcional `completed`, cujo valor padrão é `false`.
- Disponibilizar `POST /tasks`, atribuir um ID único a cada tarefa e retornar a tarefa criada com o código de status `201`.
- Disponibilizar `GET /tasks/{task_id}` e retornar o código de status `404` quando o ID não existir.

### 🛠️ Atualizar e excluir tarefas

#### Description

Complete a API com endpoints para atualizar e remover tarefas existentes. Em seguida, teste os endpoints pela documentação interativa do FastAPI.

#### Requirements

O programa concluído deve:

- Disponibilizar `PUT /tasks/{task_id}` para atualizar o título e o estado de conclusão de uma tarefa.
- Disponibilizar `DELETE /tasks/{task_id}` e retornar o código de status `204`, sem corpo na resposta, quando a exclusão for concluída.
- Retornar o código de status `404` quando uma atualização ou exclusão tentar acessar um ID inexistente.
- Permitir testar os endpoints em `/docs`.