from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ClassRoomSerializer, ClassRoomModelSerializer
from crud.models import ClassRoom, Student, UserProfile

def home(request):
    return JsonResponse({
        "message": "I am learning APIs"
    })

class HomeView(APIView):
    def get(self,*args,**kwargs):
        return Response({
            "message":"This is from classbased APIView"
        })
        

class StudentAPIView(APIView):
    def get(self, *args, **kwargs):
        return Response({
            "name": "Jon",
            "age": 30,
            "address": "KTM",
            "email": "jon@gmail.com"
        })
    
class StudentListAPIView(APIView):
    def get(self, *args, **kwargs):
        student = [
            {"name": "Jon", "age": 30, "address":"KTM", "email": "jon@gmail.com"},
            {"name": "Jane", "age": 20, "address":"PKR", "email": "jane@gmail.com"},
            {"name": "Smith", "age": 31, "address":"LTR", "email": "smith@gmail.com"},
        ]
        return Response(student)
    
class SimpleClassRoomView(APIView):
    def get(self, *args, **kwargs):
        classroom = ClassRoom.objects.get(id=16)
        response = {
            "id": classroom.id,
            "name": classroom.name
        }
        return Response(response)


class SimpleClassRoomListView(APIView):
    def get(self, *args, **kwargs):
        classrooms = ClassRoom.objects.all()
        response = []
        for classroom in classrooms:
            response.append({
                "id": classroom.id,
                "name": classroom.name
            })
        return Response(response)
    
    def post(self, *args, **kwargs):
        data = self.request.data
        name = data.get("name")
        classroom, _ = ClassRoom.objects.get_or_create(name = name)
        return Response({
            "message": "Success",
            "id": classroom.id,
            "name": classroom.name
        })
    
class ClassRoomRetrieveView(APIView):
    def get(self, *args, **kwargs):
        id = kwargs.get("id")
        try:
            classroom = ClassRoom.objects.get(id=id) # Classroom Objects

        except ClassRoom.DoesNotExist:
            return Response({
                "detail" : "Not Found"
            })
        serializer = ClassRoomSerializer(classroom) # serialization
        return Response(serializer.data)
    

class ClassRoomView(APIView):
    def get(self, *args, **kwargs):
        queryset = ClassRoom.objects.all()  # classroom queryset
        serializer = ClassRoomSerializer(queryset, many = True) #serialization
        return Response(serializer.data)
    

    def post(self, *args, **kwargs):
        # data = self.request.data
        # serializer = ClassRoomSerializer(data = data) # deserialization
        serializer = ClassRoomSerializer(data = self.request.data) # deserialization
        if serializer.is_valid():
            name = serializer.validated_data["name"]
            classroom, _ = ClassRoom.objects.get_or_create(name = name)
            return Response({
                "message": "Success",
                "id": classroom.id,
                "name": classroom.name
                })
        else:
            return Response(serializer.errors)
        
    
    # def post(self, *args, **kwargs):
    #     serializer = ClassRoomModelSerializer(data = self.request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors)
        

class ClassRoomUpdateDeleteView(APIView):
    def patch(self, *args, **kwargs):
        serializer = ClassRoomSerializer(data = self.request.data)
        if serializer.is_valid():
            name = serializer.validated_data["name"]
            classroom = ClassRoom.objects.get(id=kwargs['id'])
            classroom.name = name
            classroom.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    def delete(self, *args, **kwargs):
        id = kwargs.get("id")
        classroom = ClassRoom.objects.get(id=id)
        classroom.delete()
        return Response({
            "message": "Classroom deleted successfully!"
        })
