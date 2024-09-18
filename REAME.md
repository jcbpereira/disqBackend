# disqBackend

This is a Django project named `disqBackend`. It includes a Django application named `disqdb` and is configured to use CORS headers and PostgreSQL as the database.

## Prerequisites

- Python 3.x
- Django 3.x or higher
- PostgreSQL
- `pip` (Python package installer)

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/disqBackend.git
   cd disqBackend

2. **Run database migrations**:
Set up the environment variables: Create a .env file in the project root directory and add the following variables:
    ```sh
    SECRET_KEY='your-secret-key'
    DEBUG=True
    DB_NAME='your_database_name'
    DB_USER='your_database_user'
    DB_PASSWORD='your_database_password'
    DB_HOST='your_database_host'
    DB_PORT='5432'
    ```

## Running

1. **Run database migrations**:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```
    If you make any changes to the model you need to run this again.

2. **Run development server**:
    ```sh
    python manage.py runserver
    ```

### Running Locally

1.  **Connect to local DB**:

2. **Tunelling for development**:

    Run
    ```sh
    ngrok http 8000
    ```
    And use the url that local host is being forwarded to
    ```sh
    Forwarding                    https://2a04-148-252-146-117.ngrok-free.app -> http://localhost:8000   
    ```