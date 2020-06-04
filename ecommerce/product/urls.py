from django.urls import path, include
from . import views
app_name = 'product'
urlpatterns = [
    path('', views.index, name='home'),
    path('<slug:slug>/', views.product_details, name='product_details')

]
