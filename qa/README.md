# Django QA

Проект итоговой работы по дисциплине "Python-разрабочик", ТУСУР, Цифровая академия.
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

# Данные для проверки

В базе данных сохранены две учетные записи пользователей:
- admin: администратор (пароль: Qwerty#123)
- user: пользователь (пароль: Qwerty#123)
<!---->
Также в БД храняться несколько вопросов по темам "Программирование", "Другое", "Администрирование".
<!---->

# Примеры работы приложения

Внешний вид главного окна
![mainpage](https://github.com/internetProhozhij/django_qa/blob/master/qa/screenshots/main.png)

Внешний вид окона регистрации 
![regpage](https://github.com/internetProhozhij/django_qa/blob/master/qa/screenshots/reg.png)

Внешний вид окона авторизации
![authpage](https://github.com/internetProhozhij/django_qa/blob/master/qa/screenshots/auth.png)

Внешний вид окна создания вопроса
![questionpage](https://github.com/internetProhozhij/django_qa/blob/master/qa/screenshots/question.png)

Внешний вид окна ответов
![answerpage](https://github.com/internetProhozhij/django_qa/edit/master/qa/README.md)
