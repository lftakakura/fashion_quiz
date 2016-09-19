import uuid
from datetime import datetime

from django.db import models


class Lead(models.Model):
    GENDER_CHOICES = [
        (0, 'Masculino'),
        (1, 'Feminino')
    ]

    name = models.CharField('nome', max_length=128)
    email = models.EmailField('e-mail', max_length=256, unique=True)
    gender = models.PositiveIntegerField('sexo', choices=GENDER_CHOICES, null=True)
    age = models.PositiveIntegerField('idade', null=True)
    accepted_partners = models.BooleanField(default=True)
    ip_address = models.GenericIPAddressField(protocol='both', unpack_ipv4=True)
    created_on = models.DateTimeField(default=datetime.now)
    token = models.UUIDField(default=uuid.uuid4, unique=True)

    def __str__(self):
        return '{} ({})'.format(self.name, self.email)


class LeadAnswer(models.Model):
    lead = models.ForeignKey('Lead', on_delete=models.CASCADE)
    question = models.ForeignKey('quiz.Question', on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return '{} acertou? {}'.format(self.lead.name, self.is_correct)
