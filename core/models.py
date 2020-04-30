from django.db import models
from django.db.models import Sum
from django.db.models import Value
from django.db.models.functions import Coalesce


CATEGORY = (
	('exp','Expense'),
	('inc','Income')

	)

class Budget(models.Model):
    category = models.CharField(choices = CATEGORY,max_length=3,default="inc")
    name = models.CharField(max_length=80)
    amount = models.DecimalField(max_digits=8,decimal_places=2)


    #self expense percentage
    def get_percentage(self):
    	qs = Budget.objects.filter(category="inc")
    	totalIncome = qs.aggregate(the_sum=Coalesce(Sum('amount'),Value(0)))['the_sum']
    	if totalIncome>0:
    		if self.category == "exp":
    			percentage = round((self.amount/totalIncome*100))

    	return percentage


