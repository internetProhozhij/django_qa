from hashlib import sha256
from django.http import HttpRequest
from django.contrib import messages

from core.models import AnswerModel
from core.models import QuestionModel
from core.forms import AnswerForm
from account.models import AccountModel


def get_username(request: HttpRequest) -> str:
    """
    Получение имени пользователя.
    """
    if not request.user:
        return ""
    return request.user.username


def create_record(data: dict, 
                  user_obj: AccountModel, 
                  question_obj: QuestionModel) -> None:
    """
    Создание записи ответа.
    """
    aid = sha256(f"{data['body']}".encode("utf-8")).hexdigest()
    body = data["body"]
    obj = AnswerModel.objects.create(aid=aid,
                                     body=body,
                                     uid=user_obj,
                                     qid=question_obj)
    obj.save()


def build_context(request: HttpRequest, qid: str, aid: str=None) -> dict:
    """
    Формирование контекста страницы ответов на вопрос.
    """
    try:
        question_obj = QuestionModel.objects.get(qid=qid)
        answer_objs = list(AnswerModel.objects.filter(qid=qid))
    except:
        return {}
    
    try:
        answer_obj = AnswerModel.objects.get(aid=aid)
    except:
        answer_obj = None

    aform = AnswerForm(data=answer_obj.__dict__) if answer_obj else AnswerForm()

    if request.method == "POST":
        # Пользователи могу редактировать собственные ответы. Когда пользователь
        # нажимает на кнопку "редактировать", то формируется url следующего вида:
        # domain/question/<quesiton_id>?answer=<answer_id>.
        # Наверно, это костыль. Но другого я придумать не сумел.
        # Так как для идентификации ответа используется хэш, то при редактировании
        # ответа старый удаляется, новый добавляется
        aform = AnswerForm(request.POST)
        if aform.is_valid():
            try:
                create_record(request.POST, request.user, question_obj)
                # Проверка совпадения автора ответа и текущего пользователя нужна,
                # чтобы предотвратить возможность изменения ответа других пользователей
                # методом подбора хэшей. Как же это плохо
                if aid and answer_obj and answer_obj.uid == request.user:
                    answer_obj.delete()
                aform = AnswerForm()
                answer_objs = list(AnswerModel.objects.filter(qid=qid))
            except:
                messages.error(request, message="Ваш ответ повторяет уже существующий.")
    
    return {"question": question_obj, 
            "aform": aform,
            "answers": answer_objs,
            "username": get_username(request)}

