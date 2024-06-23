from django.shortcuts import render
from django.template import loader


# Create your views here.
def show_fruits_and_students(request):
    templates = loader.get_template("mytemplate.html")
    context = {
        "fruits":["Apple", "Bannana", "Mango"],
        "students":["Ajay", "Karthik", "Preethi", "Ramesh", "Ramya"],
    }
    return render(request, "mytemplate.html", context)
