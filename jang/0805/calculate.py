def devider(thing,list,nums,thing_index):
    for i in range(len(list)):
        if list[i] == "+" or list[i] == "-" or list[i]=="/" or list[i] == "*":
            thing.append(list[i])
            nums.append(list[i])
            thing_index.append(i)
        else:
            nums.append(float(list[i]))

def calculating(thing,nums,thing_index):
    number =[]
    s1 =""
    stop_point=0
    for i in range(len(thing_index)):
        for j in range(stop_point,thing_index[i]):
            s1 += str(int(nums[j]))
        number.append(float(s1))
        s1=""
        stop_point = thing_index[i]+1
        number.append(thing[i])

    for i in range(thing_index[len(thing_index)-1]+1,len(nums)):
        s1 += str(int(nums[i]))
    number.append(float(s1))
    print number

    temp = 0
    for i in range(len(number)):
        if type(number[i]) is not float:
            if number[i] == "+":
                temp = number[i-1] + number[i+1]
            elif number[i] == "*":
                temp = number[i-1] * number[i+1]
            elif number[i] == "/":
                temp = number[i-1] / number[i+1]
            elif number[i] == "-":
                temp = number[i-1] - number[i+1]
            else:
                print "Wrong method"
            number[i+1] = temp
    return number[len(number)-1]

