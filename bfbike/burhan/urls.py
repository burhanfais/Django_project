from django.urls import path
from. import views


urlpatterns=[
    path('',views.main,name='burhan'),
    path('Off_road/',views.Off_road,name='Off_road'),
    path('on_road/',views.on_road,name='on_road'),
    path('register/',views.register,name='register'),
    path('mt15/',views.mt15,name='mt15'),
    path('enfield350',views.enfield350,name='enfield350'),
    path('apachertr',views.apachertr,name='apachertr'),
    path('ktm390/',views.ktm390,name='ktm390'),
    path('yamahar15/',views.yamahar15,name='yamahar15'),
    path('himalyan/',views.himalyan,name='himalyan'),
    path('trk/',views.trk,name='trk'),
    path('ktm/',views.ktm,name='ktm'),
    path('xpluse/',views.xpluse,name='xpluse'),
    path('bmw/',views.bmw,name='bmw'),
    path('yezdi/',views.yezdi,name='yezdi'),
    path('data1/',views.data1,name='data1'),
    path('data2/',views.data2,name='data2')

]