class Human:
    def __init__(self, name):
        self.name = name
        return

    # ответ по умолчанию для всех одинаковый, можно
    # доверить его родительскому классу
    def answer_question(self, question):
        print("Очень интересный вопрос! Не знаю.")
        return

    def __str__(self):
        return self.name


class Student(Human):
    #  метод ask_question() принимает параметр someone:
    #  это объект, экземпляр класса Curator, Mentor или CodeReviewer,
    #  которому Student задаёт вопрос;
    #  параметр question — это просто строка
    #  имя объекта и текст вопроса задаются при вызове метода ask_question
    def ask_question(self, someone, question):
        # напечатайте на экран вопрос в нужном формате
        print(someone.__str__() + ", " + question)
        # запросите ответ на вопрос у someone
        someone.answer_question(question)
        print()  # этот print выводит разделительную пустую строку
        return


class Curator(Human):
    def answer_question(self, question):
        # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
        if question == "мне грустненько, что делать?":
            print("Держись, всё получится. Хочешь видео с котиками?")
        # если да - ответить на него
        else:
            super().answer_question(question)
        # если нет - вызвать метод answer_question() у родительского класса
        return


# объявите и реализуйте классы CodeReviewer и Mentor
class CodeReviewer(Human):
    def answer_question(self, question):
        # здесь нужно проверить, пришёл кодревьюверу знакомый вопрос или нет
        if question == 'что не так с моим проектом?':
            print('О, вопрос про проект, это я люблю.')
        # если да - ответить на него
        else:
            super().answer_question(question)
        # если нет - вызвать метод answer_question() у родительского класса
        return


class Mentor(Human):

    def answer_question(self, question):
        # здесь нужно проверить, пришёл ментору знакомый вопрос или нет
        if question == 'как устроиться работать питонистом?':
            print('Сейчас расскажу.')
        # если да - ответить на него
        else:
            super().answer_question(question)
        # если нет - вызвать метод answer_question() у родительского класса
        return


# следующий код менять не нужно, он работает, мы проверяли
student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')

student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')
