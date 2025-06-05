E-commerce Sales Chatbot
Project Setup
Prerequisites
Docker and Docker Compose
Running the Project
Clone the repository
Run docker-compose up --build
Access frontend at http://localhost:3000
Access backend at http://localhost:5000
Initial Setup
The database will be automatically initialized with:

Test user: test@example.com / password
100+ mock products across electronics, books, clothing, and home categories
Features
User authentication (login/registration)
Session persistence
Natural language product search
Responsive chat interface
Product display with images
Session timestamps
Chat reset functionality
Technical Stack
Frontend: React.js, Tailwind CSS
Backend: Flask, SQLAlchemy, PostgreSQL
Authentication: JWT
Deployment: Docker
API Endpoints
POST /api/auth/register - User registration
POST /api/auth/login - User login
POST /api/chat - Chat interaction
POST /api/search - Product search
Challenges & Solutions
Natural Language Processing
Implemented a regex-based parser to extract filters from user queries
Session Persistence
Used localStorage to maintain chat history across page refreshes
Responsive Product Display
Created a grid layout that works on mobile, tablet, and desktop
Authentication Flow
Implemented JWT with token validation and refresh mechanism
Future Improvements
Add actual NLP with libraries like spaCy
Implement cart functionality
Add product filtering options
Implement actual purchase flow
