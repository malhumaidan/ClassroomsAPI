from rest_framework import serializers

from classes.models import Classroom



class ClassroomsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ["subject", "name", "year", "classrooms"]


class ClassroomsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ["subject", "name", "year"]