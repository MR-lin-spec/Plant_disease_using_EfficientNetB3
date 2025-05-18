import tensorflow as tf
import keras
# global graph, model, output_list
# 定义计算图
from keras.src.saving import load_model
# 在 deeplearning.py 中定义 contrastive_loss
def contrastive_loss(y_true, y_pred):
    margin = 1
    square_pred = tf.square(y_pred)
    margin_square = tf.square(tf.maximum(margin - y_pred, 0))
    return tf.reduce_mean(y_true * square_pred + (1 - y_true) * margin_square)


# model = load_model(r'D:\DjangoProject\DjangoDesign\Plant-Diseases-Recognition\plant_diseases\plant_app\model_weights.h5')#这里修改预训练文件

# 确保 contrastive_loss 已定义
model = load_model(
    r'D:\DjangoProject\DjangoDesign\Plant-Diseases-Recognition\plant_diseases\plant_app\LightWeight_model_EfficientNet.hdf5',

)
output_dict2 = {
    '苹果___苹果炭疽病': 0,
    '苹果___黑腐病': 1,
    '苹果___苹果锈病': 2,
    '苹果___健康': 3,
    '蓝莓___健康': 4,
    '樱桃（包括酸樱桃）___白粉病': 5,
    '樱桃（包括酸樱桃）___健康': 6,
    '玉米（玉蜀黍）___灰斑病': 7,
    '玉米（玉蜀黍）___普通锈病': 8,
    '玉米（玉蜀黍）___北方叶枯病': 9,
    '玉米（玉蜀黍）___健康': 10,
    '葡萄___黑腐病': 11,
    '葡萄___埃斯卡病（黑霉病）': 12,
    '葡萄___叶枯病（伊萨里奥皮斯斑叶病）': 13,
    '葡萄___健康': 14,
    '柑橘___黄龙病（柑橘绿ing病）': 15,
    '桃___细菌斑点病': 16,
    '桃___健康': 17,
    '甜椒___细菌斑点病': 18,
    '甜椒___健康': 19,
    '马铃薯___早疫病': 20,
    '马铃薯___晚疫病': 21,
    '马铃薯___健康': 22,
    '覆盆子___健康': 23,
    '大豆___健康': 24,
    '西葫芦___白粉病': 25,
    '草莓___叶灼伤': 26,
    '草莓___健康': 27,
    '番茄___细菌斑点病': 28,
    '番茄___早疫病': 29,
    '番茄___晚疫病': 30,
    '番茄___叶霉病': 31,
    '番茄___斑枯病': 32,
    '番茄___蜘蛛螨（二斑蜘蛛螨）': 33,
    '番茄___靶斑病': 34,
    '番茄___番茄黄化卷叶病毒': 35,
    '番茄___番茄花叶病毒': 36,
    '番茄___健康': 37
}

output_dict = {
    "辣椒/甜椒-细菌性病害": 0,
    "辣椒/甜椒-健康": 1,
    "马铃薯-早疫病": 2,
    "马铃薯-健康": 3,
    "马铃薯-晚疫病": 4,
    "番茄-靶斑病": 5,
    "番茄-花叶病毒": 6,
    "番茄-黄化病": 7,
    "番茄-细菌性斑点病": 8,
    "番茄-早疫病": 9,
    "番茄-健康": 10,
    "番茄-晚疫病": 11,
    "番茄-叶霉病": 12,
    "番茄-叶斑病": 13,
    "番茄-红蜘蛛危害": 14
}
output_list = list(output_dict.keys())
