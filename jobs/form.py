# encoding: utf-8
from django.forms.models import ModelForm
from django import forms
from jobs.models import JobType, Job, ProfileJob, JobHistory
from users.models import Profile


class BaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class JobTypeForm(BaseForm):
    class Meta:
        model = JobType
        fields = '__all__'


class JobForm(BaseForm):
    class Meta:
        model = Job
        fields = '__all__'


class ProfileJobForm(BaseForm):
    query = Profile.objects.all() #filter(rol='TEC')
    profile = forms.ModelChoiceField(query, required=True, label='Perfil')


    class Meta:
        model = ProfileJob
        exclude = ['assign_at']


class JobHistoryForm(BaseForm):
    class Meta:
        model = JobHistory
        fields = '__all__'
        exclude = ['register_at']
