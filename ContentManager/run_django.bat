@echo off
echo Changing directory to Django project...

:: تغییر مسیر به پوشه پروژه (مسیر را مطابق با پروژه خود تنظیم کنید)
cd /d "E:\projects\git_projects\ContentManagerDjango"

echo Activating virtual environment...

:: فعال کردن محیط مجازی (اگر از محیط مجازی استفاده می‌کنید)
call venv\Scripts\activate

echo Starting Django server...

:: اجرای سرور Django
cd ContentManager
python ./manage.py runserver

pause
