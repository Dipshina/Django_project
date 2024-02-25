from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("""
<html>
    <head>
        <title> Django Project </title>
    </head>
    <body>
        <h1> Hello World </h1>
        <h2> I am learning Django </h1>
    </body>
                        
</html>

""")

def root_page(request):
    return render(request, template_name = "myapp/root_page.html")
