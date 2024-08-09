from django.urls import path
from .views import project_list, add_project, product_details

urlpatterns = [
    path('', project_list, name='project-list'),
    path('add/', add_project, name='add-project'),
    path('details/<int:project_id>/', product_details, name='product-details'),
]