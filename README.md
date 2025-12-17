

# 🚀 Python API Automation Framework

A **Hybrid Custom API Automation Framework** 
built using **Python** and **PyTest**, designed for scalable, maintainable, 
and efficient API testing with industry-standard best practices.

---

## 📌 Key Highlights

✅ Clean and scalable folder structure  
✅ Supports **CRUD API automation**  
✅ Parallel execution for faster test runs  
✅ Rich reporting using **Allure** and **PyTest HTML**  
✅ Data-driven testing support  
✅ Schema validation for advanced API testing  

---

## 🖼️ Framework Overview

![Framework Screenshot](https://github.com/user-attachments/assets/3c7d5fe5-207a-42e7-84fe-f4d53354d987)

---

## 🛠️ Tech Stack

- **Python 3.14**
- **Requests** – HTTP request handling
- **PyTest** – Test execution & assertions
- **Reporting**
  - Allure Report
  - PyTest HTML
- **Test Data Management**
  - CSV
  - Excel
  - JSON
  - Faker
- **Advanced API Testing**
  - JSON Schema Validation (`jsonschema`)
- **Parallel Execution**
  - PyTest XDist (`xdist`)

---

## 📂 Project Structure (High Level)

```

Python_API_Automation/
│
├── tests/
│   ├── crud/
│   │   ├── test_create_booking.py
│   │   ├── test_update_booking.py
│   │   └── test_delete_booking.py
│
├── test_data/
│   ├── testdata.json
│   ├── testdata.csv
│   └── testdata.xlsx
│
├── utils/
│   ├── api_client.py
│   ├── config.py
│   └── helpers.py
│
├── schemas/
│   └── booking_schema.json
│
├── reports/
│
├── requirements.txt
└── README.md

````

---

## ⚙️ Installation

Make sure **Python 3.14+** is installed.

### Install Required Packages
```bash
pip install requests pytest pytest-html faker allure-pytest jsonschema
````

---

## ⚡ Parallel Execution Setup

Install PyTest XDist:

```bash
pip install pytest-xdist
```

Run tests in parallel:

```bash
pytest -n auto
```

---

## 📊 Running Tests with Allure Report

### Execute a Test Case

```bash
pytest tests/tests/crud/test_create_booking.py --alluredir=allure_result -s
```

### Generate & View Allure Report

```bash
allure serve allure_result
```

---

## 🧪 Reporting Options

* ✅ **Allure Reports** (Interactive & detailed)
* ✅ **PyTest HTML Reports** (Lightweight & shareable)

---

## 👨‍💻 Author

**Prajwal Upadhye**
QA Engineer | API Automation | Manual & Automation Testing


---



---



---

## 📄 License

This project is licensed under the **MIT License**.

---



