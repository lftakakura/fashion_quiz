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
        accepted_partners = True

        if request.POST.get('accept-partners') is None:
            accepted_partners = False

        lead = Lead.objects.create(
            name=name,
            email=request.POST.get('email'),
            ip_address=request.POST.get('ip'),
            accepted_partners=accepted_partners
        )

        lead.save()

        return redirect(reverse('quiz:start',
                        kwargs={'token': str(lead.token)}),
                        permanent=True)


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
