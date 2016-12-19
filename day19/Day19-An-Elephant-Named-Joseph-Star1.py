
# coding: utf-8

# In[5]:

num_elves = 3001330

elves = []
for i in range(num_elves):
    elves.append([i+1,1])

while len(elves) > 1:
    l = len(elves)
    for i in range(len(elves)):
        if elves[i][1] >0:
            elves[i][1] += elves[(i+1)%l][1]
            elves[(i+1)%l][1] = 0
    for i in range(len(elves)):
        l -= 1
        if elves[l][1] == 0:
            elves.pop(l)

print "Star 1: Elf %s gets all the presents" %(elves[0][0])


# In[ ]:



