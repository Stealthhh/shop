from django.contrib.auth.forms import UserCreationForm

from .models import MyUser
#import pdb
#pdb.set_trace()


class SignUpForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('username', 'password1', 'password2')