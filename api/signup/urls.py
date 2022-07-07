from django.urls import include, path
from rest_framework import routers

from .views import QuestionViewSet

defaultRouter = routers.DefaultRouter()
defaultRouter.register("question", QuestionViewSet)

app_name = "signup"
urlpatterns = [
    path("", include(defaultRouter.urls)),
]
