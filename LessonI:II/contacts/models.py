from django.db import models
from django.utils.translation import gettext_lazy as _

class Persons(models.Model):

    GENDER_MALE = 'Male'
    GENDER_FEMALE = 'Female'
    GENDER_UNDEFINED = None

    GENDER_CHOICES = [
        (GENDER_MALE, _('Male')),
        (GENDER_FEMALE, _('Female')),
        (GENDER_UNDEFINED, _('Undefined'))
    ]

    first_name = models.CharField(verbose_name=_("First name"), max_length=30)
    last_name = models.CharField(verbose_name=_("Last name"), max_length=30)
    day_of_birth = models.DateField(verbose_name=_('Date of Birth'), null=True, blank=True, default=None)
    image = models.ImageField(verbose_name=_('Image'), upload_to='images/', null=True, blank=True, default=None)
    pesel = models.PositiveIntegerField(verbose_name=_('PESEL'), null=True, blank=True, default=None)
    gender = models.CharField(verbose_name=_('Gender'), max_length=30, choices=GENDER_CHOICES, null=True, blank=True, default=GENDER_UNDEFINED)
    friend = models.ManyToManyField(verbose_name=_('Friend'), to='contacts.Persons', blank=True, default=None)

    def __str__(self) -> str:
        return f'{self.first_name}{self.last_name}'

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('People')
