from django.shortcuts import render,redirect
from .models import Employee

def index(request):
    obj = Employee.objects.all()
    return render(request, "index.html", {'obj': obj})
def addem(request):
    if request.method == 'POST':
        empname = request.POST.get('empname')
        empdesignation = request.POST.get('empdesignation')
        image = request.FILES.get('image')  
        
        if image:
            employee = Employee(empname=empname, empdesignation=empdesignation, image=image)
            employee.save()
            return redirect('/')
        else:
            pass

    return render(request, "add-employee.html")

def empf(request,id):
    obj = Employee.objects.get(id = id)
    if request.method == 'POST':
        empname = request.POST.get('empname')
        empdesignation = request.POST.get('empdesignation')
        image = request.FILES.get('image')  

        obj.empname = empname
        obj.empdesignation = empdesignation
        obj.image = image
    
        if image:
            obj.save()
            return redirect('/')
        else:
            pass
    return render(request, "emp-full.html",{'obj': obj})

def delete(request,id):
    obj = Employee.objects.get(id = id)
    obj.delete()
    return redirect('/')

