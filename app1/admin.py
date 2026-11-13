from django.contrib import admin

# Register your models here.
from app1.models import emp_table
class emp_admin(admin.ModelAdmin):
    list_display=['pin','name','salary','email','department']
    ordering=['pin']
    list_filter=['department']
admin.site.register(emp_table,emp_admin)
    