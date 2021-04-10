from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.views.generic.edit import CreateView
from .models import Cursus, Student , Call , GeneralCall
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

def callListAll(request):
  ListCall = GeneralCall.objects.order_by('Date')

  context = {
    'listcall' : ListCall
  }
  return render(request, 'lycee/call/call.html', context)

def detailCall(request, call_id):
  listcall = Call.objects.filter(generalCall= call_id)
  gencall = GeneralCall.objects.get(pk=call_id)
  context = {
    'listcall' : listcall,
    'generalcall': gencall
  }
  return render(request, 'lycee/call/detailCall.html', context)

def callListbycursus(request , cursus_id):
  ListCall = GeneralCall.objects.filter(cursus=cursus_id).order_by('Date')
  cursus = Cursus.objects.get(pk=cursus_id)

  context = {
    'listcall' : ListCall,
    'cursus' : cursus
  }
  return render(request, 'lycee/call/listCall.html', context)


def call(request, cursus_id):
  cursus = Cursus.objects.get(pk=cursus_id)
  listEtu = Student.objects.filter(cursus=cursus_id).order_by('last_name')
  context = {
    'cursus' : cursus,
    'listEtu' : listEtu
  }
  if request.POST.get("submit") == 'Submit':
    date = request.POST.get("date")
    print(date)
    appel = GeneralCall()
    appel.Date = date
    appel.cursus = Cursus.objects.get(pk=cursus_id)
    appel.save()
    for etu in listEtu:
      id = "etu"+str(etu.id)
      if request.POST.get(id) == "on":
        missing = Call()
        missing.Reason = ""
        missing.is_Missing = 1
        missing.Date = date
        missing.student = Student.objects.get(pk=etu.id)
        missing.generalCall = appel
        missing.save()
      else:
        missing = Call()
        missing.Reason = ""
        missing.is_Missing = 0
        missing.Date = date
        missing.student = Student.objects.get(pk=etu.id)
        missing.generalCall = appel
        missing.save()
      

  return render(request, 'lycee/call/call.html', context)


def editStudent(request, student_id):

  cursus = Cursus.objects.order_by('name')
  etu = Student.objects.get(pk=student_id)

  context = {
    'cursus' : cursus,
    'etu' : etu
  }

  if request.POST.get("submit") == 'Send':
    etu.last_name = request.POST.get("nom")
    etu.first_name = request.POST.get("prenom")
    etu.cursus = request.POST.get("cursus")
    etu.save()
    return reverse('index')


  return render(request, "lycee/student/edit_student.html", context)

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