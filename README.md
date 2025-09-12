# EventSphere

**EventSphere** is a comprehensive web-based platform designed to manage and promote cultural, technical, and sports events. It enables organizers to publish events and allows students to browse, register, and provide feedback, all within a secure and user-friendly environment.

## Project Description
EventSphere enables organizers to create events with relevant details such as title, description, date, and category. Students can view these events, register or unregister, and provide feedback after participation. The platform includes user authentication, categorized event listings, search and filter functionality, and simulated registration confirmation messages.

## Features

### Core Functionality

- **User Authentication**  
  Secure signup and login system for both organizers and students.

- **Event Management for Organizers**  
  Organizers can create and manage events by specifying the title, description, category, and scheduled date.

- **Student Registration System**  
  Students can view available events, register for participation, and unregister if needed.

- **Upcoming Events Display**  
  A dynamic homepage showcases all upcoming events with relevant details including name, category, and date.

### Enhanced Capabilities

- **Event Categorization**  
  Events are classified into distinct categories—Technical, Cultural, and Sports—for streamlined browsing.

- **Search and Filter Options**  
  Users can search for specific events or apply filters based on category or date to refine results.

- **Registration Confirmation**  
  Upon successful registration, users receive a confirmation message. Email simulation is included to mimic real-world workflows.

- **Feedback Mechanism**  
  After attending an event, students can submit feedback to help organizers improve future experiences.

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Django (Python)  
- **Database**: SQLite  
- **Version Control**: Git and GitHub

## Setup Instructions
To run the project locally, follow the steps below:

- git clone https://github.com/keerthi-manasvi/event-sphere.git
- cd event-sphere
- python -m venv env
- source env/bin/activate  # For Windows: env\Scripts\activate
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver
Once the server is running, access the application at: http://127.0.0.1:8000
## Live Deployment
You can access the deployed version of EventSphere at: 
https://event-sphere-1-iqxz.onrender.com
