# Backend Fundamentals

# What is Backend Development?
# The backend is the “behind-the-scenes” part of a software application — it handles data processing, business logic, and database operations.


#  the backend interacts with:
# Databases (storing/retrieving information)
# APIs (connecting with other services)
# Business logic (rules, calculations, workflows)

# Client–Server Architecture
# Backend development follows the Client–Server model
# Client: Sends a request
# Server: Processes the request, talks to a database, and returns a response.

# HTTP Request & Response Cycle
# HTTP = Hypertext Transfer Protocol, the language for communication between client & server.

# Cycle:
# Client sends HTTP Request → Includes:
# Method (GET, POST…)
# URL 
# Headers
# Body (optional)

# Server processes request
# Server sends HTTP Response → Includes:
# Status code 
# Headers
# Body 

# HTTP Methods
# These are verbs that describe the action:
# | Method     | Purpose                   | Example                  |
# | ---------- | ------------------------- | ------------------------ |
# | **GET**    | Read data                 | Get all users            |
# | **POST**   | Create new data           | Add a new user           |
# | **PUT**    | Update entire resource    | Update full user profile |
# | **PATCH**  | Update part of a resource | Change only username     |
# | **DELETE** | Remove data               | Delete a user            |


# REST API Principles
# REST = Representational State Transfer
# It’s a set of rules for designing APIs.

# Key concepts:
# Resources = Objects/data in your system (e.g., users, products)
# Endpoints = URLs where resources are accessed (e.g., /api/users)
# Stateless = Each request is independent; server doesn’t remember past requests.

# HTTP Status Codes
# These tell the client what happened:
# | Code | Category      | Meaning                      |
# | ---- | ------------- | ---------------------------- |
# | 1xx  | Informational | Request received, continuing |
# | 2xx  | Success       | Action successful            |
# | 3xx  | Redirection   | Need to go to another URL    |
# | 4xx  | Client Error  | Problem with request         |
# | 5xx  | Server Error  | Problem on server side       |

# Common examples:
# 200 OK – Success
# 201 Created – Resource created
# 400 Bad Request – Invalid input
# 404 Not Found – Resource doesn’t exist
# 500 Internal Server Error – Something broke on the server

