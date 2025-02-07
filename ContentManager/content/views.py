from django.shortcuts import render

# Create your views here.


from django.http import JsonResponse
from .models import Blog

# def index(request, searchText=None):
#     blogs = None
#     all_blogs = Blog.objects.all()
#     if searchText:
#         blogs = Blog.objects.filter(name__icontains=searchText).order_by('-updated_at')  # Case-insensitive search
#     if not blogs:
#         blogs = all_blogs
#
#     context = {'blogs': blogs, 'all_blogs': all_blogs}
#
#     # blogs = Blog.objects.filter(name__contains=searchText)
#     return render(request, 'content/blogs.html',context )


from django.http import JsonResponse
from django.shortcuts import render
from .models import Blog, Content


def blogs(request, searchText=None):
    """
    If 'search' is provided via GET, return JSON response with matching blogs.
    Otherwise, render the template normally.
    """

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':  # Check if it's an AJAX request
        search = request.GET.get('search', '')
        if search:
            blogs = Blog.objects.filter(name__icontains=search).order_by('-updated_at')
        else:
            blogs = Blog.objects.all().order_by('-updated_at')  # Return all blogs
        data = list(blogs.values('id', 'name'))  # Convert queryset to list of dictionaries
        return JsonResponse(data, safe=False)  # Return JSON response
    else:
        blogs = None
        all_blogs = Blog.objects.all()
        if searchText:
            blogs = Blog.objects.filter(name__icontains=searchText).order_by('-updated_at')  # Case-insensitive search
        if not blogs:
            blogs = all_blogs

        context = {'blogs': blogs, 'all_blogs': all_blogs}

        # blogs = Blog.objects.filter(name__contains=searchText)
        return render(request, 'content/blogs.html', context)


def contents(request, blog_id):
    contents = Content.objects.filter(blog_id=blog_id).order_by('sort_index')

    # Loop through contents to get the file content
    for content in contents:
        if content.file:
            # Read the file content if it's a text file (like Python, Java, etc.)
            try:
                with content.file.open() as f:
                    content.file_content = f.read().decode('utf-8')  # Read as text
            except Exception as e:
                content.file_content = None  # Handle the case where the file can't be read
                print(f"Error reading file {content.file.name}: {e}")
    context = {'contents': contents, }
    return render(request, 'content/contents.html', context)
