#1. Introduction to REST APIs
# - REST (Representational State Transfer) is an architectural style
# used for designing networked applications using stateless communication.
# - REST APIs allow different software systems to communicate over HTTP.

# - Key principles of REST include:
    # - Stateless: Each request must contain all information needed to process it
    # - Client-Server: Clear separation between client and server responsibilities
    # - Uniform Interface: Consistent way to interact with resources
    # - Cacheable: Responses should be cacheable when appropriate
    # - Layered System: Architecture can have multiple layers
    # - Code on Demand (optional): Server can send executable code to client

# REST vs RPC
# ----------------------------------------------------------------------
# |   REST                      |             RPC                      |
# -------------------------------------------------------------------- |
# | Resource-based              |     Action-based                     |
# | Uses HTTP methods naturally |     Methods encoded in URL or body   |
# | /books/123                  |      /getBook?id=123                 |
# | Stateless                   |     Can be stateful                  |
#-----------------------------------------------------------------------

# HTTP Methods in REST APIs
# - GET: Retrieve data(Read)
# - POST: Create new resource(Create)
# - PUT: Update existing resource(Update/Replace)
# - PATCH: Partially update existing resource(Update/Modify)
# - DELETE: Remove resources(Delete)

# Typical REST API Endpoints Structure
# GET    /books           # Get all books
# POST   /books           # Create a new book
# GET    /books/123       # Get book with ID 123
# PUT    /books/123       # Update book with ID 123
# DELETE /books/123       # Delete book with ID 123