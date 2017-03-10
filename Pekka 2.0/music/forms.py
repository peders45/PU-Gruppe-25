from django import forms
from django.forms import ModelForm
from django.forms import inlineformset_factory
from django.contrib.auth.models import User

from .models import *


class QuestionForm(forms.ModelForm):

    question_content = forms.CharField(widget=forms.Textarea(attrs={'cols':30, 'rows': 10}), label='')

    class Meta:
        model = Question
        fields = ('question_title', 'question_content')


class QuestionVotesForm(forms.ModelForm):
    voteOn = forms.BooleanField(widget=forms.CheckboxInput())

    class Meta:
        model = QuestionVotes
        fields = ()

# la stå
# class CommentVotesForm(models.ModelForm):
#    voteOn = forms.BooleanField(widget=forms.CheckboxInput(default=False))
#
#    class Meta:
#        model=CommentVotes


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['artist', 'album_title', 'genre', 'album_logo']


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['song_title', 'audio_file']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
