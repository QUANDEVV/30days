# def element_exists(element, tuple_data):
#     if element in tuple_data:
#         return True
#     else:
#         return False

# # Example usage
# my_tuple = (1, 2, 3, 4, 5)
# element = 3

# if element_exists(element, my_tuple):
#     print(f"The element {element} exists in the tuple.")
# else:
#     print(f"The element {element} does not exist in the tuple.")



# 2
# def list_to_tuple(input_list):
#     tuple_data = tuple(input_list)
#     return tuple_data

# # Example usage
# my_list = [1, 2, 3, 4, 5]
# my_tuple = list_to_tuple(my_list)
# print(f"The converted tuple: {my_tuple}")



# 3


arr = [23, 6, 4, 90, 21]

def miniMaxSum(arr):
    arr.sort()
    # print(arr)
    min_sum = sum(arr[:4])
    max_sum = sum(arr[1:])
    print(min_sum, max_sum)
   

miniMaxSum(arr)
