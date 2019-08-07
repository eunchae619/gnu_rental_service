from django import forms
from .models import Portfolio,Comment

class NewBlog(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ('제목', '사진','임대기간','포인트','내용')

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('작성자', '내용','평점')