from django.db import models
from django.core.exceptions import ValidationError
import os


def get_first_100_characters(text):
    if text:  # Check if the string is not None or empty
        return text[:100]  # If the string is not None, return the first 100 characters
    return ''  # If the string is None, return an empty string


import os

def get_upload_to(instance, filename):
    # Extract the file extension
    ext = os.path.splitext(filename)[1].lower()

    # Document files
    if ext in ['.pdf', '.doc', '.docx', '.txt', '.md', '.rtf']:
        return os.path.join('uploads/documents/', filename)

    # Image files
    elif ext in ['.jpg', '.jpeg', '.png', '.webp']:
        return os.path.join('uploads/images/', filename)

    # Video files
    elif ext in ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.webm']:
        return os.path.join('uploads/videos/', filename)

    # Audio files
    elif ext in ['.mp3', '.wav', '.ogg', '.aac', '.flac', '.m4a']:
        return os.path.join('uploads/audio/', filename)

    # Programming languages files
    elif ext in ['.py', '.java', '.c', '.cpp', '.h', '.hpp', '.cs', '.swift', '.kt', '.kts', '.rs',
                 '.php', '.rb', '.go', '.ts', '.js', '.jsx', '.tsx', '.dart', '.r', '.lua', '.sh',
                 '.pl', '.perl', '.tcl', '.ml', '.clj', '.lisp', '.ex', '.exs', '.scala']:
        return os.path.join('uploads/code/', filename)

    # Markup & Data files
    elif ext in ['.html', '.htm', '.xml', '.json', '.yaml', '.yml', '.csv']:
        return os.path.join('uploads/data/', filename)

    # Game development files
    elif ext in ['.unity', '.prefab', '.asset', '.mat', '.fbx', '.blend', '.gltf', '.glb']:
        return os.path.join('uploads/game_models/', filename)
    elif ext in ['.gd', '.tres', '.tscn', '.godot']:
        return os.path.join('uploads/godot/', filename)
    elif ext in ['.uproject', '.uasset', '.umap']:
        return os.path.join('uploads/unreal/', filename)
    elif ext in ['.c3p', '.gms', '.yy', '.yyz']:
        return os.path.join('uploads/gamemaker/', filename)

    # 3D Models (Blender & 3D Studio Max)
    elif ext in ['.blend', '.max']:  # Blender and 3DS Max model files
        return os.path.join('uploads/3d_models/', filename)

    # Configuration & Build files
    elif ext in ['.env', '.ini', '.cfg', '.conf', '.toml', '.bat', '.cmd', '.ps1']:
        return os.path.join('uploads/config/', filename)

    # Script & Automation files
    elif ext in ['.pyc', '.ipynb', '.bat', '.cmd', '.ps1', '.vbs', '.wsf']:
        return os.path.join('uploads/scripts/', filename)

    # Archives & Compressed Files
    elif ext in ['.zip', '.tar', '.gz', '.7z', '.rar']:
        return os.path.join('uploads/archives/', filename)

    # Database & Backend files
    elif ext in ['.sql', '.db', '.sqlite', '.psql', '.mongo']:
        return os.path.join('uploads/databases/', filename)

    # Log and backup files
    elif ext in ['.log', '.bak']:
        return os.path.join('uploads/logs/', filename)

    # If file type is not recognized, store in 'others' folder
    else:
        return os.path.join('uploads/others/', filename)


def validate_file_extension(value):
    allowed_extensions = [
        # ✅ Image formats
        '.jpg', '.jpeg', '.png', '.webp',

        # ✅ Document formats
        '.pdf', '.doc', '.docx', '.txt', '.md', '.rtf',

        # ✅ Video formats
        '.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.webm',

        # ✅ Audio formats
        '.mp3', '.wav', '.ogg', '.aac', '.flac', '.m4a',

        # ✅ Programming Languages
        '.py', '.java', '.c', '.cpp', '.h', '.hpp', '.cs', '.swift', '.kt', '.kts', '.rs',
        '.php', '.rb', '.go', '.ts', '.js', '.jsx', '.tsx', '.dart', '.r', '.lua', '.sh',
        '.pl', '.perl', '.tcl', '.ml', '.clj', '.lisp', '.ex', '.exs', '.scala',

        # ✅ Markup & Data formats
        '.html', '.htm', '.xml', '.json', '.yaml', '.yml', '.csv',

        # ✅ Game Development (Unity, Unreal, Godot, etc.)
        '.unity', '.prefab', '.asset', '.mat', '.fbx', '.blend', '.gltf', '.glb',
        '.gd', '.tres', '.tscn', '.godot',
        '.uproject', '.uasset', '.umap',
        '.c3p', '.gms', '.yy', '.yyz',

        # ✅ 3D Models (Blender & 3DS Max)
        '.blend', '.max',

        # ✅ Configuration & Build Files
        '.env', '.ini', '.cfg', '.conf', '.toml', '.bat', '.cmd', '.ps1',

        # ✅ Script & Automation
        '.pyc', '.ipynb', '.bat', '.cmd', '.ps1', '.vbs', '.wsf',

        # ✅ Archives & Compressed Files
        '.zip', '.tar', '.gz', '.7z', '.rar',

        # ✅ Database & Backend Files
        '.sql', '.db', '.sqlite', '.psql', '.mongo',

        # ✅ Log and backup files
        '.log', '.bak'
    ]

    # Extract the file extension
    ext = os.path.splitext(value.name)[1].lower()  # Get the file extension from its name
    if ext not in allowed_extensions:
        raise ValidationError(
            f"This file is not allowed. Only files with the following extensions are allowed: {', '.join(allowed_extensions)}.")


class Blog(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255, default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pk} - {self.name}"


def validate_file_size(value):
    limit = 200 * 1024 * 1024  # 200 MB
    if value.size > limit:
        raise ValidationError('File size should not exceed 200 MB.')


class Content(models.Model):
    content = models.TextField(null=True, blank=True, default=None)
    blog = models.ForeignKey(Blog, related_name='blog_contents', on_delete=models.CASCADE,null=True, blank=True, default=None)
    sort_index = models.IntegerField(default=0, null=True, blank=True)
    file = models.FileField(upload_to=get_upload_to, validators=[validate_file_size, validate_file_extension],
                            null=True, blank=True, default=None)
    file_content = models.TextField(blank=True, null=True)


    def __str__(self):
        return get_first_100_characters(self.content)


class View(models.Model):
    view = models.ForeignKey(Blog, related_name='blog_views', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return get_first_100_characters(self.content)
