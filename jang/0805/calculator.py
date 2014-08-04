from mine import calculate as cal

demand = raw_input()
demand_list = []
things =[]
nums = []
thing_index = []
for i in demand:
    demand_list.append(i)

cal.devider(things,demand_list,nums,thing_index)
print cal.calculating(things,nums,thing_index)