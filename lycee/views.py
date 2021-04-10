from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.views.generic.edit import CreateView
from .models import Cursus, Student , Call
from .forms import StudentForm , ParticularCallForm

# Create your views here.
# def index(request):
#   return HttpResponse("Racine de lycee")

def detail(request, cursus_id):
  cursus = Cursus.objects.get(pk=cursus_id)
  listEtu = Student.objects.filter(cursus=cursus_id)
  context = {
    'cursus' : cursus,
    'listEtu' : listEtu
  }
  return render(request, 'lycee/Cursus/detail_cursus.html', context)

def index(request):
  # result_list = Cursus.objects.all()
  result_list = Cursus.objects.order_by('name')

  # template = loader.get_template('lycee/index.html')
  context = {
    'liste' : result_list,
  }
  return render(request, 'lycee/index.html', context)
  # return HttpResponse(template.render(context,request))

def detail_student(request, student_id):
  result_list = Student.objects.get(pk=student_id)

  context = {
    'liste'  : result_list
  }

  return render(request, 'lycee/student/detail_student.html', context)

class ParticularCallCreateView(CreateView):
  model = Call

  form_class = ParticularCallForm

  template_name = 'lycee/call/particularcall.html'

  def get_success_url(self):
    return reverse('index')

class StudentCreateView(CreateView):
  # modele
  model = Student
  # formulaire
  form_class = StudentForm
  #template
  template_name = 'lycee/student/create.html'
  def  get_success_url(self):
    return reverse('detail_student',args=(self.object.pk,))