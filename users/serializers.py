from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(allow_blank=True, read_only=True)

    def validate(self, data):
        my_username = data.get("username")
        my_password = data.get("password")

        try:
            user_obj = User.objects.get(username=my_username)
        except User.DoesNotExist:
            raise serializers.ValidationError("This username does not exist")

        if not user_obj.check_password(my_password):
            raise serializers.ValidationError("Incorrect username/password combination!")

        payload = RefreshToken.for_user(user_obj)
        token = str(payload.access_token)

        data["access"] = token

        return data


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(allow_blank=True, read_only=True)


    class Meta:
        model = User
        fields = ["username", "password", "access"]

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()

        payload = RefreshToken.for_user(new_user)
        token = str(payload.access_token)

        validated_data["access"] = token
        return validated_data
