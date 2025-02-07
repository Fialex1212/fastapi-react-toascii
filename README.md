# React&FastApi Img to ASCII

## Description
The ASCII Art Converter is a web application that allows users to upload images by link or file and convert them into ASCII art. The app utilizes a React frontend for a responsive user interface and a FastAPI backend for efficient image processing.

## Features
- Image Upload: Users can easily upload images from their devices. The frontend handles
  file input and provides a preview of the uploaded image.

- Conversion Process:
  - The uploaded image is sent to the FastAPI backend.
  - FastAPI processes the image, converting it into ASCII art using specific algorithms.
  - The resulting ASCII art is returned to the frontend.

- Responsive Design: Built with React, the app features a clean and intuitive
  interface that works well on both desktop and mobile devices.


## Tech Stack

**Frontend:** React, TailwindCSS

**Backend:** FastAPI

**Image Processing:** Pillow

## Installation

Clone my project
```cmd
    git clone https://github.com/Fialex1212/react-fastapi-todo.git
```

### Frontend
Run the frontend

```bash
  cd frontend
  npm install
  npm run dev
```

### Backend
Run the backend

```cmd
  cd backend
  python -m venv venv
  .\venv\scripts\activate
  pip install requirements.txt
  uvicorn src.main:app
```## API Reference

### Create a todo

```http
  POST /api/todo/create
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `todo` | `TodoCreate` | **Required**. Data of task |

#### Query example
```json
{
    "title": "Create new app",
    "description": "Create new app with cool functional",
}
```
#### Response example
```json
  {
    "title": "Title",
    "description": "Description",
    "is_completed": false,
    "id": "a46283a7-368d-4725-a4e2-dcf6698bc4a8",
    "created_at": "2024-09-26T15:40:37.044667",
    "updated_at": "2024-09-26T15:40:37.044667"
  }
```
### Get todo

```http
  GET /api/todo/get/{todo_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `todo_id`      | `string` | **Required**. Id of todo |

#### Response example
```json
  {
    "title": "Title",
    "description": "Description",
    "is_completed": false,
    "id": "a46283a7-368d-4725-a4e2-dcf6698bc4a8",
    "created_at": "2024-09-26T15:40:37.044667",
    "updated_at": "2024-09-26T15:40:37.044667"
  }
```

### Get list of todo

```http
  GET /api/todo/list?skip={skip}&limit={limit}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `skip`      | `int` | Skip first N tasks (default 0) |
| `limit`      | `int` | Limit the number of tasks (default 100) |

#### Response example
```json
[
  {
    "title": "Title",
    "description": "Description",
    "is_completed": false,
    "id": "a2dc9498-1da2-4106-8dd5-8093028912ae",
    "created_at": "2024-09-26T15:40:37.044667",
    "updated_at": "2024-09-26T15:40:37.044667"
  },
  {
    "title": "Title",
    "description": "Description",
    "is_completed": false,
    "id": "a46283a7-368d-4725-a4e2-dcf6698bc4a8",
    "created_at": "2024-09-26T15:40:37.044667",
    "updated_at": "2024-09-26T15:40:37.044667"
  }
]
```
### Update todo

```http
  PUT /api/todo/update/{todo_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `todo_id`      | `string` | **Required**. Id of todo |

#### Query example
```json
{
  "title": "Title",
  "description": "Description",
  "is_completed": true
}
```
#### Response example
```json
{
  "created_at": "2024-09-26T15:40:37.044667",
  "description": "Description",
  "is_completed": false,
  "id": "a46283a7-368d-4725-a4e2-dcf6698bc4a8",
  "title": "Title",
  "updated_at": "2024-09-26T15:40:37.044667"
}
```

### Delete todo

```http
  DELETE /api/todo/delete/{todo_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `todo_id`      | `string` | **Required**. Id of todo |


#### Response example
```json
{
  "created_at": "2024-09-26T15:40:37.044667",
  "description": "Description",
  "is_completed": false,
  "id": "a46283a7-368d-4725-a4e2-dcf6698bc4a8",
  "title": "Title",
  "updated_at": "2024-09-26T15:40:37.044667"
}
```
## Screenshots

### Desktop
![Desktop app Screenshot](./images/1.jpg)

### Table
![Table app Screenshot](./images/2.jpg)

### Mobile
![Mobile app Screenshot](./images/3.jpg)


## Authors

- [@Aleks Seriakov](https://github.com/Fialex1212)

