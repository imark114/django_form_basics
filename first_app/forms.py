from django import forms
import datetime

GRADUATION_YEAR_CHOICES = ['2019', '2020', '2021','2022']
FAVORITE_COLORS_CHOICES = [
    ('white', 'White'),
    ('green', 'Green'),
    ('black', 'Black'),
]
FAVORITE_LANGUAGE_CHOICES = [
    ('c++', 'C++'),
    ('python', 'Python'),
    ('javascript', 'Javascript'),
]
class contactForm(forms.Form):
    name = forms.CharField(label='Full Name',initial='Your Full Name',min_length=5)
    email = forms.EmailField()
    birth_day_date = forms.DateField(widget= forms.NumberInput(attrs={'type': 'date'}),required=False , initial='Your Email')
    graduation_year = forms.DateField(widget=forms.SelectDateWidget(years= GRADUATION_YEAR_CHOICES),required=False)
    application_time = forms.DateField(initial=datetime.date.today)
    favoriet_color = forms.ChoiceField(widget=forms.RadioSelect,choices=FAVORITE_COLORS_CHOICES,required=False)
    favaroit_programming_language = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_LANGUAGE_CHOICES,required=False)
    agree = forms.BooleanField(label='Agree With turms and conditions')
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}),required=False)