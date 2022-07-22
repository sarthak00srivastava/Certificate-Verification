from django.shortcuts import render
from django.http import HttpResponse
from verify.models import Certificates

# Create your views here.
def home(request):
    return render(request, 'home.html')


def authenticate(request):
    if request.method == 'POST':
        c_num = request.POST.get('c_num', '')
        print(c_num)
        obj = Certificates.objects.get(c_num=c_num)
        dic = {
            'Certificate No. : ':obj.c_num,
            'Name : ':obj.c_name,
            'Title : ':obj.c_title,
            'Mode : ':obj.c_mode,
            'Start Date : ':obj.start_date,
            'End Date : ':obj.end_date,
        }
        return render(request, 'home.html', {'dic':dic})
