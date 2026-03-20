from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Customer, CustomerAddress



# Register your models here.

@admin.register(User)
class custormerAdmin(UserAdmin):
    models = User
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_active', 'is_staff')
    ordering = ('email',)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("phone", "created_at", "updated_at")}),
    )
    readonly_fields = ("created_at", "updated_at")


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'user', 'loyalty_points', 'created_at')
    
@admin.register(CustomerAddress)
class CustomerAddressAdmin(admin.ModelAdmin):
    list_display = ('address_id', 'customer', 'label', 'address_type', 'is_default', 'city', 'country')
