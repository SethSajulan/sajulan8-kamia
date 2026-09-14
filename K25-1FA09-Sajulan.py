# Reflection:
# Using a math library is simpler and much better than complex numerical algorithms as it saves much more time. 
# This activity lets us make use of math.sqrt() and math.pow() to apply the Euclidean distance formula cleanly 
# in just a few lines of code while still ensuring accuracy and efficiency. 

import math

# Ask the user for an input
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate distance using the Euclidean distance formula
# d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Display the result rounded to two decimal places
print(f"\nThe distance between the two points is: {distance:.2f}")
