from django.urls import path
from . import views


from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name='kafkaApp'

urlpatterns=[
    path('index',views.index,name='index'),
    path('rand',views.rand,name='rand'),
    path('channels',views.channels,name='channels'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('consume/', views.consume, name='room'),
    path('livestocks',views.stocks,name='stocks'),
    #path('stocks',views.stockslist,name="stockslist"),
    path('pubsub',views.pubsub,name="pubsub"),
    path('pubsubRESTAPI/<str:news>/',views.pubsubAPI,name='pubsubAPI'),
    path('iicdashboard',views.iicdashboard,name='iicdashboard')
    ]
    
urlpatterns+=staticfiles_urlpatterns()