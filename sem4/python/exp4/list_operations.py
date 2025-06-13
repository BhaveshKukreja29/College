def even_odd_split(lst):
    even = []
    odd = []
    for num in lst:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd

def merge_sort_lists(lst1, lst2):
    merged = lst1 + lst2
    merged.sort()
    return merged

def update_first(lst, x):
    lst[0] = x
    return lst

def get_middle(lst):
    return lst[len(lst) // 2]
