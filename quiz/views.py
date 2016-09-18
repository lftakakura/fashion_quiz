from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from lead.models import Lead
from quiz.models import Question, Choice


def quiz_start(request, token):
    lead = get_object_or_404(Lead, token=token)
    questions = Question.objects.all()

    return render(request, 'quiz/quiz_start.html', {
        'lead': lead,
        'questions': questions
    })


def quiz_save(request):
    if request.POST:
        token = request.POST.get('token')
        lead = get_object_or_404(Lead, token=token)

        # TODO fazer save

        return redirect(reverse('quiz:done',
                        kwargs={'token': str(lead.token)}),
                        permanent=True)


def quiz_done(request, token):
    lead = get_object_or_404(Lead, token=token)

    return render(request, 'quiz/quiz_done.html', {
        'lead': lead
    })
