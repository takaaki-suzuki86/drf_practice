from django.urls import path, include
from rest_framework import routers
from .views import QuestionViewSet

defaultRouter = routers.DefaultRouter()
defaultRouter.register('question', QuestionViewSet)

app_name = 'signup'
urlpatterns = [
    path('', include(defaultRouter.urls)),
]
