# Imports from django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

# Imports from foreign installed apps

# Imports from local apps

# Start of Models
class User(AbstractUser):

    def __str__(self):
        return self.username

class AccountDetails(models.Model):
    class Meta:
        verbose_name = "Account Details"
        verbose_name_plural = "Account Details"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    address_1 = models.CharField(
        verbose_name="Address",
        max_length=100,
        blank=False
    )

    address_2 = models.CharField(
        max_length=100,
        blank=False
    )

    postal_code = models.CharField(
        verbose_name="Postal Code",
        max_length=10,
        blank=False
    )

    email = models.CharField(
        verbose_name="Email Address",
        max_length=100,
        blank=False
    )

    phone = models.CharField(
        verbose_name="Phone Number",
        max_length=25,
        blank=False
    )

class OperatingHours(models.Model):
    MONDAY = 'MO'
    TUESDAY = 'TU'
    WEDNESDAY = 'WE'
    THURSDAY = 'TH'
    FRIDAY = 'FR'
    SATURDAY = 'SA'
    SUNDAY = 'SU'
    PUBLIC_HOLIDAYS = 'PH'

    DAY_CHOICES = (
        (MONDAY, _('Monday')),
        (TUESDAY, _('Tuesday')),
        (WEDNESDAY, _('Wednesday')),
        (THURSDAY, _('Thursday')),
        (FRIDAY, _('Friday')),
        (SATURDAY, _('Saturday')),
        (SUNDAY, _('Sunday')),
        (PUBLIC_HOLIDAYS, _('Public Holidays')),
    )

    TIME_CHOICES = (
        (0, _('12am')),
        (1, _('1230am')),
        (2, _('1am')),
        (3, _('130am')),
        (4, _('2am')),
        (5, _('230am')),
        (6, _('3am')),
        (7, _('330am')),
        (8, _('4am')),
        (9, _('430am')),
        (10, _('5am')),
        (11, _('530am')),
        (12, _('6am')),
        (13, _('630am')),
        (14, _('7am')),
        (15, _('730am')),
        (16, _('8am')),
        (17, _('830am')),
        (18, _('9am')),
        (19, _('930am')),
        (20, _('10am')),
        (21, _('1030am')),
        (22, _('11am')),
        (23, _('1130am')),
        (24, _('12pm')),
        (25, _('1230pm')),
        (26, _('1pmam')),
        (27, _('130pm')),
        (28, _('2pm')),
        (29, _('230pm')),
        (30, _('3pm')),
        (31, _('330pm')),
        (32, _('4pm')),
        (33, _('430pm')),
        (34, _('5pm')),
        (35, _('530pm')),
        (36, _('6pm')),
        (37, _('630pm')),
        (38, _('7pm')),
        (39, _('730pm')),
        (40, _('8pm')),
        (41, _('830pm')),
        (42, _('9pm')),
        (43, _('930pm')),
        (44, _('10pm')),
        (45, _('1030pm')),
        (46, _('11pm')),
        (47, _('1130pm'))
    )

    class Meta:
        verbose_name = "Operating Hours"
        verbose_name_plural = "Operating Hours"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    day = models.CharField(
        max_length=2,
        choices=DAY_CHOICES
    )

    open = models.BooleanField(
        default=True
    )

    opening_time = models.CharField(
        max_length=4,
        choices=TIME_CHOICES
    )

    closing_time = models.CharField(
        max_length=4,
        choices=TIME_CHOICES
    )
