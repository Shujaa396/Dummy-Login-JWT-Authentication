# 📊 Backend Reporting, Auth & Invoice History APIs

![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?logo=postgresql)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Deployment](https://img.shields.io/badge/Deployment-Oracle%20Free%20VM-orange)

---

## 🧑‍💻 Engineer
**Syed Shujaa Hussain**  
Backend Developer – Nexus Desktop POS  

---

## 📌 Task Overview
All assigned tasks were completed within one week. This phase focused on building reporting APIs, authentication, invoice history retrieval, and server-side logging using **FastAPI** with **PostgreSQL**, fully tested via **Postman** and verified against the frontend.

---

## ✅ Tasks Implemented

### 1️⃣ GET `/invoice/history`
- Supports **filters**: date range, status
- **Pagination** for POS UI
- Returns:
  - Invoice ID
  - Invoice date
  - Total amount
  - Sync status

---

### 2️⃣ POST `/reports/sales`
- Aggregates:
  - Daily / Weekly sales totals
  - Top-selling products
- Filters supported:
  - Category
  - Date range

---

### 3️⃣ POST `/auth/login`
- Validates user credentials against DB
- Generates secure session token
- Stores login timestamps
- Rejects invalid credentials with proper error response

---

### 4️⃣ Server-Side Logging
- Logs stored for:
  - Invoice sync operations
  - User login events
- Logs are **time-stamped**, **user-traceable**, and verifiable via DB or file

---

## 🛠️ Tech Stack
- **Backend:** FastAPI (Python 3.11)
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Auth:** Token-based authentication
- **Server:** Uvicorn
- **Testing:** Postman, Swagger UI
- **Frontend:** Next.js
- **Deployment:** Oracle Free VM

---

## 🧱 Database Models (Highlights)
- **User**
- **Profile**
- **Invoice**
- **Logs (Login & Sync Events)**

---

## 🔍 Key Review Points Covered
- Pagination implemented correctly
- Filtering by status and date
- Accurate aggregation totals
- Secure token generation
- Invalid login handling
- Invoice sync and login logs stored
- JSON responses structured properly
- Time and user traceability ensured

---

## 🧪 Testing & Verification
- Postman tests with query parameters
- Valid/invalid login tests
- Aggregation cross-checked with DB
- Dummy data tested for daily/weekly reports
- Swagger UI reviewed for schemas and examples
- Logs verified against timestamps and UI actions

---

## 📁 Project Structure (Relevant)
```
app/
├── routes/
│   ├── auth.py
│   ├── invoice.py
│   └── reports.py
├── models/
│   ├── user.py
│   ├── invoice.py
│   └── logs.py
├── schemas/
│   ├── auth.py
│   ├── invoice.py
│   └── reports.py
├── database/
│   └── connection.py
```

---

## 📸 Verification Checklist
- [ ] Postman test screenshots
- [ ] Swagger UI view
- [ ] DB records verification
- [ ] Aggregation accuracy check
- [ ] Login & invoice log entries
- [ ] GitHub commit history

---

## 🚀 Status
✔ All APIs live  
✔ Fully tested with frontend & Postman  
✔ Database verified  
✔ Ready for review & deployment  

---

> **Backend Reporting & Auth Module**  
> _Built with scalability, traceability, and performance in mind._

## 👤 Author
**Syed Shujaa Hussain**  
Backend Developer  

[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:web.shujaa10@gmail.com)  
[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Shujaa396)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/syed-shujaa-hussain-69113b289)

