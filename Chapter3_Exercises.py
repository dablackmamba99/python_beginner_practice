#Programming Exercises
"""
1. Kilometer Converter
Write a program that asks the user to enter a distance in kilometers, and then converts that
distance to miles. The conversion formula is as follows:
Miles = Kilometers * 0.6214
"""

def main():
    kilometers = int(input('Enter amount of kilometers to be converted to miles: '))
    converter(kilometers)

def converter(km):
    miles = km * 0.6214
    print (km, 'km is ', miles ,'miles')

main()

"""
2. Sale Tax Program Refactoring
Programming Exercise #6 in Chapter 2 was the Sales Tax program. For that exercise you
were asked to write a program that calculates and displays the county and state sales tax
on a purchase. If you have already written that program, redesign it so the subtasks are in
functions. If you have not already written that program, write it using functions.
"""
'''
3. How Much Insurance?
Many financial experts advise that property owners should insure their homes or build-
ings for at least 80 percent of the amount it would cost to replace the structure. Write a
program that asks the user to enter the replacement cost of a building and then displays
the minimum amount of insurance he or she should buy for the property.
'''
def main():
    replacement_building_value = float(input('Enter the value of the replacement building: '))
    minimum_cost(replacement_building_value)

def minimum_cost(replacement):
    cost = replacement * 0.8
    print ('The cost of the replacement building is $', replacement, \
    'the cost for the replacement builing will be $', cost)

main()

'''
4. Automobile costs
Write a program that asks the user to enter  the monthly costs for the following expenses
incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and
maintenance. The program should then display the total monthly cost of these expenses,
and the total annual cost of these expenses.
'''

def main():
    print ('Enter the cost of the following (in $): ')
    loan_payment = float(input('Loan payment: '))
    insurance = float(input('Insurance: '))
    gas = float(input('Gas: '))
    oil = float(input('Oil: '))
    tires = float(input('Tires: '))
    maintenance = float(input('Maintenance: '))
    total_cost(loan_payment, insurance, gas, oil, tires, maintenance)
    print('The loan payment cost is: ', loan_payment)
    print('The insurance cost is: ', insurance)
    print('The gas payment cost is: ', gas)
    print('The tires payment cost is: ', tires)
    print('The maintenance payment cost is: ', maintenance)


def total_cost(loan, ins, gas, oil, tires, main):
    total = loan + ins + gas + oil + tires + main
    print('The total cost of all the expenses is: ', total)

main()

'''
5. Property Tax
A county collects property taxes on the assessment value of property, which is 60 per-
cent of the property’s actual value. For example, if an acre of land is valued at $10,000,
its assessment value is $6,000. The property tax is then 64¢ for each $100 of the assess-
ment value. The tax for the acre assessed at $6,000 will be $38.40. Write a program that
asks for the actual value of a piece of property and displays the assessment value and
property tax.
'''
#first find assessment value

def main():
    property_value = float(input('Enter the value of the property: '))
    changed_value(property_value)

def changed_value(prop_val):
    new_value = prop_val * 0.6
    taxed_value = new_value * 0.0064
    print('The property assessment value is $',new_value)
    print('The tax for the property is $', taxed_value)


main()
