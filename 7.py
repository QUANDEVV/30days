# from collections import Counter

# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}

# combined_dict = Counter(d1) + Counter(d2)

# print(combined_dict)
# The Counter class is a dictionary subclass specifically designed for counting hashable objects. 




# question 2
# string = 'w3resource'
# letter_count = {}
# # Count the letters in the string
# for letter in string:
#     letter_count[letter] = letter_count.get(letter, 0) + 1

# print(letter_count)





#question 3
from collections import Counter

data = {'Math': 81, 'Physics': 83, 'Chemistry': 87}

sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)

print(sorted_data)


















