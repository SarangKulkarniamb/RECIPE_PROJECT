from django.contrib import admin
from .models import Recipe,Rating,Membership
# Register your models here.
admin.site.register(Recipe)
admin.site.register(Rating)
admin.site.register(Membership)