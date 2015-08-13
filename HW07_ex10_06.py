# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def is_sorted(t):
    next = 1
    for previous in range(len(t)-1):
        if t[previous] > t[next]:
            return False
        else:
            next += 1
    return True

def main():
#     print is_sorted([1,2,2])
#     print is_sorted(['b','a'])
    pass
    
if __name__ == '__main__':
    main()
            
    
        
        
    