from django.forms import ModelForm
from login.models import Users_db

class Users_dbForm(ModelForm):
    class Meta:
        model = Users_db
        fields = ("user", "passw")