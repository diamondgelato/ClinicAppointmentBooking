CREATE TABLE patient (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    phone_no TEXT,
    email TEXT,
    birth_date TEXT NOT NULL, -- ISO8601 string
    gender TEXT NOT NULL,
    address TEXT
);

-- sort out the time ka thingy haaaaa
CREATE TABLE appointment (
    app_id INTEGER PRIMARY KEY AUTOINCREMENT,
    datetime TEXT NOT NULL, -- ISO8601 string
    purpose TEXT NOT NULL,
    status TEXT NOT NULL
);

CREATE TABLE report (
    report_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,  -- ISO8601 string
    name TEXT NOT NULL,
    file TEXT NOT NULL   -- path of file
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
    FOREIGN KEY (report_id) REFERENCES report(report_id),
    PRIMARY KEY (patient_id, doctor_id, report_id)
);

CREATE TABLE scheduled_app (
    patient_id INTEGER NOT NULL,
    doctor_id INTEGER NOT NULL,
    app_id INTEGER NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctor(doctor_id),
    FOREIGN KEY (app_id) REFERENCES appointment(app_id),
    PRIMARY KEY (patient_id, doctor_id, app_id)
);

INSERT INTO admin (username, password)
VALUES ('admin', 'admin');

INSERT INTO patient (first_name, last_name, username, password, phone_no, emaiL, birth_date, gender, address)
VALUES ('Mugdha', 'Kurkure', 'mugs1234', 'mugs1234', '9008210569', 'mugdha.k@gmail.com', '2001-09-18', 'FEMALE', 'Thane');

INSERT INTO doctor (first_name, last_name, qualification)
VALUES ('Mihir', 'Pandya', 'Obstretician');

INSERT INTO doctor (first_name, last_name, qualification)
VALUES ('Mugdha', 'Kurkure', 'Pediatrician');

INSERT INTO doctor (first_name, last_name, qualification)
VALUES ('Vani', 'Kamani', 'Nutritionist');

-- query for getting reports and patient ID using date
SELECT report.report_id, patient_report.patient_id, patient.first_name, patient.last_name, report.name, report.file
FROM report
JOIN patient_report ON report.report_id = patient_report.report_id
JOIN patient ON patient.patient_id = patient_report.patient_id
WHERE report.date = '2021-05-18';

-- query for getting reports and date using patient ID
SELECT report.report_id, report.date, patient.first_name, patient.last_name, report.name, report.file
FROM report
JOIN patient_report ON report.report_id = patient_report.report_id
JOIN patient ON patient.patient_id = patient_report.patient_id
WHERE patient_report.patient_id = '1';

-- query for getting patient, doctor and appointment details using date
SELECT appointment.app_id, doctor.first_name, doctor.last_name, patient.patient_id, patient.first_name, patient.last_name, appointment.datetime, appointment.purpose
FROM scheduled_app as sa
INNER JOIN appointment ON appointment.app_id = sa.app_id 
INNER JOIN patient ON patient.patient_id = sa.patient_id 
INNER JOIN doctor ON doctor.doctor_id = sa.doctor_id 
WHERE appointment.datetime LIKE '2021-05-04%';