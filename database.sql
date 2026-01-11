CREATE DATABASE HospitalDB;
GO

USE HospitalDB;
GO

CREATE TABLE Patients (
    patient_id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(100) NOT NULL,
    age INT NOT NULL CHECK (age > 0 AND age <= 120),
    weight INT NOT NULL CHECK (weight > 0 AND weight <= 300),
    condition NVARCHAR(255) NOT NULL,
    insurance_status NVARCHAR(10) NOT NULL
        CHECK (insurance_status IN ('yes', 'no')),
    insurance_type NVARCHAR(20) NULL,
    previous_doctor NVARCHAR(100) NULL,
    created_at DATETIME DEFAULT GETDATE()
);

INSERT INTO Patients
(name, age, weight, condition, insurance_status, insurance_type, previous_doctor)
VALUES
('Rohit Sharma', 32, 78, 'Fever and cough', 'yes', 'Government', 'Dr. Mehta'),
('Ananya Patel', 24, 55, 'Migraine', 'no', NULL, NULL),
('Kunal Verma', 41, 82, 'Diabetes Type 2', 'yes', 'Private', 'Dr. Singh');