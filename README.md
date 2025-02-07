ContentManagerDjango
ContentManagerDjango is a Django-based content management system designed as a simple yet efficient blog platform. This project enables users to create and manage blog posts while supporting various content formats, including programming files, images, audio, and video.

Project Structure:
Admin Panel: Built using Django's admin interface, this section serves as the backend for managing blog entries and uploading associated files.
Frontend: The project provides two main pages for content display:
Blog Listing Page: A page where all published blog posts are displayed.
Blog Detail Page: A dedicated page for viewing the full content of each blog post, including embedded files and media.
This project leverages Django’s powerful features to ensure seamless content management and an intuitive user experience.


Installation & Setup
No additional packages are required for this project. The only prerequisite is having Django installed. Follow the steps below to set up and run the project:

Django Requires Python
```bash
python --version
```

If Python is installed, you will get a result with the version number, like this
```bash
Python 3.9.2
```

To install Django, you must use a package manager like PIP
To check if your system has PIP installed, run this command in the command prompt:
```bash
pip --version
```
Install packages in a virtual environment using pip and venv
```bash
pip install virtualenv
```
Type the following in the command prompt, remember to navigate to where you want to create your project
```bash
py -m venv venv
```

Then you have to activate the environment, by typing this command:

```bash
venv\Scripts\activate.bat

```

Install Django (if not already installed):

```bash
py -m pip install Django
```

Check Django Version
```bash
django-admin --version
```




**Clone the repository:**

```bash
git clone [https://github.com/hameddalvand67/ContentManagerDjango.git]
```
Navigate to the ContentManagerDjango folder 
```
cd ContentManagerDjango
```
Migrate
Now when we have described a Model in the models.py file, we must run a command to actually create the table in the database.
Run database migrations:
```bash
py manage.py makemigrations
```

Run database migrate:

```bash
python manage.py migrate
```
Create a superuser (for accessing the admin panel):

```bash

python manage.py createsuperuser

```
Follow the prompts to set up a username and password.

Start the Django development server:

```bash
python manage.py runserver
```
Access the application:
```
Admin Panel: http://127.0.0.1:8000/admin/
Blog Listing: http://127.0.0.1:8000/
```
Now the project is fully set up and ready to use! 🚀


