from django.urls import path
from qaz.views import ClothesViews

app_name = 'clothes'

urlpatterns = [
    path('', ClothesViews.as_view(), name='home'),
]