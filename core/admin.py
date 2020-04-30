from django.contrib import admin
from .models import Budget



class BudgetAdmmin(admin.ModelAdmin):
    list_display = ('name','amount','category')

    class Meta:
        model = Budget 




admin.site.register(Budget,BudgetAdmmin)



