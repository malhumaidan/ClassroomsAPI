from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from classes.serializers import ClassroomsListSerializer, ClassroomsCreateSerializer
from classes.models import Classroom



class ClassroomsListView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomsListSerializer

class ClassroomsDetailView(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomsListSerializer
    lookup_field = "id"
    lookup_url_kwarg = "object_id"


class ClassroomsCreateView(CreateAPIView):
    serializer_class = ClassroomsCreateSerializer

    def perform_create(self, serializer):
        serializer.save(classrooms=self.request.user)


class ClassroomsUpdateView(RetrieveUpdateAPIView):
    serializer_class = ClassroomsCreateSerializer
    queryset = Classroom.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "object_id"


class ClassroomsDeleteView(DestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomsListSerializer
    lookup_field = "id"
    lookup_url_kwarg = "object_id"