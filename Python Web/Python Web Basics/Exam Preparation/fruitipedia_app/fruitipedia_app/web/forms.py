from django import forms

from fruitipedia_app.web.models import Profile, Fruit


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'password')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'Password',
                    'help_text': '*Password length requirements: 8 to 20 characters',
                }
            ),
        }
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url', 'age')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
        }


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['id']

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


class CreateFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ('name', 'image_url', 'description', 'nutrition')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Name',
                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Image URL',
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Description',
                }
            ),
            'nutrition': forms.TextInput(
                attrs={
                    'placeholder': 'Nutrition Info',
                }
            )
        }

        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }


class EditFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ('owner',)


class DeleteFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ('name', 'image_url', 'description',)

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'readonly': True,
                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'readonly': True,
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'readonly': True,
                }
            )
        }

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.__set_disabled_fields()
        #
        # def save(self, commit=True):
        #     if commit:
        #         self.instance.delete()
        #     return self.instance
        #
        # def __set_disabled_fields(self):
        #     for field in self.fields.values():
        #         field.disabled = True
