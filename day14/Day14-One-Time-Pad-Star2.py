
# coding: utf-8

# In[4]:

import hashlib

salt = 'ahsbgdzn'
index = 0
salt1 = 'abc'
hash_table = []
threes = []
keys = []
i = 0
key_found = False

while len(keys)<64:
    hash_input = salt + str(index)
    hash0 = hashlib.md5(hash_input).hexdigest()
    for x in range(2016):
        hash0 = hashlib.md5(hash0).hexdigest()
    #print i, hash_input, hash0
    hash_table.append(hash0)
    for three in threes:
        three[2] += 1
        x = 0
        five_found = False
        while x < (len(hash0)-4) and not five_found and three[2] < 1001 and three[3]:
            if hash0[x] == hash0[x+1] == hash0[x+2] == hash0[x+3] == hash0[x+4]:
                if hash0[x] == three[1]:
                    keys.append([three[0],hash_table[three[0]]])
                    five_found = True
                    print "KEY found:", three[0], hash_table[three[0]], three[2]
                    print i, hash_input, hash0
                    three[3] = False
            x +=1
    x = 0
    three_found = False
    while x < (len(hash0)-2) and not three_found:
        if hash0[x] == hash0[x+1] == hash0[x+2]:
            threes.append([i,hash0[x],0,True])
            three_found = True
            #print "One with three found:", i, hash_input, hash0
        x +=1
    i += 1
    index += 1
    
print "Numer of keys: %s" %len(keys)

x = 0
for key in keys:
    print x, key[0], key[1]
    x += 1

#print ""
#print "***************************************************************"
#print ""
#for three in threes:
#    print three[0], hash_table[three[0]], three[2], three[3]


# In[ ]:



