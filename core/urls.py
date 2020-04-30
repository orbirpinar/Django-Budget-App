from django.urls import path

from .views import home,deleteIncome,deleteExpense,deleteAll

urlpatterns = [
    path('',home,name='home'),
    path('income/<int:id>/delete/',deleteIncome,name="delete_income"),
    path('expense/<int:id>/delete/',deleteExpense,name="delete_expense"),
    path('delete',deleteAll,name="delete_all")
    ]	



# {{ form.category }}
#                         {{ form.name }}
                        # {{form.amount}}