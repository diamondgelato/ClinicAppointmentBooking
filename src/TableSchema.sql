CREATE TABLE patient (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    phone_no TEXT,
    email TEXT,
    birth_date DATE,
    gender TEXT NOT NULL,
    address TEXT
);

-- sort out the time ka thingy haaaaa
CREATE TABLE appointment (
    app_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE,
    purpose TEXT NOT NULL,
    status TEXT NOT NULL
);

CREATE TABLE report (
    report_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE,
    name TEXT NOT NULL,
    -- file BLOB,
);

CREATE TABLE doctor (
    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    qualification TEXT NOT NULL
);

CREATE TABLE admin (
    admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE patient_report (
    patient_id INTEGER NOT NULL,
    doctor_id INTEGER NOT NULL,
    report_id INTEGER NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctor(doctor_id),
    FOREIGN KEY (report_id) REFERENCES report(report_id)
);

CREATE TABLE scheduled_app (
patient_id INTEGER NOT NULL,
    doctor_id INTEGER NOT NULL,
    app_id INTEGER NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctor(doctor_id),
    FOREIGN KEY (app_id) REFERENCES appointment(app_id)
);