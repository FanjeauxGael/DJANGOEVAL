"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lycee import views
from lycee.views import StudentCreateView , ParticularCallCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lycee', views.index, name="index"),
    path('lycee/<int:cursus_id>', views.detail, name="detail"),
    path('lycee/student/<int:student_id>', views.detail_student, name="detail_student"),
    path('lycee/student/create',StudentCreateView.as_view(),name='create_student'),
    path('lycee/particularCall/', ParticularCallCreateView.as_view(), name='particular_call'),
    path('lycee/Call/<int:cursus_id>', views.call, name='call'), 
    path('lycee/student/edit/<int:student_id>', views.editStudent, name='editetu'),
    path('lycee/ListCall/', views.callListAll, name='listAll'),
    path('lycee/ListCallByCursus/<int:cursus_id>', views.callListbycursus, name='listbyCursus '),
    path('lycee/DetailCall/<int:call_id>', views.detailCall, name='detailCall ')
]