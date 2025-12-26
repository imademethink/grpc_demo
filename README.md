# Google Gemini AI based simple gRPC app
# >> API backend stack development using Python
# >> POSTMAN collection available
# >> Automation development using Python for positive and negative scenarios

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

# Manual testing using POSTMAN
need to use service.proto

# Automation
Google Gemini AI designed a simple automation based on Python

# Cheers

