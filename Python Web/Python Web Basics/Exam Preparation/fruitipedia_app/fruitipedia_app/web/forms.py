from django import forms

from fruitipedia_app.web.models import Profile, Fruit


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'Password'
                }
            )
        }

        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }

        help_texts = {
            'password': "*Password length requirements: 8 to 20 characters",
        }


class FruitCreateForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ('name', 'image_url', 'description', 'nutrition')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Name'
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Fruit Image URL'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Description'
                }
            ),
            'nutrition': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Nutrition'
                }
            ),
        }
        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }
        error_messages = {
            'fruit_name': {
                'unique': "This fruit name is already in use! Try a new one.",
            }
        }
