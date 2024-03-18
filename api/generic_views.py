from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from api.serializers import ClassRoomModelSerializer, UserProfileModelSerializer
from crud.models import ClassRoom, UserProfile
from rest_framework.viewsets import ModelViewSet

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
    serializer_class = UserProfileModelSerializer
    queryset = UserProfile.objects.all()