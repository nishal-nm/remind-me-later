Remind-Me-Later is a web application that allows users to set reminders with a message, date, and time. The application supports two types of reminders: SMS and Email. The backend is built using Django and Django REST Framework (DRF) to store reminder details in the database. The app currently does not handle the actual message delivery but is designed to store the reminder data, and it can be extended to support other reminder types in the future.

To get started with the project, follow the steps below:

1. Clone the repository:  
   git clone https://github.com/nishal-nm/remind-me-later.git

2. Navigate to the project folder:  
   cd remind-me-later

3. Set up a virtual environment:  
   python -m venv .venv  
   source .venv/bin/activate # On Windows: .venv\Scripts\activate

4. Install the dependencies:  
   pip install -r requirements.txt

5. Create a `.env` file and add your Django `SECRET_KEY`:  
   SECRET_KEY=your_django_secret_key_here

6. Apply database migrations:  
   python manage.py migrate

7. Run the server:  
   python manage.py runserver

The API endpoint to create a reminder is available at `/api/reminder/create/`. You can make a POST request with the following JSON data:

{  
 "date": "2025-05-14",  
 "time": "16:30",  
 "message": "Attend team meeting",  
 "reminder_type": "email"  
}

The response will return the created reminder data, including the ID, message, date, time, and reminder type.

The project uses:

- Django and Django REST Framework for the backend
- SQLite as the database
- Python-dotenv to manage environment variables
