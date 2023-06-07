from django.shortcuts import render,redirect
from testapp.forms import StudentForm
from testapp.models import Student
# Create your views here.
def index_view(request):
    return render(request,'testapp/home.html')

def stu_form_view(request):
    form=StudentForm()

    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/list')


    return render(request,'testapp/add.html',{'form':form})
def student_list(request):
    stu=Student.objects.all()
    return render(request,'testapp/list.html',{'stu':stu})
