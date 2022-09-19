from django import forms


class SelForm(forms.Form):

    #Especificar los campos
    pais = forms.CharField()
    continente = forms.CharField()


class EstForm(forms.Form):   
    nombre= forms.CharField()
    ciudad= forms.CharField()

class CopForm(forms.Form):   
    selecc= forms.CharField()
    cantCopas= forms.IntegerField()
    ultimaCopa= forms.IntegerField()