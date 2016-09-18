from django.shortcuts import render

from lead.models import Lead


def index(request):
    if request.POST:
        name = request.POST.get('name')

        Lead.objects.create(
            name=name,
            email=request.POST.get('email'),
            token=request.POST.get('token'),
            ip_address=request.POST.get('ip')
        )

    return render(request, 'quiz/index.html', {
        'name': name,
    })
