from django.shortcuts import render,redirect
from crud.forms import StudentForm
from crud.models import Student


def add(request):
    if request.method == 'POST':
        form = StudentForm (request.POST)
        if form.is_valid ():
            try:
                form.save ()
                return redirect ('/show')
            except:
                pass
    else:
        form = StudentForm ()
        return render (request,'index.html',{'form':form})


def getdata(request):
    student = Student.objects.all ()
    return render (request,'view.html',{'student':student})


def editdata(request,id):
    student = Student.objects.get (id=id)
    return render (request,'edit.html',{'student':student})


def updatedata(request,id):
    student = Student.objects.get (id=id)
    form = StudentForm (request.POST,instance=student)
    if form.is_valid ():
        form.save ()
        return redirect ('/show')
    return render (request,'edit.html',{'student':student})
def deletedata(request, id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('/show')
