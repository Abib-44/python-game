from browser import document
import re
import operator

expression = ""

def button_click(event):
    global expression

    value = event.target.text
    expression += str(value)
    check_input(expression)
    document["display"].value = expression

def check_input(expr):
    global expression

    if expr[-1] == "=":
        calculate_result()

    operators = {"*", "+", "-", "/"}

    if (len(expr) < 2 and expr[-1] in operators) or \
       (expr[-1] in operators and expr[-2] in operators):
        expression = expression[:-1]

def calculate_result():
    global expression
    
    expression = expression[:-1]
    chars = list(expression)

    operations = {
        "*": operator.mul,
        "/": operator.truediv,
        "+": operator.add,
        "-": operator.sub
    }

    for op in ["*", "/", "+", "-"]:

        i = 0

        while i < len(chars):
            if chars[i] == op:
                num1 = int(chars[i-1])
                num2 = int(chars[i+1])
                result = operations[op](num1, num2)
                chars[i-1] = ""
                chars[i+1] = ""
                chars[i] = str(result)
                chars = [x for x in chars if x != ""]
                i = 0
            else:
                i += 1

    expression = "".join(chars)
    document["display"].value = expression

for button in document.select("button"):
    button.bind("click", button_click)
