from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from lead.models import Lead, LeadAnswer
from quiz.models import Question, Choice


def quiz_start(request, token):
    lead = get_object_or_404(Lead, token=token)
    questions = Question.objects.all()
    q_number = 1

    return render(request, 'quiz/quiz_start.html', {
        'lead': lead,
        'questions': questions,
        'q_number': q_number
    })


def quiz_save(request):
    if request.POST:
        lead = get_object_or_404(Lead, token=request.POST.get('token'))
        questions = Question.objects.all()

        for question in questions:
            is_correct = False
            choice = request.POST.get('question-{}'.format(question.id))

            if choice and choice == question.right_option:
                is_correct = True

            LeadAnswer.objects.create(
                lead=lead,
                question=question,
                is_correct=is_correct
            )

        return redirect(reverse('quiz:done',
                        kwargs={'token': str(lead.token)}),
                        permanent=True)


def quiz_done(request, token):
    lead = get_object_or_404(Lead, token=token)
    answers = list(LeadAnswer.objects.filter(lead=lead))
    total_answers = len(answers)
    correct_answers = 0

    for ans in answers:
        if (ans.is_correct):
            correct_answers += 1

    return render(request, 'quiz/quiz_done.html', {
        'lead': lead,
        'total_answers': total_answers,
        'correct_answers': correct_answers

    })
