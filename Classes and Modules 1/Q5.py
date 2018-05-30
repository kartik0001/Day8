# Q5.

class Expenditure:
    ''' Class to add and calculate expenditure'''

    def __init__(self):
        self.salary=200000
        self.savings=50000
        self.category='a'
        self.totalexpenditure=20000

    def AddExpenditure(self):
        if self.category=='a':
            self.expenditure=36000
        elif self.category=='b':
            self.expenditure=30000.0

    def CalcTotalExp(self):
        self.totalexpenditure+=self.expenditure

    def CalcPerDayAndMonthlyExp(self):
        self.perDayExp=self.totalexpenditure/365
        self.monthlyExp=self.totalexpenditure/12


    def Display(self):
        print("Salary Is:",self.salary)
        print("Savings Is:",self.savings)
        print("Category",self.category)
        print("Expenditure",self.expenditure)
        print("Total Expenditure Is:",self.totalexpenditure)
        print("Per Month Expenditure Is:",self.monthlyExp)
        print("Daily Expenditure Is:",self.perDayExp)

e=Expenditure()
e.AddExpenditure()
e.CalcTotalExp()
e.CalcPerDayAndMonthlyExp()
e.Display()

'''
OUTPUT:
Salary Is: 200000
Savings Is: 50000
Category a
Expenditure 36000
Total Expenditure Is: 56000
Per Month Expenditure Is: 4666.666666666667
Daily Expenditure Is: 153.42465753424656

'''