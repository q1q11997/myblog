from django import forms
class LeaveMsgForm(forms.Form):
    
    msg = forms.CharField(label='留言',widget=forms.Textarea(attrs={'class':'form-control'}))