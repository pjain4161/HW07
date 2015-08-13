# I want to be able to call cumulative_sum from main w/ various lists and 
# get returned a list of the cumulative sums.
# You are safe to expect only integers in a flat list.
# Ex. the cumulative sum of [1, 2, 3] is [1, 3, 6]
#  - in the above example I want returned the list [1, 3, 6]
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def cumulative_sum(lis):
#     sum = 0
    new_lis = []
    for item in range(len(lis)):   # Run the loop for each item in list
        sum = 0
        for j in range(item+1):     # Run the loop to get the sum of all items till the current item
            sum += lis[j]
        new_lis.append(sum)
    return new_lis
    
def main():
#     print cumulative_sum([1,2,3])
    pass
    
if __name__ == '__main__':
    main()
    
        
        
        