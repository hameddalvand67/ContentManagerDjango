

**ContentManagerDjango**
---

ContentManagerDjango is a Django-based content management system designed as a simple yet efficient blog platform. This project enables users to create and manage blog posts while supporting various content formats, including programming files, images, audio, and video.
---
***Project Structure***

🔹 Admin Panel
Built using Django's admin interface, this section serves as the backend for managing blog entries and uploading associated files.

🔹 Frontend
The project provides two main pages for content display:

Blog Listing Page: A page where all published blog posts are displayed.
Blog Detail Page: A dedicated page for viewing the full content of each blog post, including embedded files and media.
This project leverages Django’s powerful features to ensure seamless content management and an intuitive user experience.
---
**Installation & Setup**

No additional packages are required for this project. The only prerequisite is having Django installed. Follow the steps below to set up and run the project.

1. Check Python Installation
Django requires Python. First, verify that Python is installed on your system:

```bash
python --version
```
If Python is installed, you should see output like this:

```bash

Python 3.9.2
```
2. Check and Install PIP
To install Django, you must use a package manager like PIP. Check if PIP is installed by running:

```bash
pip --version
```
3. Create and Activate a Virtual Environment
To manage dependencies efficiently, it is recommended to use a virtual environment (venv).

First, install virtualenv:

```bash
pip install virtualenv
```
Then, navigate to the desired directory and create a virtual environment:

```bash
py -m venv venv
```
Now, activate the virtual environment:

```bash
venv\Scripts\activate.bat
```
4. Install Django
If Django is not already installed, use the following command:

```bash
py -m pip install Django
```
To verify the installation, check the Django version:

```bash
django-admin --version
```
5. Clone the Repository from GitHub
To get the project files, clone the repository:

```bash
git clone https://github.com/hameddalvand67/ContentManagerDjango.git
```
Navigate to the project directory:

```bash
cd ContentManagerDjango
```
6. Run Database Migrations
After defining models in models.py, apply database migrations to create the necessary tables:

```bash
py manage.py makemigrations
```
Then execute:

```bash
python manage.py migrate
```
7. Create a Superuser (for Admin Panel Access)
Run the following command:

```bash

python manage.py createsuperuser
```
Follow the on-screen instructions to set up a username and password.

8. Start the Django Development Server
Run the following command to start the server:

```bash
python manage.py runserver
```
9. Access the Application
Once the server is running, you can access different sections using the following URLs:

🔹 Admin Panel:
```
http://127.0.0.1:8000/admin/
```

🔹 Blog Listing Page:
```
http://127.0.0.1:8000/
```

🎯 Final Setup Summary
✅ The project is now fully set up and ready to use! 🚀

📌 Common Issues & Troubleshooting
1️⃣ If you encounter a "ModuleNotFoundError" when running python manage.py runserver, ensure the virtual environment is activated.
✅ Solution: Before running the project, activate the virtual environment:

```bash
venv\Scripts\activate.bat
```
2️⃣ If Django is not installed, ensure that PIP is working correctly.
✅ Test PIP:

```bash
pip --version
```
3️⃣ Using a virtual environment helps prevent dependency issues and ensures a clean development setup.

❗ Need Any Modifications?
📌 If you have any questions or need adjustments, let me know! 😊🚀








