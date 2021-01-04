# implements binary search by using recursive algrithm
def binary_search(sorted_list, target):
    def do_binary_search(start_index, end_index):
        #target is not in list.
        if start_index > end_index:
            return -1
        # computer mid_index
        mid_index = (start_index + end_index) // 2

        if sorted_list[mid_index] == target:
            return mid_index
        elif sorted_list[mid_index] > target:
            return do_binary_search(start_index, mid_index - 1)
        else:
            return do_binary_search(mid_index + 1, end_index)
    return do_binary_search(0, len(sorted_list))

# implements binary search by using loop
def binary_search_2(sorted_list, target):
    start_index = 0
    end_index = len(sorted_list)
    
    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        
        if sorted_list[mid_index] == target:
            return mid_index
        elif sorted_list[mid_index] > target:
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1
    
    return -1

sorted_list = [1, 3, 4, 5, 6, 10, 11, 14, 51]
target = -10

print(binary_search(sorted_list, target))
print(binary_search_2(sorted_list, target))