
from sympy import * #Imports all functionalities of Sympy including
                    #mathematical constants.

variables=dict()    #Dictionary in the form {variable:[true_value,error]}.
vars=dict()         #Dictionary in the form {variable:true_value}.

print("""Enter 'done' when you are finished with the variables: \n
Enter Variable,True value,error in this format:x 3 0.1\n
Delimeter used is space.\n
Avoid using python and sympy keywords as variable names example(I,for,pi,etc).

""")
response=""         #Initialising the response variable to an empty string.

while response.lower() !="done":
    response=input('Type "done" if finished \n Enter your variables, true value and error: ')
                    #Accepts input in the form {variable true_value error}.
                    #Delemiter used is space eg{x 1 0.1}.

    if response!= "done":#Typing done on the terminal terminates the while loop.
        resp=response.split(" ")

        variable=resp[0]
        temp=resp[0]
        temp=symbols("resp[0]")#Converting variables into symbolic expressions.
        true_value=resp[1]
        error=resp[2]
                    # Building Dictionaries vars and variables
        vars[variable]=true_value
        variables[variable]=[]
        variables[variable].append(float(true_value))
        variables[variable].append(float(error))

print("""\n*Enter the expression  using python syntax using appropriate parenthesis.\n
*All constant values to be entered explicitly.\n
 *Program accepts trigonometric and exponential functions:(sin(),cos(),exp(),log()),etc.\n
 *Angle values are supposed to be entered in radians.\n
 *Avoid using python and sympy keywords as variable names example(I,for,pi,etc).
 """)
expression=input("Enter your expression:")#User types the expression.


all_terms=[]#Stores each term in the general formula.
for key in variables:

    partial=diff(expression,key)   #Solves partial differential equations.
    nth_term_val=partial.subs(vars)#Computes the value of the differential.
    nth_term_val*=variables[key][1]#Multiplies the error to each term.

    all_terms.append(nth_term_val)



#Calculations as per general formula
summ=0
for i in all_terms:
  temp=i**2
  summ+=temp

error=summ**0.5
error=error.evalf()


best_value=simplify(expression).subs(vars)
best_value=best_value.evalf()
print("The best value is: ",best_value)
print("The error is: ",error)


best_value=format(best_value,"E")
error=format(error,"E")
print(best_value,'±',error)#Displays the Best value along with the error
                           #in scientific notation.

