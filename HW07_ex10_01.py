# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def nested_sum(list_):
    total = 0
    for s in list_:
        if type(s) == type([]):                 #To check if element in a list is a list
            total += nested_sum(s)

        else:
            total += s
    return total 
            
    
def main():
#     print nested_sum([[2,[3,1],2],2,3])
#     print nested_sum([1,2,3])
#     print nested_sum([1,2,[3,0],8])
    pass
    
if __name__ == '__main__':
    main()
    
        