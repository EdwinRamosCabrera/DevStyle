from .models import User
from django.views.generic.edit import CreateView

class UserCreateView(CreateView):
    model = User
    fields = ['username', 'email', 'password1', 'password2']
    success_url = '/account/login/'