position = 0
def searching(list,search_element):
    lower = 0
    upper = len(list)-1
    while lower <= upper:
        mid_value = (lower-upper) // 2
        if list[mid_value] == search_element:
            globals()['position'] = mid_value
            return True
        else:
            if list[mid_value]<search_element:
                lower = mid_value
            else:
                upper = mid_value
    return False


list = [1,2,3,4,5,6,7,8,9,10]
search_element = 7
if searching(list,search_element):
    print(f'Found at {position}')
else:
    print(f'Not found')