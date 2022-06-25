from django import forms


from webapp.models import Ad


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ('title', 'text', 'photo', 'category', 'price')

