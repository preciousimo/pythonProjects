# A function that takes a list and target parameter
# Multiple variables: middle, start, end, steps
# While loop
# Increase the steps each time a split is done
# Conditions to track target position

def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while(start<=end):
        print("Step",steps, ":", str(list[start:end+1]))

        steps = steps+1
        middle = (start + end) // 2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle-1
        else:
            start = middle+1

    return -1

my_list = [2,4,6,8,10,12,14,16,18,20]
target = 7

binary_search(my_list, target)