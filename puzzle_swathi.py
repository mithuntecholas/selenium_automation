n=int(input("enter number of chairs in the circle:"))
puzzle={}
for i in range(1,n+1):
    key=i
    value={key:i}
    puzzle[key]=value
def shift_puzzle(puzz:dict):
    # print("what i am getting",puzz)
    shift_puzz = {}
    for i in range(1, n + 1):
        shift_puzz[i] = {}
    for k,v in puzz.items():
        for pos,man in v.items():
            new_pos=(k+pos)%n
            if new_pos==0:
                new_pos=n
            shift_puzz[new_pos].__setitem__(pos,man)
    return shift_puzz
def check_it_done(puzz:dict):
    for k,v in puzz.items():
        if len(v)!=1:
            return False
    else:
        return True
#print(puzzle)
the_min_value=1
while True:
    the_min_value=the_min_value+1
    puzzle=shift_puzzle(puzzle)
    #print(the_min_value)
    #print(puzzle)
    if check_it_done(puzzle) and the_min_value>1:
        #print_puzzle(puzzle)
        print("The minimum number of shift  required to  occupy each chair by exactly one person is:",the_min_value)
        break
    else:
        #print_puzzle(puzzle)
        continue




