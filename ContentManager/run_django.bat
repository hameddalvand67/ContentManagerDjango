@echo off
echo Changing directory to Django project...

:: Change directory to the project folder (update the path according to your project)
cd /d "E:\projects\git_projects\ContentManagerDjango"

echo Activating virtual environment...

:: Activate the virtual environment (if using a virtual environment)
call venv\Scripts\activate

echo Starting Django server...

:: Run the Django server
cd ContentManager
python ./manage.py runserver

pause
