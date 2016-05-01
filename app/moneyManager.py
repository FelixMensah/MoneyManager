# This Python file uses the following encoding: utf-8

import os
__author__ = 'Felix'


class User:

    def __init__(self,title=None ,first_name=None,last_name=None,age=None,income=None,rent=None,student_loan=None,
                 consumer_loan=None,mortgage_loan=None,food=None,debtreimbursement=None,clothing=None,
                 hobby=None,miscellaneous=None,children=None,contribution_NI=None):
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.income = income
        self.rent = rent
        self.student_loan = student_loan
        self.consumer_loan = consumer_loan
        self.mortgage_loan = mortgage_loan
        self.food = food
        self.debtreimbursement = debtreimbursement
        self.clothing = clothing
        self.hobby = hobby
        self.miscellaneous = miscellaneous
        self.children = children
        self.contribution_NI = contribution_NI

    @staticmethod
    def _valid_name(name):
        return name is None or name.isalpha()
        # this will choke if name isn't None or a string - maybe add more rules?

    @staticmethod
    def _valid_number(number):
        return number is None or number.isnumeric()

    @staticmethod
    def _valid_boolean(boolean):
        return boolean is None or boolean == 'Y' or boolean == 'N' or boolean =='y' or boolean =='n'

    @staticmethod
    def _valid_title(title):
        return title is None or title == 'Ms'or title == 'Mr' or title == 'Sir' or title =='Mrs' \
               or title == 'Dr' or title == 'ms' or title == 'mr' or title == 'sir' or title == 'mrs'\
               or title == 'dr' or title == 'MS' or title == 'MR' or title == 'SIR' or title == 'MRS'\
               or title == 'DR'

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if not self._valid_title(new_title):
            raise ValueError('Invalid title: {!r}'.format(new_title))
        self._title = new_title

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, new_name):
        if not self._valid_name(new_name):
            raise ValueError('Invalid first name: {!r}'.format(new_name))
        self._first_name = new_name


    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, new_name):
        if not self._valid_name(new_name):
            raise ValueError('Invalid last name: {!r}'.format(new_name))
        self._last_name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if not self._valid_number(new_age):
            raise ValueError('Invalid age: {!r}'.format(new_age))
        self._age = new_age

    @property
    def income(self):
        return self._income

    @income.setter
    def income(self, new_income):
        if not self._valid_number(new_income):
            raise ValueError('Invalid income: {!r}'.format(new_income))
        self._income = new_income


    @property
    def rent(self):
        return self._rent

    @rent.setter
    def rent(self, new_rent):
        if not self._valid_number(new_rent):
            raise ValueError('Invalid rent: {!r}'.format(new_rent))
        self._rent = new_rent


    @property
    def student_loan(self):
        return self._student_loan

    @student_loan.setter
    def student_loan(self, new_student_loan):
        if not self._valid_number(new_student_loan):
            raise ValueError('Invalid loan: {!r}'.format(new_student_loan))
        self._student_loan = new_student_loan

    @property
    def consumer_loan(self):
        return self._consumer_loan

    @consumer_loan.setter
    def consumer_loan(self, new_consumer_loan):
        if not self._valid_number(new_consumer_loan):
            raise ValueError('Invalid loan: {!r}'.format(new_consumer_loan))
        self._consumer_loan = new_consumer_loan

    @property
    def mortgage_loan(self):
        return self._mortgage_loan

    @mortgage_loan.setter
    def mortgage_loan(self, new_mortgage_loan):
        if not self._valid_number(new_mortgage_loan):
            raise ValueError('Invalid loan: {!r}'.format(new_mortgage_loan))
        self._mortgage_loan = new_mortgage_loan

    @property
    def food(self):
        return self._food

    @food.setter
    def food(self, new_food):
        if not self._valid_number(new_food):
            raise ValueError('Invalid number: {!r}'.format(new_food))
        self._food = new_food

    @property
    def debtreimbursement(self):
        return self._debtreimbursement

    @debtreimbursement.setter
    def debtreimbursement(self, new_debtreimbursement):
        if not self._valid_number(new_debtreimbursement):
            raise ValueError('Invalid number: {!r}'.format(new_debtreimbursement))
        self._debtreimbursement = new_debtreimbursement

    @property
    def clothing(self):
        return self._clothing

    @clothing.setter
    def clothing(self, new_clothing):
        if not self._valid_number(new_clothing):
            raise ValueError('Invalid input: {!r}'.format(new_clothing))
        self._clothing = new_clothing

    @property
    def hobby(self):
        return self._hobby

    @hobby.setter
    def hobby(self, new_hobby):
        if not self._valid_number(new_hobby):
            raise ValueError('Invalid input: {!r}'.format(new_hobby))
        self._hobby = new_hobby

    @property
    def miscellaneous(self):
        return self._miscellaneous

    @miscellaneous.setter
    def miscellaneous(self, new_miscellaneous):
        if not self._valid_number(new_miscellaneous):
            raise ValueError('Invalid input: {!r}'.format(new_miscellaneous))
        self._miscellaneous = new_miscellaneous

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, new_children):
        if not self._valid_number(new_children):
            raise ValueError('Invalid number: {!r}'.format(new_children))
        self._children = new_children

    @property
    def contribution_NI(self):
        return self._contribution_NI

    @contribution_NI.setter
    def contribution_NI(self, new_contribution_NI):
        if not self._valid_boolean(new_contribution_NI):
            raise ValueError('Invalid value: {!r}'.format(new_contribution_NI))
        self._contribution_NI = new_contribution_NI


    def total_loan_user(self):
        if int(self.student_loan) + int(self.consumer_loan) + int(self.mortgage_loan) - int(self.debtreimbursement) <= 0:
            return 0
        else:
            return int(self.student_loan) + int(self.consumer_loan) + int(self.mortgage_loan) - int(self.debtreimbursement)

    def personalAllowance(self):
     if int(self.age) <= 77:

            if int(self.income) <= 10600:
                return int(self.income)
            elif 10600 < int(self.income) <= 100000:
                return 10600
            elif 100000 < int(self.income) < 121200:
                return round(10600 - ((int(self.income) - 100000) / 2), 2)
            else:
                return 0
     else:
        if int(self.income) <= 10660:
            return int(self.income)
        elif 10600 < int(self.income) <= 27700:
            return 10600
        elif 27700 < int(self.income) <= 27820:
            return round(10660 - ((int(self.income) - 27700) / 2), 2)
        elif 27820 < int(self.income) <= 100000:
            return 10600
        elif 100000 < int(self.income) <= 121200:
            return round(10600 - ((int(self.income) - 100000) / 2), 2)
        else:
            return 0

    def taxpaid(self):
        taxableIncome = (int(self.income) - self.personalAllowance())
        if taxableIncome <= 0:
            return 0
        elif 0 < taxableIncome <= 31785:
            return round(0.2 * taxableIncome, 2)
        elif 31785 < taxableIncome <= 150000:
            return round(0.2 * 31785 + (taxableIncome - 31786) * 0.4, 2)
        else:
            return round(0.2 * 31785 + 0.4 * (150000 - 31785) + (taxableIncome - 150000) * 0.45, 2)

    def national_insurance_contribution(self):
        if int(self.age) > 67 or self.contribution_NI == 'N' or self.contribution_NI == 'n':
            return 0
        elif int(self.income) <= 8060:
            return 0
        elif 8060 < int(self.income) <= 42380:
            return round((int(self.income) - 8060) * 0.12, 2)
        else:
            return round(0.12 * (42380 - 8060) + (int(self.income) - 42380) * 0.02)

    def total_deduction(self):
     return self.national_insurance_contribution() + self.taxpaid()

    def money_leaving_after_tax(self):
        return int(self.income) - self.total_deduction()

    def money_leaving_after_expenses(self):
       if self.money_leaving_after_tax() - (self.children* 3762) - int(self.miscellaneous) - (int(self.hobby)*12)- int(self._clothing) - int(self.food) - (int(self.rent)*52)  - \
                int(self.debtreimbursement)*12 <= 0:
            return 0
       else:
         return self.money_leaving_after_tax() - (self.children* 3762) - int(self.miscellaneous) - (int(self.hobby)*12)- int(self._clothing) - int(self.food) - (int(self.rent)*52) - \
                int(self.debtreimbursement)*12

    def leaving_debt(self):
        return self.total_loan_user() - int(self.debtreimbursement) *12

    def saving(self):
        money_leaving_after_1year = self.money_leaving_after_expenses()
        money_leaving_after_3years = self.money_leaving_after_expenses() * 3
        money_leaving_after_5years = self.money_leaving_after_expenses() * 5
        moneyLeaving = (money_leaving_after_1year,money_leaving_after_3years,money_leaving_after_5years)
        return moneyLeaving

    @classmethod
    def from_input(cls):
        user = cls()
        while True:
            # you could alternatively use cls._valid_name directly here
            try:
                user.title = input('What is your title? Mr/Ms/Mrs/Sir/Dr: ')
            except ValueError:
                print('Please try again.')
            else:
                break

        while True:
            try:
                user.first_name = input('Enter first name: ')
            except ValueError:
                print('Please try again.')
            else:
                break

        while True:
            try:
                user.last_name = input('Enter last name: ')
            except ValueError:
                print('Please try again.')
            else:
                break

        while True:
            try:
                user.age = input('Enter your age: ')
            except ValueError:
                print('Please try again.')
            else:
                break

        while True:
            try:
                user.income = input('Enter your income for this year: ')
            except ValueError:
                print('Please try again.')
            else:
                break
        while True:
            try:
                user.rent = input('How much do you pay per week for your rent?')
            except ValueError:
                print('Please try again.')
            else:
                break

        while True:
            try:
                user.student_loan = input('How much is your student loan?:')
            except ValueError:
                print('Please try again.')
            else:
                break

        while True:
            try:
                user.consumer_loan = input('How much is your consumer loan?:')
            except ValueError:
                print('Please try again.')
            else:
                break

        while True:
            try:
                user.mortgage_loan = input('How much is your mortgage loan?:')
            except ValueError:
                print('Please try again.')
            else:
                break

        while True:
            try:
                user.food = input('Estimate how much you spend per week for your food: ')

            except ValueError:
                print('Please try again.')
            else:
                break

        while True:
            try:
                user.debtreimbursement = input('How much do you pay back per month for your debts? ')
            except ValueError:
                print('Please try again.')
            else:
                break

        while True:
            try:
                user.clothing = input('How much do you spend per year for your clothes? ')
            except ValueError:
                print('Please try again.')
            else:
                break

        while True:
            try:
                user.hobby = input('Estimate how much you spend per month for your hobbies: ')

            except ValueError:
                print('Please try again.')
            else:
                break

        while True:
            try:
                user.miscellaneous = input('Estimate any other expenses during this year: ')
            except ValueError:
                print('Please try again.')
            else:
                break

        while True:
            try:
                user.children = input('How many children do you have?')
            except ValueError:
                print('Please try again.')
            else:
                break

        while True:
            try:
                user.contribution_NI = input('Do you contribute to the NI? Y/N')
            except ValueError:
                print('Please try again.')
            else:
                break


        cwd = os.getcwd()

        my_file = open("C:\\Users\\Félix\\PycharmProjects\\MoneyManager\\src\\output", "r+")

        my_file.write("Money Manager Summary\n\n")

        my_file.write("************Personal information************\n\n")

        my_file.write(user.title + " " + user.first_name + " " + user.last_name + "\n")
        my_file.write( "Age : " + " " + str(user.age) + "\n")
        my_file.write("Number of children : " + str(user.age) + "\n\n")

        my_file.write("***************Tax information**************\n\n")

        my_file.write("Salary : " + u"\u00a3" + str(user.income) + "\n")
        my_file.write("Personal allowance : " + u"\u00a3" + str(user.personalAllowance()) + "\n")
        my_file.write("Tax paid : " + u"\u00a3" + str(user.taxpaid()) + "\n")
        my_file.write("NI contribution : " + u"\u00a3" + str(user.national_insurance_contribution()) + "\n")
        my_file.write("Total deduction : " + u"\u00a3" + str(user.total_deduction()) + "\n")
        my_file.write("You take home : " + u"\u00a3" + str(user.money_leaving_after_tax()) + "\n\n")

        my_file.write("***************Annual expenses**************\n\n")

        my_file.write("Rent : " + u"\u00a3" + str(int(user.rent)* 52) + "\n")
        my_file.write("Food : " + u"\u00a3" + str(user.food) + "\n")
        my_file.write("Hobby : " + u"\u00a3" + str(user.hobby) + "\n")
        my_file.write("Clothing : " + u"\u00a3" + str(user.clothing) + "\n")
        my_file.write("Other : " + u"\u00a3" + str(user.miscellaneous) + "\n\n")

        my_file.write("*********************Debt********************\n\n")

        my_file.write("reimbursement debt : " + u"\u00a3" + str(user.debtreimbursement) + "\n\n")
        my_file.write("Student debt : " + u"\u00a3" + str(user.student_loan) + "\n")
        my_file.write("Consumption debt : " + u"\u00a3" + str(user.consumer_loan) + "\n")
        my_file.write("Mortage debt : " + u"\u00a3" + str(user.mortgage_loan) + "\n\n")
        my_file.write("TOTAL debt : " + u"\u00a3" + str(user.total_loan_user()) + "\n\n")

        my_file.write("********************Saving*******************\n\n")

        

        my_file.close()
        return user
new_user = User.from_input()

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)
print(cwd)

