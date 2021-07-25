from django.urls import path, include
from .views import SignUpView



urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('accounts', include('django.contrib.auth.urls')),
    path('accounts', include('accounts.urls')),
    path('', include('pages.urls')),
]

#<li><a class="dropdown-item" href="{% url 'article_new' %}">Create 

#from django.contrib.auth.mixins import LoginRequiredMixin
#python3 -c "import secrets; print(secrets.token_urlsafe())"
#145:28
#'whitenoise.middleware.WhiteNoiseMiddleware',
#heroku run python3 manage.py createsuperuser


