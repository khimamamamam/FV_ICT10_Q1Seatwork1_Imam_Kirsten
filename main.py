from pyscript import display, document

fullname = 'Kirsten Heart D. Imam' #stirng
age = 16 #integer
display(f'Hi! I am {fullname} and I am {age} years old', target = "result")


h3ight = 144.78 #float
display(f'Height: {h3ight} cm', target = "result1")


_countries = ['Kazakhstan', 'Korea', 'US'] #list
display(f'Countries I want to visit: {", ".join(_countries)}', target="result2")


new_student = False #boolean
display(f'New student: {new_student}', target = "result3")


others = {
    "color": "purple",
    "car_brand": "scooter",
    "best_friend": "Both of my sisters, Gab, Aeris, and Caitlyn",
} #dictionary
display(f'Favorite color: {others["color"]}', target="result4")
display(f'Car brand: {others["car_brand"]}', target="result4")
display(f'Best friends: {others["best_friend"]}', target="result4")


fruits = set(['avocado', 'banana', 'grapes', 'pineapple', 'dragonfruit'])
display(f'My favorite fruits: {", ".join(fruits)}', target="result5")


days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")#tuple
display(f'My favorite fruits: {", ".join(days)}', target="result6")


def add(e):
    document.getElementById("output").innerHTML = " "

    number1 = float(document.getElementById("num1").value)
    number2 = float(document.getElementById("num2").value)

    result = number1 + number2
    display(result, target = "output1")

def subtract(e):
    document.getElementById("output").innerHTML = " "

    number1 = float(document.getElementById("num1").value)
    number2 = float(document.getElementById("num2").value)

    result = number1 - number2
    display(result, target = "output1")

def multiply(e):
    document.getElementById("output").innerHTML = " "

    number1 = float(document.getElementById("num1").value)
    number2 = float(document.getElementById("num2").value)

    result = number1 * number2
    display(result, target = "output1")

def divide(e):
    document.getElementById("output").innerHTML = " "

    number1 = float(document.getElementById("num1").value)
    number2 = float(document.getElementById("num2").value)

    result = number1 / number2
    display(result, target = "output1")