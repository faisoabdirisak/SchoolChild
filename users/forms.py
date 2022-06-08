from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
         model=User
         fields=['first_name', 'email', 'username', 'password1','password2']
         labels={
             'username':'username'
         }


    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':''})      


class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields=['name','child_name', 'child_age','username',
         'location', 'email', 'profile_image', 'child_image']

    def __init__(self, *args, **kwargs):
            super(ProfileForm, self).__init__(*args, **kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class':''})          



