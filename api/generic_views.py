from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from api.serializers import ClassRoomModelSerializer, StudentModelSerializer, UserModelSerializer, UserProfileModelSerializer
from crud.models import ClassRoom, Student, UserProfile

class ClassRoomGenericView(ListAPIView):
    serializer_class = ClassRoomModelSerializer
    queryset = ClassRoom.objects.all()

class ClassRoomGenericCreateView(CreateAPIView):
    serializer_class = ClassRoomModelSerializer
    queryset = ClassRoom.objects.all()

class ClassRoomListCreateView(ListCreateAPIView):
    serializer_class = ClassRoomModelSerializer
    queryset = ClassRoom.objects.all()

class ClassRoomUpdateView(UpdateAPIView):
    serializer_class = ClassRoomModelSerializer
    queryset = ClassRoom.objects.all()

class ClassRoomRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = ClassRoomModelSerializer
    queryset = ClassRoom.objects.all()

class ClassRoomViewSet(ModelViewSet):
    serializer_class = ClassRoomModelSerializer
    queryset = ClassRoom.objects.all()

class UserProfileViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserProfileModelSerializer
    queryset = UserProfile.objects.all()

class UserListCreateAPIViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()

class StudentViewSet(ModelViewSet):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()


# from rest_framework import status