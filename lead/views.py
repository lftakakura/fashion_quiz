# coding=utf-8

from django.shortcuts import redirect, render
from django.urls import reverse

from lead.models import Lead


def index(request):
    lead_ip = get_client_ip(request)

    return render(request, 'lead/index.html', {
        'lead_ip': lead_ip
    })


def lead_create(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        accepted_partners = request.POST.get('accept-partners')
        ip_address = request.POST.get('ip')

        if accepted_partners is None:
            accepted_partners = False

        if name and email and gender and age is not None:
            lead = Lead.objects.create(
                name=name,
                email=email,
                age=age,
                gender=gender,
                ip_address=ip_address,
                accepted_partners=accepted_partners
            )

            lead.save()

            return redirect(reverse('quiz:start',
                            kwargs={'token': str(lead.token)}),
                            permanent=True)
        else:
            # TODO: Redirecionar para páginas de erro
            return redirect(reverse('lead:index', permanent=True))


def get_client_ip(request):
    """
    Função que pega o IP do cliente que está fazendo a requisição.
    """

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip
