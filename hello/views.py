from django.shortcuts import render

# Create your views here.
# 定义一个业务请求函数
def hello(request):
    return render(request,'table.html')