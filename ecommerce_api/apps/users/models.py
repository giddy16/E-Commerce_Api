from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Q


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def save(self, *args, **kwargs):
        if self.email:
            self.email = self.email.lower()
        super().save(*args, **kwargs)


    def __str__(self):
        return self.email
    
class Customer(models.Model):
        customer_id = models.AutoField(primary_key=True)
        user = models.OneToOneField(
            User,
            on_delete=models.CASCADE,
            related_name='customer_profile'
        )
        loyalty_points = models.PositiveBigIntegerField(default=0)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        class Meta:
             ordering = ['-created_at']

        def __str__(self):
            return f"customer_{self.user.email}"
        
class CustomerAddress(models.Model):
    ADDRESS_TYPE_CHOICES = [
        ('shipping', 'Shipping'),   
        ('billing', 'Billing'),
        ]
    
    address_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='addresses'
    )
    label = models.CharField(max_length=50, null=True, blank=True)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address_type = models.CharField(max_length=20, choices=ADDRESS_TYPE_CHOICES)


    class Meta:
        ordering = ['-created_at']

        constraints = [
            models.UniqueConstraint(
                fields=['customer', 'is_default'],
                condition=Q(is_default=True),
                name='unique_default_address_per_customer'
            )
        ]

    def __str__(self):
        return f"{self.customer.user.email}_{self.address_id}"