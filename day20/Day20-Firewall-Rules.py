
# coding: utf-8

# In[47]:

def read_input(filename):
    with open(filename) as f:
        blocked = []
        for line in f:
            blocked_range = [int(line[:-1].split('-')[0]),int(line[:-1].split('-')[1])]
            blocked.append(blocked_range)
    return blocked

blocked = read_input('input.txt')
blocked = sorted(blocked)

highest_ip = 4294967295
not_blocked = []
num_allowed = 0
lnb = 0    #lowest not blocked

lnbc = lnb
for b in blocked:
    if b[0] <= lnbc <= b[1]:
        lnbc = b[1]+1

while lnbc != lnb:
    lnb = lnbc
    for b in blocked:
        if b[0] <= lnbc <= b[1]:
            lnbc = b[1]+1

print "Star 1. The lowest not blocked IP address is: %s" %lnb

high_reached = False
fiab = True
faib = lnb
fbib = 0
lbib = highest_ip
while not high_reached:
    if fiab:
        laib = highest_ip
        joint_blocks = False
        for b in blocked:
            if faib <= b[0] <= laib:
                laib = b[0]-1
                lbib = b[1]
                if faib == b[0]:
                    joint_blocks = True
        if not joint_blocks:
            not_blocked.append([faib,laib])
            num_allowed += (laib-faib+1)
        if laib == highest_ip:
            high_reached = True
        faib = lbib + 1
        fiab = False
    else:
        if len(not_blocked) > 0:
            fbib = not_blocked[-1][1]+1
        for b in blocked:
            if lbib > b[0] >= fbib and b[1] >= lbib:
                lbib = b[1]
        faib = lbib + 1
        fiab = True
        if lbib == highest_ip:
            high_reached = True
        
print "Star 2: Number of allowed IPs: %s" %num_allowed


# In[ ]:




# In[ ]:



