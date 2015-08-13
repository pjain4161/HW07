# I want to be able to call capitalize_nested from main w/ various lists 
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
['Apple', ['Bear'], 'Cat']
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()


def capitalize_nested(list_):
    lis = []
    for s in list_:
        if type(s) == type([]):                 #To check if element in a list is a list
            lis.append(capitalize_nested(s))
        else:
            lis.append(s.capitalize())    
    
    return lis 
            
            
def main():
#     print capitalize_nested(['apple', ['mango','abc'], 'tree'])
#     print nested_sum([1,2,3])
#     print nested_sum([1,2,[3,0],8])
    pass
    
if __name__ == '__main__':
    main()