# write a function that reads roster.txt and prints the following:
# "A list of first and last names:"
# [First Last, First Last, First Last, etc.] 
# 
# "A list of lists of first and last name:"
# [[First, Last], [First, Last], [First, Last], etc.]
# 
# "A list of first names sorted by length:"
# [ShortFirst, LongFirst, LongerFirst, etc.]

def read_file():
    list1 = []
    f = open("roster.txt")
    for line in f:
        word = line.strip()
        list1.append(word)
        
    print " A list of first and last names:"
    print list1
    
#     i = 0
    list2 = []
    list3 = []
    list4 = []
   
    for i in range(len(list1)):
        list2 = list1[i].split()
#         print list2
        
        list3.append(list2)  # get list of names inside list
        
        list4.append(list2[0]) # get first names inside list4
        
        
    
    print
    print " A list of lists of first and last name:"
    print list3 
    
    print 
    print "A list of first names sorted by length:"
    list4.sort(key = len)
    print list4
        
def main():
    read_file()

main()