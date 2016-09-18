import uuid

from django.shortcuts import render


def index(request):
    lead_ip = get_client_ip(request)
    lead_token = uuid.uuid4()

    return render(request, 'lead/index.html', {
        'lead_ip': lead_ip,
        'lead_token': lead_token
    })


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
