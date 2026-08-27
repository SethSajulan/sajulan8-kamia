# Reflection:
# Using a math library is more practical because it saves time and eliminates the need to implement 
# complex numerical algorithms, like computing square roots, manually. In this activity, functions like 
# math.sqrt() and math.pow() allowed us to apply the Euclidean distance formula cleanly in just a few 
# lines of code, ensuring both accuracy and efficiency.

import math

# Prompt the user for input
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate distance using the Euclidean distance formula
# d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Display the result formatted to two decimal places
print(f"\nThe distance between the two points is: {distance:.2f}")