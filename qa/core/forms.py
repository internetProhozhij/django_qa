from copy import deepcopy
from django import forms

from .models import QuestionModel
from .models import AnswerModel
from .models import THEMES


LOCAL_THEMES = deepcopy(THEMES)
LOCAL_THEMES.insert(0, ("all", "Все"))


class QuestionForm(forms.ModelForm):
    """
    Форма создания вопроса.
    """
    theme = forms.ChoiceField(choices=THEMES,
                              widget=forms.Select(attrs={"class": "btn btn-primary d-flex mb-3"}))

    header = forms.CharField(required=True,
                             label="",
                             strip=True,
                             widget=forms.TextInput(attrs={"class": "d-flex mb-3",
                                                           "placeholder": "Шапка вопроса"}))

    class Meta:
        model = QuestionModel
        fields = ["theme", "header", "body"]


class AnswerForm(forms.ModelForm):
    """
    Форма создания ответа.
    """
    class Meta:
        model = AnswerModel
        fields = ["body"]


class SearchForm(forms.Form):
    """
    Форма поиска вопроса.
    """
    theme = forms.ChoiceField(choices=LOCAL_THEMES,
                              label="",
                              widget=forms.Select(attrs={"class": "btn btn-primary mr-1"}))
    
    # Поиск может выполняться как по теме, так и по шапке вопроса. Поэтому
    # поле textinput не обязательно к заполнению
    textinput = forms.CharField(required=False, 
                                label="",
                                widget=forms.TextInput(attrs={"class": "d-flex mr-1",
                                                              "style": "width: 60%;"}))

