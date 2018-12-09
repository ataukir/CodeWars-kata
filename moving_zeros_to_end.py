# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
def move_zeros(array):
    ans = []
    count = 0
    for i in array:
        if (str(i) == "0" or str(i) == "0.0") and type(i) is not str:
            count += 1
        else:
            ans.append(i)
    zero_arr = [0 for i in range(count)]
    ans.extend(zero_arr)
    return ans
    
    
    
move_zeros([0,1,None,2,False,1,0]),[1,None,2,False,1,0,0]
