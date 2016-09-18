from django.shortcuts import get_object_or_404, redirect, render

from lead.models import Lead


def save_lead(request):
    if request.POST:
        name = request.POST.get('name')
        token = request.POST.get('token')
        accepted_partners = True

        if request.POST.get('accept-partners') is None:
            accepted_partners = False

        lead = Lead.objects.create(
            name=name,
            email=request.POST.get('email'),
            token=token,
            ip_address=request.POST.get('ip'),
            accepted_partners=accepted_partners
        )

        lead.save()

        return redirect(lead.get_absolute_url(), permanent=True)


def index(request, token):
    lead = get_object_or_404(Lead, token=token)

    return render(request, 'quiz/index.html', {
        'name': lead.name
    })
