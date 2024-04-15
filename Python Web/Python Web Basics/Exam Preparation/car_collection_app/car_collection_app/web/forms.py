from django import forms

from car_collection_app.web.models import Profile, Car


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['id']

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


class BaseCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CreateCarForm(BaseCarForm):
    pass


class EditCarForm(BaseCarForm):
    pass


class DeleteCarForm(BaseCarForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.disabled = True
