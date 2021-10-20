Variables:
Variables are containers for storing data values.

Creating Variables:
->Python has no command for declaring a variable.
->A variable is created the moment you first assign a value to it.
x = 5
y = "John"
print(x)
print(y)

->Variables do not need to be declared with any particular type,
and can even change type after they have been set.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

Casting:
->If you want to specify the data type of a variable,
this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


Variable Names:
->A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
->A variable name must start with a letter or the underscore character
->A variable name cannot start with a number
->A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
->Variable names are case-sensitive (age, Age and AGE are three different variables)

Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"

Multi Words Variable Names:
Variable names with more than one word can be difficult to read.

There are several techniques you can use to make them more readable:

->Camel Case:
 Each word, except the first, starts with a capital letter:
 myVariableName = "John"
 
->Pascal Case:
 Each word starts with a capital letter:
 MyVariableName = "John"
 
->Snake Case:
Each word is separated by an underscore character:
my_variable_name = "John"

