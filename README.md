
# **Healthcare Backend API**  
A Django REST Framework-based backend for managing patients, doctors, and assignments in a healthcare system.  

## **Live API URL**  
📌 **Base URL:** `<your-render-app-url>`  

## **Tech Stack**  
- Django  
- Django REST Framework (DRF)  
- PostgreSQL  
- JWT Authentication (SimpleJWT)  
- Swagger & ReDoc for API documentation  
- Whitenoise for static file handling  
- Deployed on **Render**  

---

## **Setup Instructions**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/Mansiv75/HealthcareBackend/
cd HealthcareBackend
```

### **2. Create a Virtual Environment**  
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4. Configure Environment Variables**  
Create a `.env` file in the root directory and add:  
```
DJANGO_SECRET_KEY=<your-secret-key>
DATABASE_URL=<your-postgres-url>
```

### **5. Run Migrations**  
```bash
python manage.py makemigrations
python manage.py migrate
```

### **6. Create a Superuser** (For Admin Access)  
```bash
python manage.py createsuperuser
```

### **7. Run the Development Server**  
```bash
python manage.py runserver
```

---

## **API Documentation**  

### **Swagger UI**
📌 **URL:** `<>/swagger/`  

### **ReDoc**
📌 **URL:** `<>/redoc/`  

---

## **Authentication Routes**  

### **Register a User**  
**POST** `/api/auth/register/`  
_Request:_  
```json
{
    "username": "John Doe",
    "email": "johndoe@example.com",
    "password": "securepassword"
}
```
_Response:_  
```json
{
    "message": "User registered successfully"
}
```
![image](https://github.com/user-attachments/assets/132cf948-9604-4e5e-936b-5ec0d13ff3a2)



### **Login User**  
**POST** `/api/auth/login/`  
_Request:_  
```json
{
    "username": "ricksorkin",
    "password": "securepassword"
}
```
_Response:_  
```json
{
    "access": "<jwt-token>",
    "refresh": "<refresh-token>"
}
```
![image](https://github.com/user-attachments/assets/39b7e49a-1e38-4bfe-8c84-4e7184c8252f)


---

## **Patient Routes**  

### **Create a Patient**  
**POST** `/api/patients/`  
_Request:_  
```json
{
    "name": "Alice",
    "age": 29,
    "disease": "Diabetes"
}
```
![image](https://github.com/user-attachments/assets/881391c1-3dd8-4bc0-8910-bd3658dcf3a2)


### **Get All Patients**  
**GET** `/api/patients/`  
![image](https://github.com/user-attachments/assets/34842a85-6b13-4ed9-9322-ea9bdc043107)


### **Get a Specific Patient**  
**GET** `/api/patients/{id}/`  
![image](https://github.com/user-attachments/assets/2156d991-e4aa-4e4e-996b-72aa24fe2e55)


### **Update a Patient**  
**PUT** `/api/patients/{id}/`  
![image](https://github.com/user-attachments/assets/202ea776-7daa-489c-97c8-785ba2c0b7c2)



### **Delete a Patient**  
**DELETE** `/api/patients/{id}/`  


---

## **Doctor Routes**  

### **Create a Doctor**  
**POST** `/api/doctors/`  
_Request:_  
```json
{
    "name": "Dr. Smith",
    "specialization": "Cardiology",
    "experience": 10
}
```
![image](https://github.com/user-attachments/assets/51865bad-60a6-4e30-950a-05375fb274ea)


### **Get All Doctors**  
**GET** `/api/doctors/`  
![image](https://github.com/user-attachments/assets/f20fe7f3-8695-41f9-b14b-cc5d9cc48dbb)


### **Get a Specific Doctor**  
**GET** `/api/doctors/{id}/`  
![image](https://github.com/user-attachments/assets/6e47f469-bff3-4114-ac9b-23726f9ec6e5)


### **Update a Doctor**  
**PUT** `/api/doctors/{id}/`  
![image](https://github.com/user-attachments/assets/36a1f85f-08d7-494e-a9e6-3f79e6f461dc)


### **Delete a Doctor**  
**DELETE** `/api/doctors/{id}/`  

---

## **Patient-Doctor Mapping Routes**  

### **Assign a Doctor to a Patient**  
**POST** `/api/mappings/`  
_Request:_  
```json
{
    "patient": 1,
    "doctor": 3
}
```
![image](https://github.com/user-attachments/assets/59d83d2c-2ef8-4466-b4de-d34091c186a1)


### **Get All Assignments**  
**GET** `/api/mappings/`  
![image](https://github.com/user-attachments/assets/1045aa7a-8237-42e2-bb49-e5854c4fee8a)


### **Get Assigned Doctors for a Patient**  
**GET** `/api/mappings/{patient_id}/`  
![image](https://github.com/user-attachments/assets/aac7668e-a860-4940-b888-3e0e91eaf71f)


### **Remove a Doctor from a Patient**  
**DELETE** `/api/mappings/delete/{id}/`  
![image](https://github.com/user-attachments/assets/430b54c1-24a8-4f1d-be5f-3ec42f5a3c65)


---

## **Admin Panel**  
📌 **URL:** `<>/admin/`  
- Log in with the superuser account created earlier.  
- Manage **Users, Patients, Doctors, and Mappings**.  
Got it! Here's a clean **README.md** file with space for images after each route. 🚀
![image](https://github.com/user-attachments/assets/6538fbe6-e1b5-489c-94b9-05fe0a3c0a55)



---

## **Deployment on Render**  

### **1. Push Code to GitHub**  
```bash
git add .
git commit -m "Deploy to Render"
git push origin main
```

### **2. Deploy on Render**  
1. Go to [Render](https://dashboard.render.com/)  
2. Create a **New Web Service**  
3. Connect GitHub repo  
4. Set Environment Variables (`DJANGO_SECRET_KEY`, `DATABASE_URL`)  
5. Set Build Command:  
   ```bash
   pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
   ```
6. Set Start Command:  
   ```bash
   gunicorn core.wsgi --log-file -
   ```
7. Deploy 🚀  

---

## **Contributing**  
Feel free to contribute! Open an issue or a PR.  

---

## **License**  
📜 **MIT License**  

---
