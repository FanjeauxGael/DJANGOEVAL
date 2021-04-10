from django.forms.models import ModelForm
from .models import Student
from .models import Call

class StudentForm(ModelForm):

  class Meta:
    # modele
    model = Student
    # les champs qu'on vas traiter
    fields =(
      'first_name',
      'last_name',
      'birth_date',
      'email',
      'phone',
      'cursus',
      'comments',
    )

class  ParticularCallForm(ModelForm):

  class Meta:
    model = Call
    fields={
      'Date',
      'is_Missing',
      'student',
      'Reason'
    }
