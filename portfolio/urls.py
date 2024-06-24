from django.urls import path
from .views import home, skills, contact_view, about

app_name = 'portfolio'
urlpatterns = [
    path('', home, name='home'),
    path('skills/', skills, name='skills'),
    path('contact/', contact_view, name='contact'),
    path('about/', about, name='about'),
]