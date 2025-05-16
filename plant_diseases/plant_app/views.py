from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from keras.preprocessing import image
import numpy as np
from .deeplearning import graph, model, output_list
import base64

from .models import User


def index(request):
    if request.method == 'POST' and request.FILES.get('myfile'):
        myfile = request.FILES['myfile']
        b64_img = base64.b64encode(myfile.file.read()).decode('ascii')
        img = image.load_img(myfile, target_size=(224, 224))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = img/255

        with graph.as_default():
            prediction = model.predict(img)

        prediction_flatten = prediction.flatten()
        max_val_index = np.argmax(prediction_flatten)
        result = output_list[max_val_index]

        return render(request, "plant_app/index.html", {
            'result': result, 'file_url': b64_img})

    return render(request, "plant_app/index.html")


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        #如果用户名和密码符合要求
        if username == "Lin" and password == "1234":
            return redirect('index')  # 登录成功，重定向到主页
        #如果是注册按钮
        else:
            return redirect('error')  # 登录失败，重定向到错误页面
    else:
            return render(request, 'plant_app/login.html')  # 渲染登录页面

def error_view(request):
    return render(request, 'plant_app/error.html')

#注册界面
def register_view(request):
    if request.method=="POST":
        #获取信息
        username = request.POST['username']
        password = request.POST['password']
        #注册用户
        User.objects.create(user=username,password=password)
        #返回结果
        return redirect("login")
    elif request.method=="GET":
        return render(request,'plant_app/register.html')

