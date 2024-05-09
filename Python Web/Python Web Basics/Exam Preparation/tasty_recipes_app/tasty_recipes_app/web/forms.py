from django import forms

from tasty_recipes_app.web.models import Profile, Recipe


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['bio']
        error_messages = {
            'nickname': {
                'min_length': "Nickname must be at least 2 characters long!",
                'unique': "This nickname is already taken.",
            },
            'first_name': {
                'required': "First name is required.",
                'invalid': "Invalid first name.",
            },
            'last_name': {
                'required': "Last name is required.",
                'invalid': "Invalid last name.",
            },
        }

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['id']

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


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(),
            'cuisine_type': forms.Select(attrs={'class': 'form-control'}),
            'ingredients': forms.Textarea(
                attrs={
                    'placeholder': 'ingredient1, ingredient2, ...',
                    'rows': 10,
                    'cols': 40,
                }),
            'instructions': forms.Textarea(
                attrs={
                    'placeholder': 'Enter detailed instructions here...',
                    'rows': 10,
                    'cols': 40,
                    'id': 'id_ingredients',
                }),
            'cooking_time': forms.NumberInput(),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Optional image URL here...'
                })
        }
        labels = {
            'cuisine_type': 'Cuisine Type',
            'cooking_time': 'Cooking Time',
            'image_url': 'Image URL',
        }
        help_texts = {
            'ingredients': 'Ingredients must be separated by a comma and space.',
            'cooking_time': 'Provide the cooking time in minutes.',
        }


class EditRecipeForm(CreateRecipeForm):
    pass


class DeleteRecipeForm(CreateRecipeForm):
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
