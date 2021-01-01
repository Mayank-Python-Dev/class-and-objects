position = 0
def searching(list,search_element):
    for i in range(len(list)):
        if list[i] == search_element:
            return True
        globals()['position']+=1
    else:
        return False


list = [1,2,3,4,5,6,7,8,9,10]
search_element = 11
if searching(list,search_element):
    print(f'Found at {position}')
else:
    print(f'Not found')

print(6+5-4*3/2%1)

