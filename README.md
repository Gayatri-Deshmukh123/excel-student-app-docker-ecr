# Student Excel Data Web Application | Docker & AWS ECR

## Project Overview

This project is a Python-based web application that reads student records from an Excel file and displays them on a webpage using Flask.

The application is containerized using Docker, and the Docker images are stored in Amazon Elastic Container Registry (ECR). Whenever the Excel data is updated, a new Docker image version can be built and pushed to ECR.

This project demonstrates application development, containerization, image versioning, deployment, and rollback.

## Objectives

- Read student data from an Excel file using Python.
- Display student records on a webpage using Flask.
- Containerize the application using Docker.
- Store Docker images in Amazon ECR.
- Maintain multiple image versions such as v1, v2, and v3.
- Deploy updated application versions.
- Perform rollback to a previous stable version.

## Technologies Used

- Python
- Pandas
- Flask
- HTML
- Docker
- Amazon Elastic Container Registry (ECR)
- AWS CLI
- Git
- GitHub
- Visual Studio Code

## Architecture

The application follows this workflow:

1. Student records are stored in an Excel file.
2. Python reads the Excel data using Pandas.
3. Flask processes the data and renders it on an HTML webpage.
4. Docker packages the application, dependencies, and Excel file into an image.
5. The Docker image is tagged with a version.
6. The versioned image is pushed to Amazon ECR.
7. Updated images can be deployed as new containers.
8. If an update fails, a previous stable image can be used for rollback.

### Workflow

Excel File → Python → Flask → HTML Webpage → Docker Image → Amazon ECR → Container Deployment

## Project Structure

```text
Student-Excel-Docker/
│
├── app.py
├── students.xlsx
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── README.md
│
├── templates/
│   └── index.html
│
└── screenshots/
```

## Application Features

- Reads student records from an Excel workbook.
- Displays student details in a webpage.
- Uses Flask to serve the web application.
- Updates webpage data when the Excel file is modified and the application reloads the data.
- Runs inside a Docker container.
- Supports multiple Docker image versions.
- Stores versioned images in Amazon ECR.
- Supports running different versions using Docker port mapping.
- Allows previous versions to be restored.

## Local Setup and Execution

### 1. Clone the Repository

```bash
git clone [github.com/Gayatri-Deshmukh123]
cd Student-Excel-Docker
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the virtual environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```
If having Execution-policy issue:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

Open the application in a browser using the local URL configured by the Flask application.

## Docker Implementation

The application is containerized using Docker to provide a consistent runtime environment.

### Build the Docker Image

```bash
docker build -t student-management:v1 .
```

### Run the Container

```bash
docker run -d -p 5000:5000 --name student-app-v1 student-management:v1
```

### Verify the Running Container

```bash
docker ps
```

### View Docker Images

```bash
docker images
```

### View Container Logs

```bash
docker logs student-app-v1
```

## Docker Image Versioning

Different versions of the application are built to represent changes in student records or application updates.

| Image Version | Description |
|---|---|
| v1 | Initial application release |
| v2 | Updated student records |
| v3 | Further updated application/data release |

Each version is assigned a unique tag to identify the corresponding release.

## Amazon ECR Implementation

Amazon Elastic Container Registry (ECR) is used as a private container image registry to store Docker images.

### Steps Performed

1. Created a private ECR repository.
2. Configured AWS CLI.
3. Authenticated Docker with Amazon ECR.
4. Tagged local Docker images with the ECR repository URI.
5. Pushed image versions to ECR.
6. Verified uploaded images and tags in the AWS Console.

### Image Storage

The repository stores multiple versions of the application, allowing different releases to be retrieved when required.

Example tags:

- v1
- v2
- v3

## Application Update Workflow

When student records are modified:

1. Update the Excel file.
2. Verify the updated data using the application.
3. Build a new Docker image.
4. Assign a new version tag.
5. Run the updated image in a container.
6. Verify the application output.
7. Push the new version to Amazon ECR.

This process keeps previous image versions available for comparison and recovery.

## Rollback

Rollback is performed by returning to a previously working Docker image version.

If the latest version has an issue:

1. Identify the last stable image version.
2. Stop the container running the faulty version.
3. Retrieve the previous image if it is not available locally.
4. Run a new container using the stable image tag.
5. Verify the application is working correctly.

Maintaining versioned images in ECR makes it possible to restore a previous application release without rebuilding it from scratch.

## Screenshots and Project Evidence

Screenshots demonstrating the project implementation are available in the `screenshots/` directory.

Evidence includes:

- Excel student data
- Python application output
- Flask webpage
- Docker images
- Running Docker containers
- Application updates
- Amazon ECR repository and image tags
- Rollback demonstration

## Challenges and Learning

Through this project, I gained practical experience in:

- Reading structured data from Excel using Python.
- Building a web application using Flask.
- Connecting Python logic with HTML templates.
- Creating Docker images and containers.
- Understanding Docker port mapping.
- Managing Docker image tags.
- Authenticating Docker with Amazon ECR.
- Pushing images to a cloud registry.
- Managing multiple application versions.
- Understanding rollback and recovery of previous releases.
- Troubleshooting application and container issues.

## Conclusion

This project demonstrates the workflow of developing a Python web application, packaging it using Docker, storing versioned images in Amazon ECR, and managing application updates and rollback.

It helped me understand the practical relationship between application development, containerization, cloud image storage, and release management.

---

**Author:** Gayatri Deshmukh  
**Project:** Student Excel Docker ECR
