# Employee Records Management API

This Django-based API manages employee records and provides analytical insights.

## Git clone
   ```bash
   git clone https://github.com/sheikhrokonuzzman34/Managing-employee-records-API.git

   ``` 


## How to Run

1. Install dependencies: `pip install -r requirements.txt`
2. Apply migrations: `python manage.py migrate`
3. Run the server: `python manage.py runserver`

## Testing

Run the test suite:

```bash
python manage.py test
```   

## API Endpoints

### Departments

- **List and Create Departments:**
  - URL: `/departments/`
  - Method: `GET` (List), `POST` (Create)

- **Retrieve, Update, and Delete Department:**
  - URL: `/departments/<int:pk>/`
  - Method: `GET` (Retrieve), `PUT` (Update), `DELETE` (Delete)

### Employees

- **List and Create Employees:**
  - URL: `/employees/`
  - Method: `GET` (List), `POST` (Create)

- **Retrieve, Update, and Delete Employee:**
  - URL: `/employees/<int:pk>/`
  - Method: `GET` (Retrieve), `PUT` (Update), `DELETE` (Delete)

- **Employee Analytics:**
  - URL: `/analytics/`
  - Method: `GET`
  - Provides analytical data like employee count by department, average tenure, etc.





