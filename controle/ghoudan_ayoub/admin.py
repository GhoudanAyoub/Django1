from django.contrib import admin

# Register your admin here.
from .models import Compte, Operation, Client


@admin.register(Client)
class ClientAd(admin.ModelAdmin):
    pass

@admin.register(Compte)
class CompteAdm(admin.ModelAdmin):
    pass

@admin.register(Operation)
class OperationAdm(admin.ModelAdmin):
    pass