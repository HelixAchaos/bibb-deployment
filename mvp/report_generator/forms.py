from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField()


class ResultsForm(forms.Form):
    def __init__(self, thought_choices, *args, **kwargs):
        super(ResultsForm, self).__init__(*args, **kwargs)
        self.fields['thoughts'].choices = thought_choices

    thoughts = forms.MultipleChoiceField(choices=(),
                                         widget=forms.CheckboxSelectMultiple(),
                                         required=False)

    summary = forms.CharField(label='Write your summary here.',
                              max_length=1000,
                              widget=forms.Textarea)
    action = forms.CharField(label="What are you going to do?",
                             max_length=1000,
                             widget=forms.Textarea)
    recipient = forms.EmailField(label="Email recipient here:")