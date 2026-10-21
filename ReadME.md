
# Placement Tracker 

This is a web application built using Python and Flask.The goal of this is to help students organise and track their placement and internship applications.

## About the Project

Applying for placements can involve keeping track of multiple companies, roles, deadlines and application stages.

I built Placement Tracker with the goal of making this easier by keeping application information in one place.

This project helped me develop my skills in Python, web development, databases and building full-stack applications.

## Features

- Add new placement and internship applications
- View all saved applications
- Edit application details
- Delete applications with a confirmation prompt
- Search applications by company name
- Filter applications by status
- Track total applications, interviews and offers on a dashboard
- Responsive interface with a lilac-purple design
- Basic server-side form validation

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML
- CSS
- Jinja2
- Git and GitHub

## How to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/ogualarachel/placement-tracker.git
   ```

2. Open the project folder:

   ```bash
   cd placement-tracker
   ```

3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment.

   Windows:

   ```powershell
   .venv\Scripts\activate
   ```

5. Install the required packages:

   ```bash
   python -m pip install -r requirements.txt
   ```

6. Start the application:

   ```bash
   python app.py
   ```

7. Open your browser at:

   http://127.0.0.1:5000
 SQLite database is created automatically when the application starts.

## What I Learned

Through this project, I practised:

- Creating routes and handling HTTP requests with Flask
- Connecting a Python application to a SQLite database
- Performing CRUD operations
- Using Jinja2 to display dynamic data
- Validating user input
- Building and styling a responsive web interface
- Using Git for version control

## Future Improvements

- User accounts and authentication
- CSRF protection for forms
- Deadline reminders
- More advanced application statistics
- Secure production deployment

## Project Status

Working local portfolio project. Further security hardening and testing are planned before public deployment.
