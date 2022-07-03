from django.urls import path, include, re_path
from . import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'signup', QuestionViewSet)

# app_name = 'api'
urlpatterns = [
    # path("signup/", include('api.signup.urls'), name="signup"),
    # path("signup/", include('api.signup.urls'), name="signup"),
    path("", views.index, name="index"),
    # path("signup/", include(defaultRouter.urls)),
    path("signup/", include('api.signup.urls'), name="signup"),
    # path("signup/", JobGroupingList.as_view()),
]
