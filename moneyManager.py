from datetime import date
import os
import calendar

__author__ = 'Felix'


def title():
    while AssertionError:
        titleuser = input("What is your title? : Mr, Mrs, Ms")
        titleuser = titleuser.capitalize()
        if titleuser == 'Mr' or titleuser == 'Mrs' or titleuser == 'Ms':
            return titleuser
            break
        try:
            assert (titleuser == 'Mr' or titleuser == 'Mrs' or titleuser == 'Ms')
        except AssertionError:
            print('You have to choose between Mr, Mrs and Ms.')


def firstname():
    while AssertionError:
        try:
            firstnameuser = input("What is your firstname?")
            firstnameuser = firstnameuser.capitalize()
            assert (firstnameuser.isalpha())
            return firstnameuser
        except AssertionError:
            print('You have to enter a proper firstname.')


def surname():
    while AssertionError:
        surnameuser = input("What is your surname?")
        surnameuser = surnameuser.upper()
        if surnameuser.isalpha():
            return surnameuser
            break
        try:
            assert (surnameuser.isalpha())
        except AssertionError:
            print('You have to enter a proper surname.')


def age():
    while AssertionError:
        try:
            year = input('Enter your year of birth : YYYY')
            month = input('Enter your month of birth : MM')
            day = input('Enter your day of birth : DD')

            assert (year.isnumeric() and len(year) == 4)
            assert (not (not month.isnumeric() or not (1 <= len(month) <= 2)) and 1 <= int(month) <= 12)
            assert (not (not day.isnumeric() or not (1 <= len(day) <= 2)) and 1 <= int(day) <= 31)

            assert (int(year) <= date.today().year)
            age = date.today().year - int(year)
            year = int(year)
            month = int(month)
            day = int(day)
            dob = (age, year, month, day)
            return dob

        except AssertionError:
            print('You have to enter a proper date of birth: YYYY-MM-DD.')


def income():
    while AssertionError:
        try:
            salaryfrequency = input(
                'Do you want to enter your salary per year, pear month or per week ? Enter Y, M or W.')
            salaryfrequency = salaryfrequency.upper()
            assert (salaryfrequency == 'Y' or salaryfrequency == 'W' or salaryfrequency == 'M')
            if salaryfrequency == 'W':
                while AssertionError:
                    try:
                        wageweek = input('How much do you earn per week?')
                        assert (wageweek.isnumeric())
                        return int(wageweek) * 52
                    except AssertionError:
                        print('Enter a numeric input.')
            elif salaryfrequency == 'M':
                while AssertionError:
                    try:
                        wagemonth = input('How much do you earn per month?')
                        assert (wagemonth.isnumeric())
                        return int(wagemonth) * 12
                    except AssertionError:
                        print('Enter a numeric input.')
            else:
                while AssertionError:
                    try:
                        wageyear = input('How much do you earn per year?')
                        assert (wageyear.isnumeric())
                        return int(wageyear)
                    except AssertionError:
                        print('Enter a numeric input.')

        except AssertionError:
            print('Paid weekly -> W : Paid monthly -> M : Paid Yearly -> Y')


def rent():
    while AssertionError:
        try:
            rentfrequency = input('Do you pay your rent weekly or monthly? Enter W or M.')
            rentfrequency = rentfrequency.upper()
            assert (rentfrequency == 'W' or rentfrequency == 'M')
            if rentfrequency == 'W':
                while AssertionError:
                    try:
                        rentweek = input('How much do you pay per week?')
                        assert (rentweek.isnumeric())
                        return int(rentweek) * 52
                    except AssertionError:
                        print('Enter a numeric input.')
            elif rentfrequency == 'M':
                while AssertionError:
                    try:
                        rentmonth = input('How much do you pay per month?')
                        assert (rentmonth.isnumeric())
                        return int(rentmonth) * 12
                    except AssertionError:
                        print('Enter a numeric input.')
        except AssertionError:
            print('Paid weekly -> W or Paid monthly -> M.')


def studentloan():
    while AssertionError:
        try:
            studentloan = input('Do you have a student loan? Y/N')
            studentloan = studentloan.upper()
            assert (studentloan == 'Y' or studentloan == 'N')
            if studentloan == 'N':
                studentloanuser = 0
                return studentloanuser
            else:
                while AssertionError:
                    try:
                        studentloanuser = input('How much is your student loan?')
                        assert (studentloanuser.isnumeric())
                        return int(studentloanuser)
                    except AssertionError:
                        print('Enter a numeric input.')
        except AssertionError:
            print('You have to choose between Yes or No: Y/N ')


def consumerloan():
    while AssertionError:
        try:
            consumerloan = input('Do you have a consumer loan? Y/N')
            consumerloan = consumerloan.upper()
            assert (consumerloan == 'Y' or consumerloan == 'N')

            if consumerloan == 'N':
                consumerloanuser = 0
                return consumerloanuser
            else:
                while AssertionError:
                    try:
                        consumerloanuser = input('How much is your consumer loan?')
                        assert (consumerloanuser.isnumeric())
                        return int(consumerloanuser)
                    except AssertionError:
                        print('Enter a numeric input.')
        except AssertionError:
            print('You have to choose between Yes or No: Y/N ')


def mortgageloan():
    while AssertionError:
        try:
            mortgageloan = input('Do you have a mortgage loan? Y/N')
            mortgageloan = mortgageloan.upper()
            assert (mortgageloan == 'Y' or mortgageloan == 'N')
            if mortgageloan == 'N':
                mortgageloanuser = 0
                return mortgageloanuser
            else:
                while AssertionError:
                    try:
                        mortgageloanuser = input('How much is your mortgage loan?')
                        assert (mortgageloanuser.isnumeric())
                        return int(mortgageloanuser)
                    except AssertionError:
                        print('Enter a numeric input.')
        except AssertionError:
            print('You have to choose between Yes or No: Y/N ')


def food():
    while AssertionError:
        try:
            fooduser = input('How much do yo spend per week for your food?')
            assert (fooduser.isnumeric())
            return int(fooduser) * 52
        except AssertionError:
            print('Enter a numeric input.')


def debtreimbursement():
    while AssertionError:
        try:
            debtreimbursemenuser = input('How much do you payback per month for your loans?')
            assert (debtreimbursemenuser.isnumeric())
            return int(debtreimbursemenuser) * 12
        except AssertionError:
            print('Enter a numeric input.')


def clothing():
    while AssertionError:
        try:
            clothinguser = input('Estimate how much you pay per year for your clothes.')
            assert (clothinguser.isnumeric())
            return int(clothinguser)
        except AssertionError:
            print('Enter a numeric input.')


def hobby():
    while AssertionError:
        try:
            hobbyuser = input('Give an estimation of how much you pay per month for your hobbies.')
            assert (hobbyuser.isnumeric())
            return int(hobbyuser) * 12
        except AssertionError:
            print('Enter a numeric input.')


def miscellaneous():
    while AssertionError:
        try:
            miscellaneoususer = input('Estimate any other expenses during this year.')
            assert (miscellaneoususer.isnumeric())
            return int(miscellaneoususer)
        except AssertionError:
            print('Enter a numeric input.')


def childrenNumber():
    print('The average cost of raising a child in the UK is ' + u"\u00a3" + '3762.')
    while AssertionError:
        try:
            childrenuser = input('How many chidren do you have?')
            assert (childrenuser.isnumeric())
            childrenCost = int(childrenuser) * 3762
            childrenuser = int(childrenuser)
            childrenTotal = (childrenuser, childrenCost)
            return childrenTotal
        except AssertionError:
            print('Enter a numeric input.')


def contributionNI():
    while AssertionError:
        try:
            contributionuser = input('Do you contribute to the National Insurance?Y/N.')
            contributionuser = contributionuser.upper()
            assert (contributionuser == 'Y' or contributionuser == 'N')
            if contributionuser == 'Y':
                return True
            else:
                return False
        except AssertionError:
            print('Enter \'Y\' for Yes or \'N\' for no.')


print('Welcome to the Money Manager !\n')
print('The Money Manager application will help you estimate your tax and your savings.\n')

titleUser = title()
firstnameUser = firstname()
surnameUser = surname()

ageDobUser = age()
ageUser = ageDobUser[0]
yearUser = ageDobUser[1]
monthUser = ageDobUser[2]
dayUser = ageDobUser[3]
childrenUser = childrenNumber()
childrennumberUser = childrenUser[0]
childrencostUser = childrenUser[1]
contributionNIUser = contributionNI()
incomeUser = income()
rentUser = rent()
studentloanUser = studentloan()
consumerloanUser = consumerloan()
mortgageloanUser = mortgageloan()
debtreimbursementUser = debtreimbursement()
totalloanUser = studentloanUser + consumerloanUser + mortgageloanUser - debtreimbursementUser
foodUser = food()
clothingUser = clothing()
hobbyUser = hobby()
miscellaneousUser = miscellaneous()


def totalloanUser(studentloanUser, consumerloanUser, mortgageloanUser, debtreimbursementUser):
    if studentloanUser + consumerloanUser + mortgageloanUser - debtreimbursementUser <= 0:
        return 0
    else:
        return studentloanUser + consumerloanUser + mortgageloanUser - debtreimbursementUser


totalloanUser = totalloanUser(studentloanUser, consumerloanUser, mortgageloanUser, debtreimbursementUser)


def personalAllowance(ageUser, incomeUser):
    if ageUser <= 77:
        if incomeUser <= 10600:
            return incomeUser
        elif 10600 < incomeUser <= 100000:
            return 10600
        elif 100000 < incomeUser < 121200:
            return round(10600 - ((incomeUser - 100000) / 2), 2)
        else:
            return 0
    else:
        if incomeUser <= 10660:
            return incomeUser
        elif 10600 < incomeUser <= 27700:
            return 10600
        elif 27700 < incomeUser <= 27820:
            return round(10660 - ((incomeUser - 27700) / 2), 2)
        elif 27820 < incomeUser <= 100000:
            return 10600
        elif 100000 < incomeUser <= 121200:
            return round(10600 - ((incomeUser - 100000) / 2), 2)
        else:
            return 0


personalAllowanceUser = personalAllowance(ageUser, incomeUser)


def taxpaid(personalAllowanceUser, incomeUser):
    taxableIncome = (incomeUser - personalAllowanceUser)
    if taxableIncome <= 0:
        return 0
    elif 0 < taxableIncome <= 31785:
        return round(0.2 * taxableIncome, 2)
    elif 31785 < taxableIncome <= 150000:
        return round(0.2 * 31785 + (taxableIncome - 31786) * 0.4, 2)
    else:
        return round(0.2 * 31785 + 0.4 * (150000 - 31785) + (taxableIncome - 150000) * 0.45, 2)


taxpaidUser = taxpaid(personalAllowanceUser, incomeUser)


def nationalInsuranceContribution(contributionNIUser, ageUser, incomeUser):
    if ageUser > 67 or contributionNIUser == False:
        return 0
    elif incomeUser <= 8060:
        return 0
    elif 8060 < incomeUser <= 42380:
        return round((incomeUser - 8060) * 0.12, 2)
    else:
        return round(0.12 * (42380 - 8060) + (incomeUser - 42380) * 0.02)


nationalInsuranceContribution = nationalInsuranceContribution(contributionNIUser, ageUser, incomeUser)


def totalDeduction(nationalInsuranceContribution, taxpaidUser):
    return nationalInsuranceContribution + taxpaidUser


totalDeductionUser = totalDeduction(nationalInsuranceContribution, taxpaidUser)


def moneyLeavingAfterTax(totalDeductionUser, incomeUser):
    return incomeUser - totalDeductionUser


moneyLeavingAfterTaxUser = moneyLeavingAfterTax(totalDeductionUser, incomeUser)


def moneyLeavingAfterExpenses(moneyLeavingAfterTaxUser, childrencostUser, miscellaneousUser, hobbyUser, clothingUser,
                              foodUser, rentUser, debtreimbursementUser):
    if moneyLeavingAfterTaxUser - childrencostUser - miscellaneousUser - hobbyUser - clothingUser - foodUser - rentUser - debtreimbursementUser <= 0:
        return 0
    else:
        return moneyLeavingAfterTaxUser - childrencostUser - miscellaneousUser - hobbyUser - clothingUser - foodUser - rentUser - debtreimbursementUser


moneyLeavingAfterExpenses = moneyLeavingAfterExpenses(moneyLeavingAfterTaxUser, childrencostUser, miscellaneousUser,
                                                      hobbyUser, clothingUser, foodUser, rentUser,
                                                      debtreimbursementUser)


def leavingDebt(totalloanUser, debtreimbursementUser):
    return totalloanUser - debtreimbursementUser


leavingDebtUser = leavingDebt(totalloanUser, debtreimbursementUser)


def saving(moneyLeavingAfterExpenses):
    moneyLeavingAfterExpenses1year = moneyLeavingAfterExpenses
    moneyLeavingAfterExpenses3years = moneyLeavingAfterExpenses * 3
    moneyLeavingAfterExpenses5years = moneyLeavingAfterExpenses * 5
    moneyLeaving = (moneyLeavingAfterExpenses1year, moneyLeavingAfterExpenses3years, moneyLeavingAfterExpenses5years)
    return moneyLeaving


savingUser = saving(moneyLeavingAfterExpenses)

saving1year = round(savingUser[0], 2)
saving3years = round(savingUser[1], 2)
saving5years = round(savingUser[2], 2)


# print(os.getcwd())

my_file = open("C:\\Users\\Félix\\PycharmProjects\\MoneyManager\\src\\output", "r+")

my_file.write("Money Manager Summary\n\n")

my_file.write("************Personal information************\n\n")

my_file.write(titleUser + " " + firstnameUser + " " + surnameUser + "\n")
my_file.write(
    "Date of birth : " + str(dayUser) + " " + str(calendar.month_name[int(monthUser)]) + " " + str(yearUser) + "\n")
my_file.write("Number of children : " + str(childrennumberUser) + "\n\n")

my_file.write("***************Tax information**************\n\n")

my_file.write("Salary : " + u"\u00a3" + str(incomeUser) + "\n")
my_file.write("Personal allowance : " + u"\u00a3" + str(personalAllowanceUser) + "\n")
my_file.write("Tax paid : " + u"\u00a3" + str(taxpaidUser) + "\n")
my_file.write("NI contribution : " + u"\u00a3" + str(nationalInsuranceContribution) + "\n")
my_file.write("Total deduction : " + u"\u00a3" + str(totalDeductionUser) + "\n")
my_file.write("You take home : " + u"\u00a3" + str(moneyLeavingAfterTaxUser) + "\n\n")

my_file.write("***************Annual expenses**************\n\n")

my_file.write("Rent : " + u"\u00a3" + str(rentUser) + "\n")
my_file.write("Food : " + u"\u00a3" + str(foodUser) + "\n")
my_file.write("Hobby : " + u"\u00a3" + str(hobbyUser) + "\n")
my_file.write("Clothing : " + u"\u00a3" + str(clothingUser) + "\n")
my_file.write("Other : " + u"\u00a3" + str(miscellaneousUser) + "\n\n")

my_file.write("*********************Debt********************\n\n")

my_file.write("reimbursement debt : " + u"\u00a3" + str(debtreimbursementUser) + "\n\n")
my_file.write("Student debt : " + u"\u00a3" + str(studentloanUser) + "\n")
my_file.write("Consumption debt : " + u"\u00a3" + str(consumerloanUser) + "\n")
my_file.write("Mortage debt : " + u"\u00a3" + str(mortgageloanUser) + "\n\n")
my_file.write("TOTAL debt : " + u"\u00a3" + str(totalloanUser) + "\n\n")

my_file.write("********************Saving*******************\n\n")

my_file.write("With your current way of life, you could save " + u"\u00a3" + str(round(saving1year))+ " in 1 year, " + u"\u00a3" + str(round(saving3years)) +" in 3 years, and " + u"\u00a3" + str(round(saving5years))+" in 5 years.")

my_file.close()
