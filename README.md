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

Install Django (if not already installed):

bash
Copy
Edit
pip install django
Clone the repository:

bash
Copy
Edit
git clone [https://github.com/hameddalvand67/ContentManagerDjango.git]
cd ContentManagerDjango
Run database migrations:

bash
Copy
Edit
python manage.py migrate
Create a superuser (for accessing the admin panel):

bash
Copy
Edit
python manage.py createsuperuser
Follow the prompts to set up a username and password.

Start the Django development server:

bash
Copy
Edit
python manage.py runserver
Access the application:

Admin Panel: http://127.0.0.1:8000/admin/
Blog Listing: http://127.0.0.1:8000/
Now the project is fully set up and ready to use! 🚀


print("Hello, world!")

