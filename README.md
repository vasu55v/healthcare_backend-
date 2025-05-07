# 🏥 Healthcare Backend – Django + DRF + PostgreSQL

This backend API powers a healthcare app where users can register/login, manage patients and doctors, and assign doctors to patients.

---

## 🔧 Tech Stack

- Django 4.2
- Django REST Framework
- PostgreSQL
- JWT Authentication (`djangorestframework-simplejwt`)

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/vasu55v/healthcare_backend.git
cd healthcare_backend


1. Authentication APIs
POST /api/auth/register/ - Register a new user with name, email, and password.
POST /api/auth/login/ - Log in a user and return a JWT token.


2. Patient Management APIs
POST /api/patients/ - Add a new patient (Authenticated users only).
GET /api/patients/ - Retrieve all patients created by the authenticated user.
GET /api/patients/<id>/ - Get details of a specific patient.
PUT /api/patients/<id>/ - Update patient details.
DELETE /api/patients/<id>/ - Delete a patient record.


3. Doctor Management APIs
POST /api/doctors/ - Add a new doctor (Authenticated users only).
GET /api/doctors/ - Retrieve all doctors.
GET /api/doctors/<id>/ - Get details of a specific doctor.
PUT /api/doctors/<id>/ - Update doctor details.
DELETE /api/doctors/<id>/ - Delete a doctor record.


4. Patient-Doctor Mapping APIs
POST /api/mappings/ - Assign a doctor to a patient.
GET /api/mappings/ - Retrieve all patient-doctor mappings.
GET /api/mappings/<patient_id>/ - Get all doctors assigned to a specific patient.
DELETE /api/mappings/<id>/ - Remove a doctor from a patient.
