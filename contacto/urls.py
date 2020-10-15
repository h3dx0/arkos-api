from django.urls import path
from contacto import  views
app_name = 'contacto'

urlpatterns = [
    path('send/email/', views.send_email, name='send_email'),

]