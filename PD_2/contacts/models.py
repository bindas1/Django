from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Person(models.Model):
    MAX_HEIGHT = 220
    MIN_HEIGHT = 100

    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_UNSPECIFIED = None
    GENDER_CHOICES = [
        (GENDER_MALE, _('Male')),
        (GENDER_FEMALE, _('Female')),
        (GENDER_UNSPECIFIED, _('Unspecified'))
    ]

    first_name = models.CharField(verbose_name=_("First Name"), max_length = 30)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=30)
    date_of_birth = models.DateField(verbose_name=_("Date of Birth"), blank = True, null = True, default = None)
    pesel = models.PositiveIntegerField(verbose_name=_('PESEL'), help_text=_("Type your PESEL number"), blank = True, null = True, default = None)
    image = models.ImageField(verbose_name=_('Image'), upload_to='image/', blank = True, null = True, default = None)
    homepage = models.URLField(verbose_name=_('Homepage'), blank = True, null = True, default = None)
    notes = models.TextField(verbose_name=_('Notes'), blank = True, null = True, default = None)
    height = models.DecimalField(verbose_name=_('Height'), help_text=_('Please enter height in cm'), max_digits=4, decimal_places=1, validators=[MinValueValidator(MIN_HEIGHT), MaxValueValidator(MAX_HEIGHT)], blank = True, null = True, default = None)
    gender = models.CharField(verbose_name=_('Gender'), max_length=30, choices=GENDER_CHOICES, blank = True, null = True, default = None)
    friends = models.ManyToManyField(verbose_name=_('Friends'), to='contacts.Person', blank=True, default = None)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('People')


class Address(models.Model):

    ADDRESS_WORK = 'work'
    ADDRESS_HOME = 'home'
    ADDRESS_OTHER = 'other'
    ADDRESS_UNSPECIFIED = None

    ADDRESS_CHOICES = [
        (ADDRESS_WORK, _('work')),
        (ADDRESS_HOME, _('home')),
        (ADDRESS_OTHER, _('other')),
        (ADDRESS_UNSPECIFIED, None)
    ]

    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.CharField(verbose_name=_("Address's role"), max_length=30, choices=ADDRESS_CHOICES, blank=True, null=True, default=None)
    street = models.CharField(verbose_name=_("Street"), max_length=30)
    # street number may contain letters
    number = models.CharField(verbose_name=_("Street number"), max_length=60)
    flat_number = models.PositiveIntegerField(verbose_name=_('flat_number'), blank=True, null=True, default=None)
    postal_code = models.CharField(verbose_name=_("Postal code"), max_length=10)
    city = models.CharField(verbose_name=_("City"), max_length=60)
    country = models.CharField(verbose_name=_("Country"), max_length=60)

    def __str__(self) -> str:
        return f'{self.address}'

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')


class PhoneNumber(models.Model):

    PHONE_WORK = 'work'
    PHONE_HOME = 'home'
    PHONE_MOBILE = 'mobile'
    PHONE_OTHER = 'other'
    PHONE_UNSPECIFIED = None

    PHONE_CHOICES = [
        (PHONE_WORK, _('work')),
        (PHONE_HOME, _('home')),
        (PHONE_MOBILE, _('mobile')),
        (PHONE_OTHER, _('other')),
        (PHONE_UNSPECIFIED, None)
    ]

    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.CharField(verbose_name=_("Phone number's role"), max_length=30, choices=PHONE_CHOICES, blank=True, null=True, default=None)
    phone = models.CharField(verbose_name=_("Phone number"), max_length=60)

    def __str__(self) -> str:
        return f'{self.phone}'

    class Meta:
        verbose_name = _('Phone number')
        verbose_name_plural = _('Phone numbers')


class EmailField(models.Model):

    EMAIL_WORK = 'work'
    EMAIL_HOME = 'home'
    EMAIL_OTHER = 'other'
    EMAIL_UNSPECIFIED = None

    EMAIL_CHOICES = [
        (EMAIL_WORK, _('work')),
        (EMAIL_HOME, _('home')),
        (EMAIL_OTHER, _('other')),
        (EMAIL_UNSPECIFIED, None)
    ]

    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.CharField(verbose_name=_("Email's role"), max_length=30, choices=EMAIL_CHOICES, blank=True, null=True, default=None)
    email = models.CharField(verbose_name=_("Email"), max_length=60)

    def __str__(self) -> str:
        return f'{self.email}'

    class Meta:
        verbose_name = _('Email')
        verbose_name_plural = _('Emails')
