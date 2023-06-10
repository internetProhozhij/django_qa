from django.db import models


# Список тем, на которые можно задавать вопросы.
# Кажды элемент списка представлен кортежем, где 
# первый элемент - название темы в базе данных, а 
# второй элемент - название темы, отображаемое пользователю
THEMES = [("prog", "Программирование"),
          ("admin", "Администрирование"),
          ("music", "Музыка"),
          ("movie", "Кино"),
          ("serial", "Сериалы"),
          ("anime", "Аниме"),
          ("other", "Другое"),]


class QuestionModel(models.Model):
    """
    Таблица с вопросами.
    """
    qid = models.CharField(max_length=256, primary_key=True)
    theme = models.CharField(max_length=256, choices=THEMES, null=False)
    date = models.DateTimeField(auto_now=True)
    header = models.CharField(max_length=140, null=False)
    body = models.TextField(null=False)
    uid = models.ForeignKey(to="account.AccountModel", on_delete=models.CASCADE)


class AnswerModel(models.Model):
    """
    Таблица с ответами.
    """
    aid = models.CharField(max_length=256, primary_key=True)
    date = models.DateTimeField(auto_now=True)
    body = models.TextField(null=False)
    uid = models.ForeignKey(to="account.AccountModel", on_delete=models.CASCADE)
    qid = models.ForeignKey(to="QuestionModel", on_delete=models.CASCADE)

