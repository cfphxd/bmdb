from django import forms

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)

class SearchForm(forms.Form):
    choice = forms.ChoiceField(choices = ([('1','1'), ('2','2'),('3','3'), ]))
    title = forms.Select(choices=TITLE_CHOICES) 
    search_term = forms.CharField(max_length=100)
