from django.urls import include, re_path, path


urlpatterns = [
    # https://djoser.readthedocs.io/en/latest/getting_started.html

    re_path(r'', include('djoser.urls')),

    # jwt/create/     # jwt/refresh/     # jwt/verify/
    path(r'', include('djoser.urls.jwt')),
]
