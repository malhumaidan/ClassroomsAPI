from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from classes.views import ClassroomsListView, ClassroomsDetailView, ClassroomsCreateView, ClassroomsUpdateView, ClassroomsDeleteView
from users.views import LoginAPIView, RegisterAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", RegisterAPIView.as_view(), name="api-register"),
    path("login/", LoginAPIView.as_view(), name="api-login"),



    path("list/", ClassroomsListView.as_view(), name="api-classroom-list"),
    path("classroom/details/<int:object_id>", ClassroomsDetailView.as_view(), name="api-classroom-detail"),
    path("classroom/create/<int:object_id>", ClassroomsCreateView.as_view(), name="api-classroom-create"),
    path("classroom/update/<int:object_id>", ClassroomsUpdateView.as_view(), name="api-classroom-update"),
    path("classroom/delete/<int:object_id>", ClassroomsDeleteView.as_view(), name="api-classroom-delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
