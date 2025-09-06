from django.contrib import admin
from .models import User, Trainer, SubscriptionPlan, Client, Visit

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age')
    search_fields = ('first_name', 'last_name')

@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration_days', 'price')
    search_fields = ('name',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'subscription', 'trainer')
    search_fields = ('first_name', 'last_name', 'phone')
    list_filter = ('subscription', 'trainer')

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('client', 'visited_at')
    list_filter = ('visited_at',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'created_at')
