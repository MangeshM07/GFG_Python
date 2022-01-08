#Importing entire code
# from Corey.Fundamentals import my_module as mm

from Corey.Fundamentals.my_module import find_index as fi
import sys

courses = ["History", "Maths", "Physics", "CompSci"]

# index = mm.find_index(courses, "Maths")
index = fi(courses, "Maths")
index = fi(courses, "Maths")
print(index)
print(sys.path)

