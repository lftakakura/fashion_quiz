from django.db import models


class Question(models.Model):
    question_title = models.TextField('pergunta')
    right_option = models.CharField(max_length=1)

    def __str__(self):
        return '{} - Resposta: {}'.format(self.question_title, self.right_option)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_letter = models.CharField(max_length=1)
    choice_text = models.CharField(max_length=256)

    def __str__(self):
        return '{} - Resposta: {}: {}'.format(
            self.question.question_title, self.choice_letter, self.choice_text
        )
