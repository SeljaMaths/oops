#single inheritance
from datetime import datetime


class Person:
    def __init__(self,name,month,year,date):
        self.n = name
        self.m = month
        self.y= year
        self.d = date


class Age(Person):
    def __init__(self, name,month,year,date):
        Person.__init__(self,name,month,year,date)

    def age_calculation(self):
        current_time = datetime.now()
        current_year = current_time.year
        current_date = current_time.date()
        current_month = current_time.month

        return current_year

    def my_age_calculate(self):
        a= self.age_calculation()
        age = a-self.y
        return f'i am {self.n}. Now, i am {age} years old'


name = input('enter the name:')
month = input('enter the month:')
year = int(input('enter the year:'))
date = int(input('enter the date:'))


obj = Age(name,month,year,date)
x = obj.my_age_calculate()
print(x)

