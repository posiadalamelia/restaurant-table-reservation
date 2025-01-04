# Restaurant Table Reservation System
  
## Overview
Web application for managing restaurant table reservations. Customers can make reservations online, while administrators manage them via an admin panel.

## Project Structure
### Containers 
The project is divided into two main containers:
1. Application Container (Backend + Frontend):
    * Technologies: Python, HTML, CSS  
    * Framework: Flask
    * Port: 5000
    * Key Features:
        * A home page with a reservation form.
        * An admin panel for managing reservations.

2. Database Container:
    * Technology: Redis
    * Port: 6379
    * Functions:
        * Key-value storage for reservation data.
        * Fast data access and management.

### Technologies Used:
* Backend: Python 3.11
* Backend Framework: Flask
* Frontend: HTML, CSS
* Database: Redis
* Containerization: Docker, Docker Compose
* OS: Linux (Ubuntu)
* Version Control: Git

## Core Features
1. Main Page: Reservation form with redirect to confirmation page.
2. Admin Panel (/admin): Viev, search, edit and delete reservations.
3. Redis Database: Key-value storage for reservations. 
4. Container communication: Via app-network in Docker Compose

# Setup and Installation
1. Clone Repository:
    ``` bash
    $ git clone https://github.com/posiadalamelia/restaurant-table-reservation.git
    ```
2. Run Container 
    > **Note:**
    > You need to have [Docker](https://docs.docker.com/engine/install/) installed on your machine.
    ```bash
    # Run docker containers with compose
    $ docker-compose up -d --build
    ```
3. Access the application:
    * **Main Page** : http://localhost:5000
    * **Admin Panel**: http://localhost:5000/admin

## Plans for future
Add login panel for workers and limit reservations through specific number of tables. 






 
