# 📚 Inked Impressions – A Book Review Hub

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-green)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-brightgreen)
![HTML](https://img.shields.io/badge/HTML-Bootstrap-orange)

---

## 🚀 Live Demo

🌐 [https://boobathy13.github.io/Sparta-Back-End-Project/](https://boobathy13.github.io/Inked-Impressions/)

---

## 📌 Overview

**Inked Impressions** is a lightweight web application that allows readers to explore, rate, and review books in a simple and visually appealing way. Built using Flask and MongoDB, it enables users to share opinions and feedback, while displaying book collections, user comments, and star ratings in a clean interface.

---

## ✨ Features

* ✅ **Add & View Reviews** – Submit feedback on books
* ✅ **Star Ratings** – Rate books from 1 to 5 stars
* ✅ **Dynamic Display** – Show submitted reviews in a table format
* ✅ **Book Gallery** – Pre-filled collection of popular books
* ✅ **Responsive UI** – Works well on desktop & mobile (Bootstrap)

---

## 🧰 Tech Stack

* **Frontend:** HTML, CSS, JavaScript, Bootstrap
* **Backend:** Flask (Python)
* **Database:** MongoDB (hosted on MongoDB Atlas)
* **Libraries:** jQuery, WebClient (AJAX for API calls)

---

## 🔧 Prerequisites

* ✅ Python 3.9+
* ✅ `pip` package manager
* ✅ Internet connection (for MongoDB Atlas & CDN assets)

---

## 🛠️ Installation & Running Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Inked-Impressions.git
cd Inked-Impressions
```

### 2️⃣ Set Up Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows
```

### 3️⃣ Install Required Packages

```bash
pip install flask pymongo
```

### 4️⃣ Start the Flask Server

```bash
python app.py
```

Visit: [http://localhost:5000](http://localhost:5000)

---

## 🌐 API Endpoints

### 🔸 Submit Review (POST)

**Endpoint:** `/order`
**Form Data Fields:**

* `name_give` – Reviewer's name
* `count_give` – Book name
* `address_give` – Star rating
* `phone_give` – Comments

**Response:**

```json
{ "result": "success" }
```

---

### 🔸 View Reviews (GET)

**Endpoint:** `/order`
**Response:**

```json
{
  "result": "success",
  "orders": [
    {
      "name": "Alice",
      "count": "Atomic Habits",
      "address": "⭐⭐⭐⭐⭐",
      "phone": "Great book on habit building!"
    },
    ...
  ]
}
```

---

## 🖼️ UI Preview

### 🏷️ Book Collection

Preloaded book cards with author info, summaries, and visual star ratings.

### 📝 Feedback Section

Simple form to submit a review:

* Name
* Book Name
* Star Rating (1–5)
* Comments

### 📋 Latest Comments Table

Dynamically displays the latest feedback submitted by users.

---

## 🗂️ Project Structure

```
Inked-Impressions/
├── templates/
│   └── index.html           # Frontend UI
├── app.py                   # Flask backend
├── static/                  # (optional for future static files)
├── README.md
├── .gitignore
├── requirements.txt         # (optional for packaging dependencies)
```

---

## 🚀 Future Enhancements

* 🔐 Add form validation & CAPTCHA
* 🧾 Store timestamps for reviews
* 🌈 Add book categories and filters
* 📊 Admin dashboard for analytics
* 📥 Allow image uploads or book suggestions

---

## 📝 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Boobathy R**
📧 [Mail ID](mailto:hungrylearner2002@gmail.com)



