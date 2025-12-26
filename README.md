# Google Gemini AI based simple gRPC app
# API backend stack development using Python
# POSTMAN collection available
# Automation development using Python for positive and negative scenarios

<img width="1280" height="720" alt="Slide1" src="https://github.com/user-attachments/assets/3f7a2a89-a86b-4a61-9892-89466fa61b6c" />
.

<img width="1280" height="720" alt="Slide2" src="https://github.com/user-attachments/assets/6670c126-32d1-44fd-aa1e-d2818b31cdce" />

Backend development prompt https://gemini.google.com/share/181a3c873a30

Developed the backend stack from scratch.
Simple conversational discussion with AI (Google Gemini)

# Case study: Ride booking system (e.g. Uber)
There are 4 microservices - entrypoint1 (gRPC based), identity1, payment1, routing1

Client basically talks to entrypoint1 microservice and provide all data

entrypoint1 services talks to all 3 microservice (in parallel) and validates respective data

identity1 microservice verify user name give by entrypoint1 service contains only alphabetical letters

payment1 microservice verify payment amount give by entrypoint1 service is non zero

routing1 microservice verify source and destination name give by entrypoint1 service is non same

if response from all 3 microservice is success, then entrypoint1 responds with success

if any one internal microservice response is fail, then entrypoint1 responds with failure

there is simple logging implements

# Docker steps
docker-compose up --build

docker compose down

# Manual testing using POSTMAN
need to import service.proto file - https://github.com/imademethink/grpc_demo/blob/main/qa/service.proto

postman collection link https://web.postman.co/workspace/My-Workspace~0c40b27d-d372-48d1-8840-a7cd2908b70c/collection/694d777ca01b6da78de879e8?action=share&source=copy-link&creator=3085350

# Automation
Google Gemini AI designed a simple automation based on Python


# Article on medium.com
https://medium.com/@shrikant.swami/ai-assisted-prompt-based-grpc-basic-app-development-from-scratch-52fcb99a64d0


# Cheers
