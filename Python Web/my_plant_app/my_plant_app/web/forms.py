from django import forms

from my_plant_app.web.models import Profile, Plant


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('profile_picture',)


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


class PlantCreateForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class PlantEditForm(PlantCreateForm):
    pass


class PlantDeleteForm(PlantCreateForm):
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
