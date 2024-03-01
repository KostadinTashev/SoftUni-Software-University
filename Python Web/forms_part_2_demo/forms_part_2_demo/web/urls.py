from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from forms_part_2_demo.web.views import index, list_persons, create_person

urlpatterns = [
    path('', index, name='index'),
    path('persons/', list_persons, name='list persons'),
    path('persons/create/', create_person, name='create person'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
