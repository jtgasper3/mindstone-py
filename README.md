# Mindstone Py

## Overview
Mindstone Py is a Python application that interacts with an API to generate chat completions using a specified model. The application is designed to be run in a Docker container for easy setup and deployment.

## Project Structure
```
mindstone-py
├── main.py          # Main logic of the application
├── requirements.txt # Python dependencies
├── Dockerfile       # Docker instructions
└── README.md        # Project documentation
```

## Requirements
Make sure you have Docker installed on your machine to build and run the application.

## Setup
1. Clone the repository or download the project files.
2. Navigate to the project directory.

## Running the Application
To build and run the application using Docker, execute the following commands:

1. Build the Docker image:
   ```
   docker build -t mindstone-py .
   ```

2. Run the Docker container:
   ```
   docker run mindstone-py
   ```

## Dependencies
The project requires the following Python packages, which are listed in `requirements.txt`:
- requests
- json

## License
This project is licensed under the MIT License.