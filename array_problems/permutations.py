def permute_array(arr, start_index, result_list):
    if start_index == len(arr):
        result_list.append(list(arr))  # Add a copy of the current permutation
        return

    for i in range(start_index, len(arr)):
        arr[start_index], arr[i] = arr[i], arr[start_index]  # Swap
        permute_array(arr, start_index + 1, result_list)  # Recurse
        arr[start_index], arr[i] = arr[i], arr[start_index]  # Backtrack (swap back)

def get_all_permutations(input_array):
    permutations = []
    permute_array(input_array, 0, permutations)
    return permutations

# Example Usage:
my_array = [1, 2, 3]
all_perms = get_all_permutations(my_array)
# for p in all_perms:
#     print(p)

# my_string = "ABC"
# all_string_perms = get_all_permutations(list(my_string))
# for p in all_string_perms:
#     print("".join(p))
print("************************************************")