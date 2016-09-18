import uuid
from datetime import datetime

from django.db import models


class Lead(models.Model):
    name = models.CharField('nome', max_length=128)
    email = models.EmailField('e-mail', max_length=256)
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    ip_address = models.GenericIPAddressField(protocol='both', unpack_ipv4=True)
    created_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return '{} ({})'.format(self.name, self.email)


# class LeadAnswer(models.Model):
#     lead = models.ForeignKey('Lead', on_delete=models.CASCADE)
#     question = models.ForeignKey('quiz.Question', on_delete=models.CASCADE)
#     lead_answer = models.CharField(max_length=1)
