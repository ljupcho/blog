from django import forms
from models import Comment

class CommentForm(forms.ModelForm):

    def __init__(self, object, *args, **kwargs):
        """Override the default to store the original document
        that comments are embedded in.
        """
        self.object = object
        return super(CommentForm, self).__init__(*args, **kwargs)

    def save(self, *args):
        """Append to the comments list and save the post"""
        self.object.comments.append(self.instance)
        self.object.save()
        return self.object

    class Meta:
        model = Comment
        widgets = {
          'body': forms.Textarea(attrs={'rows':6, 'cols':100}),
        }