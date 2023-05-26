# import itertools

# def find_combinations(numbers, target):
#     # Generate all unique combinations of 3 numbers from the list
#     combinations = itertools.combinations(numbers, 3)
    
#     # Find valid combinations that add up to the target
#     valid_combinations = []
#     for combo in combinations:
#         if sum(combo) == target:
#             valid_combinations.append(combo)
    
#     return valid_combinations

# # Example usage
# numbers = [1, 2, 3, 4, 5, 6, 7]
# target = 10

# result = find_combinations(numbers, target)
# print(result)



# 2

# def merge_sets(set1, set2):
#     # Create a new set by merging set1 and set2
#     merged_set = set1.union(set2)
    
#     return merged_set

# # Example usage
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# merged_set = merge_sets(set1, set2)
# print(merged_set)



# 3

def update_set(set1, set2):
    # Update set1 with items that are not present in set2
    set1.difference_update(set2)
    
    return set1

# Example usage
set1 = {10, 20, 30}
set2 = {20, 40, 50}

updated_set = update_set(set1, set2)
print("set1:", updated_set)
