from django.urls import path
from . import views

urlpatterns = [
 path('', views.home, name='home'),
 path('about/', views.about, name='about'),
 path('finch/', views.finch_index , name='finch'),
 path('finch/<int:finch_id>/', views.finch_detail, name='finch_detail'),
 # new route used to show a form and create a cat
 path('finch/create/', views.FinchCreate.as_view(), name='finch_create'),
 path('cats/<int:pk>/update/', views.FinchUpdate.as_view(), name='finch_update'),
 path('cats/<int:pk>/delete/', views.FinchDelete.as_view(), name='finch_delete')
]

