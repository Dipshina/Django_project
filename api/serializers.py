# Serializers help to serialize and deserialize data
# Process of converting native types (queryset, object) to JSON data is serialization
# Process of validating and converting JSON type to python object is deserialization

from django.contrib.auth.models import User
from rest_framework import serializers
from crud.models import ClassRoom, Student, UserProfile

class ClassRoomSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length=5)

class ClassRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['id', 'name']



class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name','email', 'password', 'is_active']
        extra_kwargs = {
            "password": {
                "write_only":True
            }
        }

    # Password hash garna use gareko
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data) #user creation without their password
        user.set_password(password) # user password hashed
        user.save()
        return user
    

class UserProfileModelSerializer(serializers.ModelSerializer):
    # user = UserModelSerializer()
    class Meta:
        model= UserProfile
        fields = ['id', 'address', 'phone', 'profile_picture', 'user']

    def get_fields(self):
        request = self.context.get("request")
        fields = super().get_fields()
        if request and request.method.lower() == "get":
            fields['user'] = UserModelSerializer()
        return fields
    

class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'classroom', 'user']


