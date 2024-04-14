from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('drf_demos.web.urls')),
    path('api/', include('drf_demos.api.urls')),
    path('accounts/', include('drf_demos.accounts.urls')),
]

'''
Rest -> Representational State Transfer
API -> Application Programming Interface

(JSON, XML, YAML)

=> REST API


Author (first_name, last_name)
Book (title, description, author)

# Authors : /authors/

C -> Create author
POST /authors/

R -> Get author details
GET /authors/{ID}/
{
    'first_name': 'Kostadin',
    'last_name': 'Tashev'
}

R -> Get all authors
GET /authors/

U -> Update author
PUT /authors/{ID}/
{
    'first_name': 'Kostadin 2',
    'last_name': 'Tashev'
}
PATCH /authors/{ID}/
{
    'first_name': 'Kostadin 2'
}

D -> Delete author
DELETE /authors/{ID}


## Actions

PUT /authors/{ID}/upvote/

# Summarize:

GET /authors/
GET /authors/{ID}/
POST /authors/
PUT /authors/{ID}/
(PATCH /authors/{ID}/)
DELETE /authors/{ID}/
'''

'''
type2 is a text format (JSON, txt, csv, XML)
Serialization -> obj(type1) -> obj2(type2)
Deserialization -> obj2(type2) -> obj(type1)
'''

'''
AJAX - Asynchronous JavScript and XML

'''
