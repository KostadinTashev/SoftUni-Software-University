from django import forms
from django.forms import modelform_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from cbv_demos.web.models import Article


# View in Django:
# 1. The `view` must be `callable`
# 2. Returns 'HttpResponse` object

def list_articles(request):
    context = {
        'articles': Article.objects.all(),
    }

    return render(request,
                  'articles/list.html',
                  context)


# views.CreateView
# views.ListView
# views.UpdateView
# views.DetailView
# views.DetailView


class BaseView:
    def get(self, request):
        pass

    def post(self, request):
        pass

    @classmethod
    def as_view(cls):
        self = cls()

        def view(request):
            if request.method == 'GET':
                return self.get(request)
            else:
                return self.post(request)

        return view


# class ArticlesListView(BaseView):
# class ArticlesListView(views.View):
#     def get(self, request):
#         context = {
#             'articles': Article.objects.all(),
#         }
#
#         return render(request,
#                       'articles/list.html',
#                       context)

# class ArticlesListView(views.TemplateView):
#     template_name = 'articles/list.html'
#
#     # static data
#     # extra_context = {
#     #     'articles': Article.objects.all(),
#     # }
#
#     # dynamic data
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['articles'] = Article.objects.all()
#         return context

class ArticlesListView(views.ListView):
    template_name = 'articles/list.html'
    model = Article
    context_object_name = 'articles'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()

        search = self.request.GET.get('search', '')
        queryset = queryset.filter(title__icontains=search)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context


class ArticleDetailView(views.DetailView):
    model = Article
    template_name = 'articles/detail.html'


# class ArticleForm(forms.ModelForm):
#     pass

# Forms:
# 1. Auto created based on 'fields' (default)
# 2. `form_class` - return class
# 3. `get_form_class` - return class
# 4. `get_form` - return instance

class DisabledFormFieldsMixin:
    disabled_fields = ()

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)

        for field in self.disabled_fields:
            form.fields[field].widget.attrs['disabled'] = 'disabled'
            form.fields[field].widget.attrs['readonly'] = 'readonly'

        return form


class ArticleCreateView(DisabledFormFieldsMixin, views.CreateView):
    model = Article
    template_name = 'articles/create.html'
    fields = '__all__'
    disabled_fields = ('title',)
    success_url = reverse_lazy('list articles cbv')

    # form_class = modelform_factory(
    #     Article, fields='__all__',
    #     widgets={
    #         'title': forms.TextInput(
    #             attrs={
    #                 'class': 'abc',
    #             }
    #         )
    #     })

    # form_class = ArticleForm

    # def get_form_class(self):
    #     pass

    # def get_form(self, form_class=None):
    #     pass


class ArticleUpdateView(views.UpdateView):
    pass


class ArticleDeleteView(DisabledFormFieldsMixin, views.DeleteView):
    model = Article
    template_name = 'articles/delete.html'
    form_class = modelform_factory(
        Article,
        fields=('title', 'content')
    )
    disabled_fields = ('title', 'content')
    # success_url = reverse_lazy('list articles cbv')


class RedirectToArticlesView(views.RedirectView):
    url = reverse_lazy('list articles cbv')
