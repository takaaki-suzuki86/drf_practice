from django.urls import include, path, re_path
from rest_framework import routers

from . import views

# router = routers.DefaultRouter()
# router.register(r'signup', QuestionViewSet)


# app_name = 'api'
urlpatterns = [
    # path("signup/", include('api.signup.urls'), name="signup"),
    # path("signup/", include('api.signup.urls'), name="signup"),
    path("", views.index, name="index"),
    # path("signup/", include(defaultRouter.urls)),
    path("signup/", include("api.signup.urls"), name="signup"),
]
