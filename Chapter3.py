#Exercise3

#example program 3.1
def message():
    print ('I am Arthur,')
    print ('King of Britons')

message()
#Example Program 3.2
def main():
    print ('I have a message for you. ')
    message()
    print ('Goodbye! ')

#define the message function
def message ():
    print ('I am Arthur,')
    print ('King of Britons')

main()

#Local variables - this program demonstrates two functions that have...
#...local variables with the same name

def main():
	#call the texas function
	texas()
	#call the california
	california()

#definiton of the function. It creates a local variable named birds.
def texas():
	birds = 5000
	print'texas has', birds, 'birds.'

def california():
	birds = 8000
	print 'california has', birds, 'birds.'

#call the main function.
main()


#Example 3-6 pass_arg.py
#this program demonstrates an argument being passed to a function

def main():
	value = 5
	show_double(value)

	#the show_double function accepts an argument and displays double its value

def show_double(number):
	result = number * 2
	print(result)

# Call the main function
main()

#Example 3.7 cups_to_ounces.py
#this program converts cups to fluid ounces.

def main():
	#display the intro screen.
	intro()
	cups_needed = int(input('Enter the number of cups: ')) #gets the number of cups,
	cups_to_ounces(cups_needed) #convert the cups to ounces.

# The intro function displays an introduction screen.
def intro():
	print 'This program converts measurements in cupts to fluid ounces'
	print 'For your reference the formula is: 1 cup = fluid ounces'
	print

# the cups_to_ounces function accepts a number of cups and displays the...
# ...equivalent number of ounces

def cups_to_ounces(cups):
	ounces = cups * 8
	print 'That converts to', ounces, 'ounces.'

main()

#Program 3-8 Multiple_args.py
#This program demonstrates a function that accepts two arguments

def main():
	print ('The sum of 12 and 45 is')
	show_sum(12, 45)

#the show_sum function accepts two arguments and displays their sum

def show_sum(num1, num2):
	result = num1 + num2
	print (result)

main()

#Program 3-9 strings_arg.py
#This program demonstrates passing two string arguments to a function

def main():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    print('Your name reversed is ')
    reverse_name(first_name, last_name)

def reverse_name(first, last):
    print(last, first)

main()

#Making changes to parameters
#Program 3-10 change_me.py():
#This program demonstrates what happens when you change the value of the pararmeter

def main():
    value = 99
    print ('The value is ', value)
    change_me(value)
    print('Back in main the value is', value)

def change_me(arg):
    print('I am changing the value. ')
    arg = 0
    print ('Now the value is ', arg)

main()

#Program 3-11 keyword_args.py
#this program demonstrates keyword arguments

def main():
    #show amount of simple interest, using 0.01 as interest rate per period,
    #10 as the number of periods, and $10,000 as the principal
    show_interest(rate=0.01, periods=10, principal=10000.0)

#The show_interest function displays the amount of simple interest for a given
#principal, interest for a given principal, interest rate per period, and number
#periods

def show_interest(principal, rate, periods):
    interest = principal * rate * periods
    print ('The simple interest will be $', \
            format(interest, ',.2f'), \
            sep='')

# Call the main function
main()

#Program 3-13 GLOBAL variable
my_value = 10

#The show_value function prints the value of the global variable

def show_value():
    print(my_value)

#call the value function
show_value()

# Program 3-14 create a global variable
number = 0

def main():
    global number
    number = int(input('Enter a number: '))
    show_number()

def show_number():
    print ('The number you entered is ', number)

main()
