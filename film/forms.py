from django.forms import ModelForm,Textarea
from .models import Comments

class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']
        widgets = {
            'comment':Textarea(attrs={
                "style":"border-radius: 10px;outline: none;",
                "cols":"50",
                "rows":"3"
            })
        }