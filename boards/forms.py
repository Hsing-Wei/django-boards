from django import forms
from boards.models import Topic


class NewTopicForm(forms.ModelForm):
    subject = forms.CharField(label='主题')
    message = forms.CharField(widget=forms.Textarea(), max_length=4000, label='内容')

    class Meta:
        model = Topic
        fields = ['subject', 'message']
