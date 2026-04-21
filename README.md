# 🛠️ Self-Healing Flask Infrastructure with Ansible

![Status](https://img.shields.io/badge/Status-Functional-brightgreen)
![Docker](https://img.shields.io/badge/Container-Docker-2496ed)
![Ansible](https://img.shields.io/badge/Automation-Ansible-ee0000)
![Python](https://img.shields.io/badge/Language-Python-3776ab)

This project implements an automated "Self-Healing" pipeline. It features a Python-based monitor that watches a Flask application running in Docker; if the service fails, the system automatically triggers an Ansible playbook to restart the container and extract logs for diagnosis.

---

## 🏗️ Architecture Overview

The system consists of three main layers:
1.  **Application Layer:** A Flask web server running inside a Python 3.10-slim Docker container.
2.  **Monitoring Layer:** A Python script utilizing `requests` or `urllib` to poll the service health every 5 seconds.
3.  **Healing Layer:** An Ansible runner that executes playbooks to restart the `flaskcc` container and save logs to a local file.

---

## 📂 Project Structure

* `app.py`: Simple Flask API with a `/submit` POST route.
* `dockerfile`: Containerizes the Flask environment.
* `requirements.txt`: Defines dependencies including `flask`, `ansible-runner`, and `ollama`.
* `Main Script.py`: The logic engine that triggers recovery upon service failure.
* `logs_checking.yaml`: Ansible playbook for container management and log extraction.
* `restart_container.yaml`: Simplified playbook for standard container restarts.

---

## 🚀 Deployment Guide

### 1. Build and Run the Container
First, package the Flask application into a Docker image and run it:
```bash
docker build -t flask-auto-heal .
docker run -d -p 5000:5000 --name flaskcc flask-auto-heal
```

### 2. Configure the Monitor
The monitoring script is configured to watch `http://127.0.0.1:5000`. Ensure your local environment has the necessary Python packages:
```bash
pip install -r requirements.txt
```

### 3. Initialize the Self-Healing Loop
Run the main script to start the health checks:
```bash
python "Main Script.py"
```

---

## 📉 Self-Healing Logic

The monitoring script performs the following check:

| Status Code | Action | Output |
| :--- | :--- | :--- |
| `200 OK` | None | "IS UP" |
| `Non-200 / Timeout` | Run `logs_checking.yaml` | "NOT UP" |
| `Connection Error` | Run `logs_checking.yaml` | "Service Error" |

When a failure is detected, Ansible performs a **Hard Restart** on the `flaskcc` container and saves the stdout logs to `logs_flaskcc.txt`.

---

## 🛠️ Requirements
* **Docker Engine:** For container orchestration.
* **Ansible:** Must have the `community.docker` collection installed (`ansible-galaxy collection install community.docker`).
* **Python 3.x:** To run the monitor and Flask server.

---

## 📝 Troubleshooting
The system saves real-time container logs during every restart cycle. You can inspect `logs_flaskcc.txt` to see the Flask debug output and identify why the service crashed.
```bash
cat logs_flaskcc.txt
```
