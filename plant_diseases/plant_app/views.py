from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from keras.preprocessing import image
import numpy as np
from .deeplearning import graph, model, output_list
import base64


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
        username = request.POST['username']
        password = request.POST['password']

        return render(request, 'plant_app/index.html')
        #user = authenticate(request, username=username, password=password)
        #if user is not None:
         #   login(request, user)
         #   return redirect('index')  # 登录成功后重定向到主页
        #else:
            # 登录失败，返回登录页面并显示错误信息
         #   return render(request, 'plant_app/login.html', {'错误信息': '登录失败'})
    else:
        return render(request, 'plant_app/login.html')


