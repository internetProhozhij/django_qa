# Django QA

Проект итоговой работы по дисциплине "Python-разрабочик", ТУСУР, Цифровая академия.
<!---->

Django QA - веб-приложение вопросов-ответов.
- Каждый авторизованный пользователь может задавать вопросы на любую из доступных категорий,
    а также отвечать на любой вопрос. Также таким пользователям доступна функция редактирования
    собственных ответов.
- Неавторизованные пользователи могут только просматировать вопросы и ответы на них.
- Администратор кроме возможностей авторизованного пользователя может удалять вопросы с сайта.
<!---->

На сайте реализован механизм поиска по:
- категории;
- шапке вопроса;
- категории и шапке вопроса.
<!---->

# Requirenments

- `Python 3.10` или выше
- пакет `Django=4.2.1`
- пакет `markdown=3.4.4`
<!---->

# Структура проекта

```
qa/
 |
 +---> qa/ (каталог с настройками проекта)
 | 
 +---> account/ (каталог приложения авторизации/регистрации)
 |
 +---> core/ (каталог приложения управления вопросами/ответами)
```
<!---->

# Структура базы данных

```

         +===============+
         | Пользователь  |
         +==+============+
   +-----|pk|  username  |----------+
   |     +==+============+          |
   |     |  |  password  |          |
   |     +  +============+          |
   |     |  |   is_god   |          |      +===============+
   |     +  +============+          |      |     Ответ     |
   |     |  | last_login |          |      +===============+
   |     +==+============+          |      |pk|    aid     |
   |                                |      +==+============+
   |                                |      |  |    body    |
   |     +===============+          |      +  +============+
   |     |     Вопрос    |          |      |  |    date    |
   |     +==+============+          |      +==+============+
   |     |pk|    qid     |-----+    +----->|fk|  username  |
   |     +==+============+     |           +==+============+
   |     |  |   theme    |     +---------->|fk|    qid     |
   |     +  +============+                 +==+============+     
   |     |  |   header   |     
   |     +  +============+     
   |     |  |    body    |     
   |     +  +============+     
   |     |  |    date    |     
   |     +==+============+     
   +---->|fk|  username  |     
         +==+============+     

```
<!---->
### Таблица `Пользователь`

- `username`: имя пользователя, используется для авторизации;
- `password`: пароль, хэш;
- `is_god`: флаг администратора (`True`: админ, `False`: простой пользователь);
- `last_login`: дата последней авторизации (Django сам его создал, без использования этого
    поля метод встроенной формы авторизации пользователя `.is_valid()` завершается фатальным
    крахом. Я решил ничего не трогать).
<!---->

### Таблица `Вопрос`

- `qid`: идентификатор, хэш содержимого `body`;
- `theme`: тема;
- `header`: шапка;
- `body`: содержимое;
- `date`: дата создания;
- `username`: идентификатор пользователя, создавшего вопрос.
<!---->

### Таблица `Ответ`

- `aid`: идентификатор, хэш содержимого `body`;
- `body`: содержимое;
- `date`: дата создания;
- `username`: идентификатор пользователя, создавшего ответ;
- `qid`: идентификатор вопроса, которому принадлежит ответ.
<!---->

# Данные для проверки

В базе данных сохранены две учетные записи пользователей:
- `admin`: администратор (пароль: `Qwerty#123`)
- `user`: пользователь (пароль: `Qwerty#123`)
<!---->
Также в БД храняться несколько вопросов по темам "Программирование", "Другое", "Администрирование".
<!---->

# Примеры работы приложения

### Внешний вид главного окна

![mainpage](https://github.com/internetProhozhij/django_qa/blob/master/screenshots/main.png)
<!---->

### Внешний вид окна регистрации 

![regpage](https://github.com/internetProhozhij/django_qa/blob/master/screenshots/reg.png)
<!---->

### Внешний вид окна авторизации

![authpage](https://github.com/internetProhozhij/django_qa/blob/master/screenshots/auth.png)
<!---->

### Внешний вид окна создания вопроса

![questionpage](https://github.com/internetProhozhij/django_qa/blob/master/screenshots/question.png)
<!---->

### Внешний вид окна ответов

![answerpage](https://github.com/internetProhozhij/django_qa/blob/master/screenshots/answer.png)
