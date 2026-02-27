
def list_sum(lst):
    
    if lst==[]:
        raise ValueError("The list cannot be empty.")
    if len(lst)==1:
        return lst.pop()
    else:
        return lst.pop() + list_sum(lst)

print("the sum of list is: ",list_sum([1,2,3,4,5]))