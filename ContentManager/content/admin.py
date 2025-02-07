import urllib
from django.contrib import admin
from .models import Blog, Content, get_first_100_characters
from django.utils.html import format_html
from django.urls import reverse


class ContentAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('id','blog', 'sort_index', 'file', 'content_preview')
    search_fields = ['blog__name', 'content']  # Searchable fields
    list_filter = ['blog']  # Filter by blog
    readonly_fields = ('file_content',)  # کاربر نمی‌تواند مقدار را تغییر دهد


    def content_preview(self, obj):
        """Returns the first 100 characters of the content for preview in the admin panel."""
        return get_first_100_characters(obj.content)

    content_preview.short_description = 'Content Preview'  # Display name in admin panel

    def get_queryset(self, request):
        """Filters the queryset to show only contents related to a specific blog if provided in the request."""
        queryset = super().get_queryset(request)
        if 'blog__id' in request.GET:
            blog_id = request.GET['blog__id']
            queryset = queryset.filter(blog__id=blog_id)
        return queryset

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        Filters the blog selection in the content form to show only contents related to the selected blog.
        This ensures that when adding/editing content from a specific blog page, only that blog is preselected.
        """
        blog_id = None

        # Check if blog_id is directly provided in the URL parameters
        if 'blog__id' in request.GET:
            blog_id = request.GET.get('blog__id')

        # If not found, check within '_changelist_filters' for a blog filter
        elif '_changelist_filters' in request.GET:
            filters = request.GET.get('_changelist_filters', '')
            parsed_filters = urllib.parse.parse_qs(filters)
            blog_ids = parsed_filters.get('blog__id', [])
            if blog_ids:
                blog_id = blog_ids[0]

        # If a specific blog is selected, limit the queryset to that blog
        if db_field.name == "blog" and blog_id:
            kwargs['queryset'] = Blog.objects.filter(id=blog_id)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class BlogAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('id','name', 'desc', 'blog_contents','view_link', 'created_at', 'updated_at')
    search_fields = ['name', 'desc']  # Allow search by name and description
    readonly_fields = ('created_at','updated_at',)  # کاربر نمی‌تواند مقدار را تغییر دهد

    def blog_contents(self, obj):
        """
        Creates a clickable link to view all contents related to the blog in the admin panel.
        This helps in quickly navigating to the contents of a specific blog.
        """
        url = reverse("admin:content_content_changelist") + f"?blog__id={obj.id}"
        return format_html('<a href="{}">blog_contents </a>', url)


    def view_link(self, obj):
        """Generate a clickable link for each blog object"""
        return format_html('<a href="http://127.0.0.1:8000/blog/{}/" target="_blank">View Blog</a>', obj.id)

    view_link.short_description = "Blog Link"  # عنوان ستون در لیست نمایش ادمین

    blog_contents.short_description = 'blog_contents Link'  # Display name in admin panel


# Register the models to appear in the Django admin
admin.site.register(Blog, BlogAdmin)
admin.site.register(Content, ContentAdmin)
