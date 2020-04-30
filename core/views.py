from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView,CreateView


from .models import Budget
from .forms import BudgetForm

percentage_list = []  
def home(request):
    if request.method == "POST":
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.save()
            return redirect('home')
    else:
        form = BudgetForm()

    expenses = Budget.objects.filter(category="exp")
    incomes = Budget.objects.filter(category="inc")


    #total income
    total_income = 0
    for value in incomes:
        total_income+=value.amount

     
    #total expense
    total_expense = 0
    for value in expenses:
        total_expense+=value.amount
  


    

    #Available budget
    budget = total_income - total_expense
    

    #All percentages
    if total_income>0:
        percentages = f'{round((total_expense/total_income)*100)}%'
    else:
        percentages = -1




    context = {
        'expenses':expenses,
        'incomes':incomes,
        'total_expense':total_expense,
        'total_income':total_income,
        'budget':budget,
        'form':form,
        'percentages':percentages,
        'percentage_list':percentage_list
    }


    return render(request,'index.html',context)






def deleteExpense(request,id):
    expense = get_object_or_404(Budget,id=id)
    expense.delete()
    return redirect('home')

def deleteIncome(request,id):
    income = get_object_or_404(Budget,id=id)
    income.delete()
    return redirect('home')


def deleteAll(request):
    budget = Budget.objects.all().delete()
    return redirect('home')



