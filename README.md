# flask-registration-system

# 🚀 flask-registration-system

A Python Flask project implementing user registration, login, and two-factor authentication (2FA) with QR code generation.

---

## 📖 Introduction

**flask-registration-system** is a web application built with Python and Flask that enables users to register, authenticate, and secure their accounts using two-factor authentication (2FA). With an intuitive interface, it provides enhanced security through QR code-based 2FA, making authentication robust for modern web applications.

---

## ✨ Features

- **User Registration**: Sign up new users with profile information and photo upload.
- **Login System**: Secure user login with session management.
- **Two-Factor Authentication (2FA)**: Protect accounts with QR code-based 2FA.
- **Dashboard**: Personalized dashboard displaying user details.
- **Password Security**: Passwords are securely hashed.
- **Responsive UI**: Modern, responsive design using custom CSS.
- **SQLite Database**: User data managed with SQLAlchemy and SQLite.
- **MVC Structure**: Organized codebase with controllers, models, and templates.

---

## ⚙️ Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/flask-registration-system.git
    cd flask-registration-system
    ```

2. **Set Up Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Initialize the Database**
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

5. **Run the Application**
    ```bash
    flask run
    ```
    The app will be available at `http://localhost:5000`.

---

## 📝 Usage

1. **Register**
    - Visit the home page and click on "Register".
    - Fill out the registration form and upload a profile image.

2. **Login**
    - Enter your credentials.
    - If enabled, scan the QR code with your authenticator app for 2FA.

3. **Dashboard**
    - After login, access your personalized dashboard to view your profile.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to your branch: `git push origin feature/your-feature`
5. Open a Pull Request.

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> Made with ❤️ by the flask-registration-system community.

---

**Feel free to open issues and suggestions!**

## License
This project is licensed under the **MIT** License.

---
🔗 GitHub Repo: https://github.com/Imranch4/flask-registration-system
