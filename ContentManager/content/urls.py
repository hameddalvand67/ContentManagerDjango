from django.urls import path
from .views import blogs,contents

urlpatterns = [
    path('', blogs),  # Default route (no search text)
    path('<str:searchText>/', blogs),  # Route with search text
    path('blog/<int:blog_id>/', contents),  # Route with search text


]
