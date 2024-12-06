# task_management_api# Task Management API

A RESTful API for managing tasks built with Django REST Framework.

## Setup

1. Clone the repository
   `git clone https://github.com/titima20/task_management_api.git`

2. Create and activate virtual environment
   python -m venv venv source venv/bin/activate # Unix/MacOS venv\Scripts\activate # Windows

3. Install dependencies
   `pip install -r requirements.txt`

4. Run migrations
   `python manage.py migrate`

5. Start development server
   `python manage.py runserver`

## API Endpoints

- `/api/tasks/` - Task CRUD operations
- `/api/users/` - User management
