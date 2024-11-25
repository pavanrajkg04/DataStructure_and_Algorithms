def LinearSearch(list,Target):
    for i in range(0,len(list)):
        if list[i] == Target:
            return i
    return None

def validate(result):
    if result is not None:
        print("The Target is : ",result)
    else:
        print("The target not found",result) 



result = LinearSearch([1,2,3,4,5,6,7,8,9,10],3)
validate(result)