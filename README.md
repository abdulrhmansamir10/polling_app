# Full-Stack Polling App with Docker

This is a full-stack, multi-container polling application where users can vote for their favorite programming language. This project is fully containerized using Docker and orchestrated with Docker Compose.

## ✨ Features

* View poll options and current vote counts.
* Cast a vote for an option.
* See vote counts update after voting.
* All services (frontend, backend, database) run in isolated Docker containers.

## 🚀 Tech Stack

* **Frontend:** React, Nginx (as a reverse proxy and static server)
* **Backend:** Python (Flask)
* **Database:** PostgreSQL
* **Containerization:** Docker, Docker Compose

## 🏁 Getting Started

### Prerequisites

Make sure you have Docker and Docker Compose installed on your machine.

* [Install Docker Engine](https://docs.docker.com/engine/install/)
* [Install Docker Compose](https://docs.docker.com/compose/install/)

### Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/abdulrhmansamir10/polling-app.git](https://github.com/abdulrhmansamir10/polling-app.git)
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd polling-app
    ```

3.  **Build and run the application:**
    ```bash
    docker-compose up --build
    ```
    The application will be available at [http://localhost:3000](http://localhost:3000).

4.  **Stop the application:**
    To stop and remove the containers, networks, and volumes, run:
    ```bash
    docker-compose down -v
    ```

## 📁 Project Structure
