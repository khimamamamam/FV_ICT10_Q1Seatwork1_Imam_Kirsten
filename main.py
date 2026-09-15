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


h3ight = 144.78
_countries = {"kazakhstan", "korea", "china"}
display(f'My height is {h3ight}, The countries I want to visit are {_countries}', target = "result2")


others = {
    "color": "purple",
    "car_brand": "scooter",
    "best_friend": "Both of my sisters, Gab, Aeris, and Caitlyn",
}
display(others["color"], others["car_brand"], others["best_friend"], target = "result3")

set = (("avocado", "banana", "grapes", "pineapple", "dragonfruit"))
display(f'My favorite fruits are {set}', target = "result4")