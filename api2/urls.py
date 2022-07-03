from django.urls import path, include
# from . import views
# from .signup.views import TestViewSet


app_name = 'api'
urlpatterns = [
    # path("signup/", include('api.signup.urls'), name="signup"),
    path("signup/", include('api.signup.urls'), name="signup"),
    # re_path("^signup/?$", TestViewSet.as_view()),
]
