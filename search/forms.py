from django import forms


class ExoplanetUploadCSVFileForm(forms.Form):
    file = forms.FileField()
