from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('guests/', views.GuestListView.as_view(), name='guests'),
    path('location/', views.location_picker, name='location'),
    path('theme/', views.ThemePickerView.as_view(), name='theme'),
    path('shoppingList/', views.ResourceCreateView.as_view(), name='list-creation'),
]
