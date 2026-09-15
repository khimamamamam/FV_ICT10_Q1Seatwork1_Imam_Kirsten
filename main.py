from pyscript import display
#

#a = 0 # integer
#b = 0.1 # float
#c = [] #empty list

#display(bool(a))
#display(bool(b))
#display(bool(c))

fullname = 'Kirsten Heart D. Imam' #stirng
age = 16 #integer
display(f'Hi! I am {fullname} and I am {age} years old', target = "result")


h3ight = 144.78 #float
_countries = ['kazakhstan', 'korea', 'china'] #ist
display(f'Height: {h3ight}, Countries I want to visit: {_countries}', target = "result2")


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

