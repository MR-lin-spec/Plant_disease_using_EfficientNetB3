from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
import numpy as np
from keras.api._tf_keras.keras.preprocessing import image
from .deeplearning import model, output_list
import base64
import tensorflow as tf
from .models import User
import io
import base64


def index(request):
    if request.method == 'POST' and request.FILES.get('myfile'):
        myfile = request.FILES['myfile']
        # 读取文件内容（一次读取，然后用于后续各项处理）
        file_bytes = myfile.read()
        # 转换为 base64，后面可以用于在页面上回显图片
        b64_img = base64.b64encode(file_bytes).decode('ascii')
        # 利用 BytesIO 构造一个文件对象供 load_img 使用
        img_io = io.BytesIO(file_bytes)

        # 进行数据预处理：加载图片并调整尺寸
        img = image.load_img(img_io, target_size=(300, 300))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = tf.keras.applications.efficientnet.preprocess_input(img)
        # 若需要其他归一化处理，可以取消注释下面的代码
        # img = img / 127.5
        # img = img - 1.0

        # 使用预先加载的图模型进行预测
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
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        #注册用户
        if username is not None and password is not None:
            User.objects.create(user=username,password=password)
        #返回结果
        return redirect("login")
    elif request.method=="GET":
        return render(request,'plant_app/register.html')

