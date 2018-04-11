from django import forms
from boards.models import Topic


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(),
                              max_length=4000,
                              help_text='最多可输入4000个字符',
                              label='内容')

    class Meta:
        model = Topic
        fields = ['subject', 'message']
        labels = {
            'subject': '主题'
        }
