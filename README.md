# Game Library API

A full-stack application for managing and displaying video game collections.

### Frontend Features

- Responsive grid layout of game cards
- Real-time game information display
- Clean and modern UI with dark mode support
- Type-safe development with TypeScript

### Backend Features

- Complete CRUD operations for game entries
- Robust data validation with Pydantic
- SQLite database integration
- Interactive API documentation

## Tech Stack

### Frontend
- Next.js
- TailwindCSS
- TypeScript
- Custom React Hooks

### Backend
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite

## Getting Started

### Frontend Setup
1. Install dependencies:
```bash
npm install
```

## Backend Setup Guide
Welcome to the Game Library API! This guide will help you get up and running quickly.

### Quick Start
1. Clone Repository
```bash
git clone <repository-url>
```
2. Set Up Virtual Environment
```bash
python -m venv venv
```
3. Activate Virtual Environment

- On Windows:
```bash
venv\Scripts\activate
```
- On macOS and Linux:
```bash
source venv/bin/activate
```
4. Install Dependencies
```bash
pip install -r requirements.txt
```
5. Launch Server
```bash
uvicorn app.main:app --reload
```
### Using the API
- Interactive API documentation: http://localhost:8000/docs
- API endpoints available at http://localhost:8000/api/v1/
- Supports full CRUD operations for game entries

### Key Features
- ✨ Modern FastAPI framework
- 📦 SQLite database integration
- ✅ Pydantic data validation
- 🔄 SQLAlchemy ORM
- 📚 Interactive Swagger documentation

### Next Steps
- Visit the API documentation
- Create your first game entry
- Explore the available endpoints
- Start building with the API