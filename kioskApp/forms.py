# coding: utf-8
from kioskApp.models import *
from dojango import forms
import django
import datetime

class RobotScriptForm(forms.ModelForm):
    class Meta:
        model =RobotScript
    exclude = ('user',)
class  PlatePlasticaForm(forms.ModelForm):
    class Meta:
        model=PlatePlastica
        fields =[ 'description','wells']
    description = forms.CharField(max_length=100)
    wells = forms.CharField(max_length=4)
class  ExperimentForm(forms.ModelForm):
    class Meta:
        model=Experiment
	exclude = ('user','means','distance')
    grade = forms.FloatField(initial=0.0)
    grade.widget.attrs['readonly'] = True
        #fields =['name', 'description','volume', 'date', 'pipetingMode', 'liquidClass', 'tipType', 'sourcePlastic','destPlastic','plateReader']
    date =  forms.DateTimeField(initial=datetime.datetime.today() + datetime.timedelta(hours=2))
    date.required = False

class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadModel
class RobotScriptForm(forms.ModelForm):
    class Meta:
        model= RobotScript
    date = forms.DateTimeField(initial=datetime.datetime.today() + datetime.timedelta(hours=2))


class RobotScriptErrorForm(forms.ModelForm):
    class Meta:
        model= RobotScriptError
    exclude = ('robotscript',)
    date = forms.DateTimeField(initial=datetime.datetime.today() + datetime.timedelta(hours=2))
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
    user = forms.CharField(widget=forms.HiddenInput(),required=False)
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email']
    username = forms.CharField()
    username.label = u"שם משתמש"
    password = forms.CharField()
    password.label = u"ססמא"
    email = forms.CharField()
    email.label = u"אי מייל"
    email.required = False

class LiquidClassVolumeForm(forms.ModelForm):
    class Meta:
        model = LiquidClassVolume
