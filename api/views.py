from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
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
