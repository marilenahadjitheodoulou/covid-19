from django.urls import path
from . import views
from contacts import views as contact_views

app_name='contacts'
urlpatterns = [
    path('upload/', contact_views.upload, name='upload'),
    path('mycontacts/', contact_views.UploadView.as_view(), name='mycontacts'),
]
