import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
# continue here

print (random_numbers)

import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Continue by replacing numbers greater than 80 with their corresponding negative value
for i in range(len(random_numbers)):
    if random_numbers[i] > 80:
        random_numbers[i] = -random_numbers[i]

# Print the list at the end
print("Updated list:", random_numbers)