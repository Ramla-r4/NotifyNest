# 📂Task Management App

###  A platform for managing tasks and setting reminders, with a focus on user authentication and timely reminders.


## 🛠 Tech Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Django,
- **Database:**: PostgreSQL 
- **ask Queue**: Celery with Redis
- **Authentication:** Django's built-in Authentication
- **Email Services:** SMTP

  
## 🔥 Features 
✅ User Authentication (Signup, Login, Logout)                     
✅ Task Management (Users can add, view, and manage tasks)             
✅ Email Reminders (Automated email reminders for due tasks)             
✅ Real-Time Updates (Live updates with Celery and Redis)                 
✅ Secure & Scalable (Using Django’s built-in features for security)                  
         

## 🛠 Installation
1. Clone the repo:
   git clone https://github.com/Ramla-r4/NotifyNest.git  
   
## 🔥 Set up our environment:
  python -m venv myvenv  
  source venv/bin/activate 
## 📦Set up Celery and Redis:
   Install Redis on your machine 
   sudo apt install redis-server  # For Ubunt
   redis-server  # For Ubunt
Run Celery:
celery -A Project worker --pool=solo -l info


