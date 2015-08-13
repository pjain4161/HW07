# write a function called chop that takes a list, 
# modifies it by removing the first and last elements, 
# and returns None


def chop(list_):
    
    
#     print length
    list_.pop(0)
#     length = len(list_)-1
    list_.pop(-1)
    print list_
    return None
    
def main():
    list_ = [1,2,3, "hi", "sea", "class"]
    chop(list_)
    
main()
    