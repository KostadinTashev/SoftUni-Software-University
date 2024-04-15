from django import forms

from eventer_app.web.models import Profile, Event


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'profile_picture', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            Event.objects.all().delete()
            self.instance.delete()
        return self.instance

    def __set_hidden_fields(self):
        for field in self.fields.values():
            field.widget = forms.HiddenInput()


class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_name', 'category', 'description', 'date', 'event_image')
        labels = {
            'event_name': 'NAME',
        }


class EditEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        labels = {
            'event_name': 'NAME'
        }


class DeleteEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        labels = {
            'event_name': 'NAME'
        }

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
