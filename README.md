**This is my final design,Using EfficientNetB3,SQlite3,Django,the following are some setting about that**
**My CondaEnvironment list**
absl-py                      2.1.0
asgiref                      3.8.1
astunparse                   1.6.3
cachetools                   5.5.2
certifi                      2025.4.26
charset-normalizer           3.4.2
coreapi                      2.3.3
coreschema                   0.0.4
Django                       5.2
django-cors-headers          4.7.0
djangorestframework          3.16.0
flatbuffers                  25.2.10
gast                         0.6.0
google-auth                  2.40.1
google-auth-oauthlib         1.2.2
google-pasta                 0.2.0
grpcio                       1.71.0
h5py                         3.12.1
idna                         3.10
itypes                       1.2.0
Jinja2                       3.1.6
joblib                       1.5.0
keras                        3.3.3
libclang                     18.1.1
Markdown                     2.6.10
markdown-it-py               2.2.0
MarkupSafe                   3.0.2
mdurl                        0.1.0
mkl_fft                      1.3.11
mkl_random                   1.2.8
mkl-service                  2.4.0
ml-dtypes                    0.2.0
namex                        0.0.7
numpy                        1.26.4
oauthlib                     3.2.2
opt_einsum                   3.4.0
optree                       0.14.1
packaging                    24.2
pillow                       11.2.1
pip                          25.1
protobuf                     4.25.7
pyasn1                       0.6.1
pyasn1_modules               0.4.2
Pygments                     2.2.0
pytz                         2025.2
requests                     2.32.3
requests-oauthlib            2.0.0
rich                         13.9.4
rsa                          4.9.1
schema                       0.7.7
scikit-learn                 1.6.1
scipy                        1.15.3
setuptools                   78.1.1
six                          1.17.0
sqlparse                     0.5.2
tensorboard                  2.15.2
tensorboard-data-server      0.7.2
tensorflow                   2.15.0
tensorflow-estimator         2.15.0
tensorflow-intel             2.15.0
tensorflow-io-gcs-filesystem 0.31.0
termcolor                    3.1.0
threadpoolctl                3.6.0
typing_extensions            4.12.2
tzdata                       2025.2
uritemplate                  4.1.1
urllib3                      2.4.0
Werkzeug                     3.1.3
wheel                        0.45.1
wrapt                        1.14.1

**Something about using django-rest framework that you should attention**
1:using  **keras.api._tf_keras.keras.preprocessing** instead **tensorflow.keras.preprocessing**
2:using **from keras.src.saving import load_model** instead  **from tensorflow.keras.models import load_model** and so on

All in all,the tensorflow api give me bad experiences than pytorch,I advise you to use pytorch to imporve this project if necessary
Any question if you have,Don't hestiate to email me,My email is 3304452595@qq.com  In Fujan agriculate and forest university
