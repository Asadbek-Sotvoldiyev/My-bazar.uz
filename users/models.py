from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator

CUSTOMER, EMPLOYEE, ADMIN = ('customer', 'employee', 'admin')

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):

    USER_ROLES = (
        (CUSTOMER, CUSTOMER),
        (EMPLOYEE, EMPLOYEE),
        (ADMIN, ADMIN),

    )

    phone_number = models.CharField(max_length=13, null=True, blank=True)
    bio = models.TextField(null=True, blank=True, max_length=255)
    user_role = models.CharField(max_length=30, choices=USER_ROLES, default=CUSTOMER)
    image = models.ImageField(upload_to='users/', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])

    def __str__(self):
        return self.username
