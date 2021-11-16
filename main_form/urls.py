from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainFormView.as_view(), name='main_form'),
    path('confirm/<int:pk>', views.ConfirmView.as_view(), name='confirm'),
    path('get_amount', views.get_amount, name='get_amount'),
]