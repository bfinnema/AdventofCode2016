
# coding: utf-8

# In[31]:

num_elves = 3001330

elves = []
for i in range(num_elves):
    elves.append([i,1])

while len(elves) > 1:
    l = len(elves)
    etg = l/2
    elves[0][1] += elves[etg][1]
    elves.pop(etg)
    elf = elves.pop(0)
    elves.append(elf)
    
print "Star 2: Elf %s gets all the presents" %(elves[0][0]+1)


# In[ ]:



