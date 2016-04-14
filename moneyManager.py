from datetime import date

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
                 assert(rentweek.isnumeric())
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
            childrenTotal = (childrenuser,childrenCost)
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
"""
titleUser = title()
firstnameUser = firstname()
surnameUser = surname()
"""
ageDobUser = age()
ageUser = ageDobUser[0]
yearUser = ageDobUser[1]
monthUser = ageDobUser[2]
dayUser = ageDobUser[3]
contributionNIUser = contributionNI()
incomeUser = income()

"""
rentUser = rent()
studentloanUser = studentloan()
consumerloanUser = consumerloan()
mortgageloanUser = mortgageloan()
foodUser = food()
clothingUser = clothing()
hobbyUser = hobby()
miscellaneousUser = miscellaneous()
childrenUser = childrenNumber()
childrennumberUser = childrenUser[0]
childrencostUser = childrenUser[1]
"""

def personalAllowance(ageUser,incomeUser):
      if ageUser <= 77:
          if incomeUser <=10600:
              return incomeUser
          elif  10600<incomeUser <= 100000:
              return 10600
          elif 100000< incomeUser <121200:
              return round(10600-((incomeUser-100000)/2),2)
          else:
              return 0
      else:
          if incomeUser <= 10660:
              return incomeUser
          elif 10600< incomeUser <= 27700:
              return 10600
          elif 27700<incomeUser <=27820:
              return round(10660-((incomeUser-27700)/2),2)
          elif 27820 < incomeUser <= 100000:
              return 10600
          elif 100000<incomeUser<=121200:
              return round(10600-((incomeUser-100000)/2),2)
          else:
              return 0

personalAllowanceUser = personalAllowance(ageUser,incomeUser)

def taxpaid(personalAllowanceUser,incomeUser):
    taxableIncome = (incomeUser - personalAllowanceUser)
    if taxableIncome <=0:
        return 0
    elif 0< taxableIncome <= 31785:
        return round(0.2*taxableIncome,2)
    elif 31785 < taxableIncome <= 150000:
        return round(0.2*31785 + (taxableIncome - 31786)*0.4,2)
    else:
        return round(0.2*31785 + 0.4*(150000-31785) + (taxableIncome-150000)*0.45,2)

taxpaidUser = taxpaid(personalAllowanceUser,incomeUser)

def nationalInsuranceContribution(contributionNIUser,ageUser,incomeUser):
    if ageUser > 67 or contributionNIUser == False:
        return 0
    elif incomeUser <= 8060:
        return 0
    elif 8060 < incomeUser <= 42380:
        return round((incomeUser - 8060)*0.12,2)
    else:
        return round(0.12*(42380-8060) + (incomeUser-42380)*0.02)

nationalInsuranceContribution = nationalInsuranceContribution(contributionNIUser,ageUser,incomeUser)

def totalDeduction(nationalInsuranceContribution,taxpaidUser):
    return  nationalInsuranceContribution + taxpaidUser

totalDeductionUser = totalDeduction(nationalInsuranceContribution,taxpaidUser)

def moneyLeavingAfterTax(totalDeductionUser,incomeUser):
    return incomeUser - totalDeductionUser

moneyLeavingAfterTaxUser = moneyLeavingAfterTax(totalDeductionUser,incomeUser)
print(moneyLeavingAfterTaxUser)
# def moneyLeavingAfterExpenses():
# def leavingDebt():
# def saving():

