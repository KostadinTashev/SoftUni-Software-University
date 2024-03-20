from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls'), ),
    path('', include('auth_demos.web.urls'), ),
]
# auth - authentication or authorization

# Auth flow:
'''
# Authentication
The User send the credentials to system
    -username & password, phone number + sms code, authentication app

# Authorization
After authentication, the system authorizes the user
'''

'''
Web1 (web app)
    - SoftUni_key = '4124-4223-4123-543344-44445f'
    
Web2 (web app)
    - SoftUni_key = '4124-4223-4123-543344-44445f'
'''

'''
DB -> pbkdf2_sha256$720000$70738lxUfqCJ7IfEqp6nAH$KXdIRCC6gIxTs6/eNr4CrQ16gNw7GB7/aa48XquAmDI=
admin -> pbkdf2_sha256$720000$70738lxUfqCJ7IfEqp6nAH$KXdIRCC6gIxTs6/eNr4CrQ16gNw7GB7/aa48XquAmDI=
'''
