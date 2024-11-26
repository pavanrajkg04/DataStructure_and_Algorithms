def BinarySearch(list,target):
    first = 0
    last = len(list) - 1
    while first <= last:
        midpoint = (first+last)//2 # Floor Division
        if list[midpoint] < target:
            first = midpoint + 1
        elif list[midpoint] > target:
            last = midpoint - 1
        else:
            return midpoint
    return None

def validate(result):
    if result is not None:
        print("The Target index is : ",result)
    else:
        print("The target not found") 



result = BinarySearch([1,2,3,4,5,6,7,8,9,10],3)
validate(result)