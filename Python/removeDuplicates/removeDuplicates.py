def removeDuplicates_set(input_list):
    return(list(set(input_list)))

def removeDuplicates_loop(input_list):
    length = len(input_list)
    i = 0
    while(i< length-1):
        if(input_list[i] == input_list[i+1]):
            input_list.remove(input_list[i])
        else:
            i += 1
        length = len(input_list)
        

    return(input_list)



input_list = list(map(int,input("Enter two numbers: ").rstrip().split(' ')))
print(removeDuplicates_set(input_list))
print(removeDuplicates_loop(input_list))

