# Internship Training

This repository contains my weekly internship training tasks and practice projects.

## Week 1 - Docker Setup & English for IT

### Technical Tasks

* Install Docker Desktop & Docker Compose
* Deploy MySQL using Docker
* Create a simple Dockerfile
* Build and run a simple web application with Nginx

### English Tasks

* English for IT B1+
* Complete Module 1
* Learn virtualization-related vocabulary

---

## Week 2 - MinIO Object Storage

### Technical Tasks

* Deploy MinIO Object Storage using Docker Compose
* Access the MinIO Console
* Create the `week2-images` bucket
* Configure bucket access policy
* Upload an image to MinIO using Python
* Retrieve an image from MinIO using Python

### Technologies

* Docker
* Docker Compose
* MinIO
* Python
* MinIO Python SDK

### Week 2 Project Structure

```text
week2-minio/
├── app.py
├── docker-compose.yml
├── requirements.txt
├── images/
│   └── test.jpg
└── downloaded-test.jpg
```

### Run MinIO

```bash
docker compose up -d
```

MinIO Console:

```text
http://localhost:9001
```

### Install Python Dependencies

```bash
python -m pip install -r requirements.txt
```

### Run Upload & Retrieve Script

```bash
python app.py
```

Expected output:

```text
Upload successful!
Retrieve successful!
```

### English Tasks

* Complete Module 2
* Learn 10 new keywords related to File Storage and Cloud Computing

---

## Repository Structure

```text
intern-training/
├── week1-docker/
├── week2-minio/
└── README.md
```

## Author

**Võ Đình Hưng**
