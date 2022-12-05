# Project Omega
# A graphing software that graphs that function, or point, you input, as well as its switch.
# Hope this is cool!

import matplotlib.pyplot as plt
import math
from sympy import var
from sympy import sympify



def menu():
    """Prints the menu of options that the user can choose."""
    print()
    print("(0) Enter a new function")
    print("(1) Give me a list of python math functions!")
    print("(2) Give me all x values of my function!")
    print("(3) Give me all y values of my function!")
    print("(4) Give me all switched x values of my function!")
    print("(5) Give me all switched y values of my function!")
    print("(6) Graph my function!")
    print("(7) Graph my switched function!")
    print("(8) Graph both the original and switched function!")
    print("(9) Quit")
    print()

def allfunctions():
    """
    Simply prints all valid python functions
    """
    print(' ')
    print('Here are possible functions! \n All typical python functions shoudl work!')
    print(' ')
    print('Arithmetic: \n +, -, * (mult), / (div), ** (pow)')
    print('Trig: sin(x), cos(x), tan(x), etc.')
    print('Others: abs(x), etc.')
    print('Basically, all sympy and python functions should work, \n Have fun!')


def inputFunctionX():
    """
    Takes a function input from the user.
    Creates a list of points in form (column, row), i.e. (x,y)
    """
    x = 100
    X = [x * 0.01 for x in range(0, x * 100 + 1)]
    return X


def switchX():
    """
    Reverses order of string.
    i.e. 26 -> 62. -26 -> -62
    """
    currentx = inputFunctionX()
    currentxlarge = [item*100 for item in currentx]
    newx = []
    for x in currentxlarge:
        cx = str(round(x))
        newx += [int(cx[::-1])]
    newxnormal = [item/100 for item in newx]
    return newxnormal

def main():
    """The main user-interaction loop."""
    x = var('x')
    function = sympify(x)  # an initial function

    while True:       # The user-interaction loop
        print("\n\nThe current function is y =",function)
        menu()
        choice = input("Choose an option: ")

        #
        # "Clean and check" the user's input
        # 
        

        try:
            choice = int(choice)   # Make into an int!
        except:
            print("I didn't understand your input! Continuing...")
            continue

        x = inputFunctionX() # list of all x values! Always 0 -> 100 at 0.01
        sx = switchX()
        if choice == 9:
            break

        elif choice == 0: #working! I think
            x = var('x')  # the possible variable names must be known beforehand...
            user_input = input("Choose your function, in python:")
            function = sympify(user_input)
            res = function.subs(x, [0, 1, 2, math.pi])
            print(res)
        
        


        elif choice == 1:
            allfunctions()

        elif choice == 2: #working!
            print(x)

        elif choice == 3: #working!
            fullx = inputFunctionX()
            y = []
            for num in fullx:
                x = var('x')
                res = function.subs(x, num)
                y += [res]
            print(y)


        elif choice == 4:
            # switched x values
            print(sx)
        
        elif choice == 5: #working!!!
            # switched y values
            fullx = inputFunctionX()
            currently = []
            for num in fullx:
                x = var('x')
                res = function.subs(x, num)
                currently += [res]
            currentlylarge = [item*100 for item in currently]
            newy = []
            for x in currentlylarge:
                cy = str(round(x))
                if '-' in cy:
                    cy = cy[1:]
                    newy += [-1 * int(cy[::-1])]
                else:
                    newy+= [int(cy[::-1])]
            newynormal = [item/100 for item in newy]
            print(newynormal)

        elif choice == 6: # works!
            fullx = inputFunctionX()
            y = []
            for num in fullx:
                x = var('x')
                res = function.subs(x, num)
                y += [res]

            print(fullx[0:3])
            print(y[0:3])
            
            plt.plot(fullx, y)

            # naming the x axis
            plt.xlabel('x - axis')
            # naming the y axis
            plt.ylabel('y - axis')

            # function to show the plot
            plt.show()

        elif choice == 7:
            fullx = inputFunctionX()
            
            currently = []
            for num in fullx:
                x = var('x')
                res = function.subs(x, num)
                currently += [res]
            currentlylarge = [item*100 for item in currently]
            newy = []
            for x in currentlylarge:
                cy = str(round(x))
                if '-' in cy:
                    cy = cy[1:]
                    newy += [-1 * int(cy[::-1])]
                else:
                    newy+= [int(cy[::-1])]
            newynormal = [item/100 for item in newy]

            currentx = inputFunctionX()
            currentxlarge = [item*100 for item in currentx]
            newx = []
            for x in currentxlarge:
                cx = str(round(x))
                newx += [int(cx[::-1])]
            newxnormal = [item/100 for item in newx]

            plt.plot(newxnormal, newynormal)

            # naming the x axis
            plt.xlabel('x - axis')
            # naming the y axis
            plt.ylabel('y - axis')

            # function to show the plot
            plt.show()
        
        elif choice == 8:
            fullx = inputFunctionX()
            
            currently = []
            for num in fullx:
                x = var('x')
                res = function.subs(x, num)
                currently += [res]
            currentlylarge = [item*100 for item in currently]
            newy = []
            for x in currentlylarge:
                cy = str(round(x))
                if '-' in cy:
                    cy = cy[1:]
                    newy += [-1 * int(cy[::-1])]
                else:
                    newy+= [int(cy[::-1])]
            newynormal = [item/100 for item in newy]

            currentx = inputFunctionX()
            currentxlarge = [item*100 for item in currentx]
            newx = []
            for x in currentxlarge:
                cx = str(round(x))
                newx += [int(cx[::-1])]
            newxnormal = [item/100 for item in newx]

            plt.plot(newxnormal, newynormal, label='switched')
            plt.plot(fullx, currently, label='original')
           
            # naming the x axis
            plt.xlabel('x - axis')
            # naming the y axis
            plt.ylabel('y - axis')
            plt.title("Switch and Original")
            plt.legend();

            # function to show the plot
            plt.show()
            

        #
        # Run the appropriate menu option
        #

