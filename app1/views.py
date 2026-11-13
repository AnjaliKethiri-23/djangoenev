from django.shortcuts import render
from django.views import View
# Create your views here.
from app1.models import emp_table
from django.http import HttpResponse


class Emp_details(View):
    def get(self,request):
        try:
            data=emp_table.objects.all()
            context={
                'data':data
            }
            return render(request,"app1_tem/home.html",context)
        except Exception as n:
            return HttpResponse(f"<h1 style='color:red'>{n}</h1>")