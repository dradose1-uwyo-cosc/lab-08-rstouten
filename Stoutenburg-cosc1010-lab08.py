# Reuben Stoutenburg
# UWYO COSC 1010
# Submission Date: 11/7/24
# Lab 08
# Lab Section: 13
# Sources, people worked with, help given to:
# ChatGPT to check if floats are in correct format so string.replace('.','',1).isdigit():
# ChatGPT to figure our how to take the square root so "import math" and math.sqrt(value)

def validate_number(string):
    #check if string is int, float, or neither
    try:
        int_value = int(string)
        return int_value
    except ValueError:
        try:
            if '.' in string and string.replace('.','',1).isdigit():
                float_value = float(string)
                return float_value
            else:
                return False
        except ValueError:
            return False

print("*" * 75)

def graph(m,b,x_min,x_max):
    #Find the y-values for all x values in given range
    def validate_int_float(value):
    #check if string is int, float, or neither
        try:
            return int(value)
        except ValueError:
            try:
                if '.' in value and value.replace('.','',1).isdigit():
                    return float(value)
                else:
                    return False
            except ValueError:
                return False
    def validate_int(value):
    #check if string is integer
        try:
            return int(value)
        except ValueError:
            return False
    x_min_value = validate_int(x_min)
    x_max_value = validate_int(x_max)
    #check if x min/max are integers
    if x_min_value is False or x_max_value is False:
        return False
    #check if x_min is less than x_max
    if x_min_value >= x_max_value is False:
        return False
    m_value = validate_int_float(m)
    b_value = validate_int_float(b)
    #check m and b values
    if m_value is False or b_value is False:
        return False
    y_values = []
    #loop through x values and append each corresponding y value to a list
    for x in range(x_min_value,x_max_value + 1):
        y = m_value * x + b_value
        y_values.append(y)
    return y_values

    
while True:
    input_m = input("Give me the slope of a line: ")
    input_b = input('Give me a y-intercept: ')
    input_x_min = input('Give me a minimum x-value: ')
    input_x_max = input('Give me a maximum x-value: ')
    break
print(graph(input_m,input_b,input_x_min,input_x_max))

print("*" * 75)
import math
while True:
    print("When prompted give me the 3 coefficients in a polynomial(a,b,c)")
    input_a = input("a: ")
    input_b = input("b: ")
    input_c = input("c: ")
    break

def quadratic_calculator(a,b,c):
    #solve quadratic formula with given a,b,c values
    def validate_val(value):
    #check if string is int, float, or neither
        try:
            return int(value)
        except ValueError:
            try:
                if '.' in value and value.replace('.','',1).isdigit():
                    return float(value)
                else:
                    return False
            except ValueError:
                return False
    a_value = validate_val(a)
    b_value = validate_val(b)
    c_value = validate_val(c)
    if a_value is False or b_value is False or c_value is False:
        return False
    def sqr_rt(a,b,c):
        #take the square root b^2 - 4ac
        try:
            sqr_root = math.sqrt(b**2 - 4 * a * c)
            return sqr_root
        except:
            return False
    root_result = sqr_rt(a_value,b_value,c_value)
    positive_result = (-b_value + root_result)/(2*a_value)
    negative_result = (-b_value - root_result)/(2*a_value)
    return positive_result , negative_result

print(quadratic_calculator(input_a,input_b,input_c))

    


                
                
                
            
                    
     





