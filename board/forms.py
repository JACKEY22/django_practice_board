from django import forms

class PostWirteForm(forms.Form):
    title = forms.CharField(max_length=128, label='제목', error_messages={'required':'제목을 입력해주세요.'})
    contents = forms.CharField(label='내용', error_messages={'required':'내용을 입력해주세요.'}, widget=forms.Textarea)
    tags = forms.CharField(max_length=32, label='태그', required=False)
