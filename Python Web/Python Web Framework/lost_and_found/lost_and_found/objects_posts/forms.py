from lost_and_found.objects_posts.form_mixins import FieldsWithFormControlClassMixin
from lost_and_found.objects_posts.models import Post, Object
from django import forms


class PostCreateForm(FieldsWithFormControlClassMixin, forms.ModelForm):
    form_control_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_form_controls()

    class Meta:
        model = Post
        exclude = ('object', 'found')


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('object',)


class ObjectForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = "__all__"
