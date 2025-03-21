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

**Frontend:** React, Vite

**Backend:** FastAPI

**Image Processing:** Pillow

**Database** SQLite

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
```

## Authors

- [@Aleks Seriakov](https://github.com/Fialex1212)

