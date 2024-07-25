# Personal Finance Tracker

## Overview
Personal Finance Tracker is a web application designed to help users manage their income, expenses, and savings goals. The application allows users to input transactions, categorize them, and visualize their spending habits through charts and reports. It also includes features for setting and tracking savings goals.

## Distinctiveness and Complexity
This project is distinct from other projects in this course because it focuses on personal finance management rather than social networking or e-commerce. The complexity lies in the integration of dynamic data visualization, user authentication, and a responsive design.

## File Descriptions
- `finance_tracker/`: Root directory of the Django project.
- `tracker/`: Django app containing models, views, forms, and templates.
  - `models.py`: Defines the data models for users, transactions, categories, and goals.
  - `views.py`: Contains view functions for handling user requests and rendering templates.
  - `forms.py`: Defines forms for creating and updating transactions and goals.
  - `templates/`: Contains HTML templates for the application's frontend.
- `static/`: Contains static files such as CSS and JavaScript.
- `requirements.txt`: Lists Python packages required to run the application.

## How to Run the Application
1. Clone the repository.
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
3. Apply the migrations:
   ```bash
   python manage.py migrate
4. Create a superuser to access the admin panel:
   ```bash
   python manage.py createsuperuser
5. Run the development server:
   ```bash
   python manage.py runserver
## Additional Information
- The application uses Django for the backend and JavaScript for the frontend.
- Charts are implemented using the Chart.js library.
- The site is designed to be mobile-responsive using Bootstrap.
