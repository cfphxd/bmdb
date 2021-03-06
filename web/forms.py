from django import forms

SEARCH_TARGET_CHOICES = (
    ('Biomarker', 'Biomarker'),
    ('Food', 'Food'),
    ('Disease', 'Disease'),
    ('Pathway', 'Pathway'),
    ('All', 'All'),
)



class SearchForm(forms.Form):
    search_target = forms.ChoiceField(choices = SEARCH_TARGET_CHOICES)
    search_term = forms.CharField(required=True)
