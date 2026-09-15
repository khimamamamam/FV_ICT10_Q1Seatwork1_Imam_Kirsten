from pyscript import display 
from js import document

fullname = 'Kirsten Heart D. Imam' #stirng
age = 16 #integer
display(f'Hi! I am {fullname} and I am {age} years old', target = "result")


h3ight = 144.78 #float
_countries = ['kazakhstan', 'korea', 'china']
display(f'Countries I want to visit: {", ".join(_countries)}', target="result2")


new_student = False #boolean
display(f'New student: {new_student}', target = "result3")


others = {
    "color": "purple",
    "car_brand": "scooter",
    "best_friend": "Both of my sisters, Gab, Aeris, and Caitlyn",
} #dictionary
display(others["color"], others["car_brand"], others["best_friend"], target = "result4")


fruits = set(['avocado', 'banana', 'grapes', 'pineapple', 'dragonfruit']) #set
display(f'My favorite fruits: {fruits}', target = "result5")


days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday") #tuple
display(f'Days of the week: {days}', target = "result6")


def add_numbers(e):
    num1 = float(document.getElementById("num1").value)
    num2 = float(document.getElementById("num2").value)
    document.getElementById("output").innerText = num1 + num2

def subtract_numbers(e):
    num1 = float(document.getElementById("num1").value)
    num2 = float(document.getElementById("num2").value)
    document.getElementById("output").innerText = num1 - num2

def multiply_numbers(e):
    num1 = float(document.getElementById("num1").value)
    num2 = float(document.getElementById("num2").value)
    document.getElementById("output").innerText = num1 * num2

def divide_numbers(e):
    num1 = float(document.getElementById("num1").value)
    num2 = float(document.getElementById("num2").value)
    document.getElementById("output").innerText = num1 / num2