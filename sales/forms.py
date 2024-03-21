from django import forms

# for searching items

CHART_CHOICES = (
                ("#1","Bar"),             
                ("#2","Pie chart"),
                ("#3","Line")
                )


class SalesSearchForm(forms.Form):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    chart_type = forms.ChoiceField(choices =CHART_CHOICES)