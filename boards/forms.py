from django import forms
from boards.models import Topic


class NewTopicForm(forms.ModelForm):
    # subject = forms.CharField(label='主题')
    message = forms.CharField(widget=forms.Textarea(), max_length=4000, label='内容')

    class Meta:
        model = Topic
        fields = ['subject', 'message']

        def __init__(self, *args, **kwargs):
            super(NewTopicForm, self).__init__(*args, **kwargs)
            self.fields['subject'].label = '主题'
