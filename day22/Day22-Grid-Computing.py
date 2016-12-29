
# coding: utf-8

# In[27]:

import numpy as np

def read_input(filename):
    with open(filename) as f:
        storage_nodes = []
        for line in f:
            node = []
            if line.startswith('dev',1,4):
                lsplit = line.split()
                name_split = lsplit[0].split('-')
                x = int(name_split[1][1:])
                if x > biggest[0]: biggest[0] = x
                y = int(name_split[2][1:])
                if y > biggest[1]: biggest[1] = y
                node = [[x,y],int(lsplit[1][:-1]),int(lsplit[2][:-1]),int(lsplit[3][:-1]),int(lsplit[4][:-1])]
                storage_nodes.append(node)
                size[x,y] = int(lsplit[1][:-1])
                used[x,y] = int(lsplit[2][:-1])
                avail[x,y] = int(lsplit[3][:-1])
    return storage_nodes

biggest = [0,0]
#size = 32*[28*[0]]
size = np.zeros((32,28))
used = np.zeros((32,28))
avail = np.zeros((32,28))
storage_nodes = read_input('input.txt')

print "Biggest x: %s" %biggest[0]
print "Biggest y: %s" %biggest[1]
viable_pairs = []
s = storage_nodes
for i in range(len(storage_nodes)):
    for j in range(i+1,len(storage_nodes)):
        if (s[i][2] > 0 and s[i][2] < s[j][3]) or (s[j][2] > 0 and s[j][2] < s[i][3]):
            viable_pairs.append([s[i],s[j]])
            
print "Star 1: Number of viable pairs: %s" %len(viable_pairs)

def move(xm,ym,p0):
    print "p0: %s.   Node with zero: %s,%s,%s.   Node to copy from: %s,%s,%s" %(p0,size[p0[0],p0[1]],used[p0[0],p0[1]],avail[p0[0],p0[1]],size[p0[0]+xm,p0[1]+ym],used[p0[0]+xm,p0[1]+ym],avail[p0[0]+xm,p0[1]+ym])
    if used[p0[0]+xm,p0[1]+ym] <= avail[p0[0],p0[1]]:
        used[p0[0],p0[1]] = used[p0[0]+xm,p0[1]+ym]
        used[p0[0]+xm,p0[1]+ym] = 0
        avail[p0[0]+xm,p0[1]+ym] = size[p0[0]+xm,p0[1]+ym]
        avail[p0[0],p0[1]] = size[p0[0],p0[1]] - used[p0[0],p0[1]]
        return True
    else:
        return False

def ok_to_go(xm,ym,p0):
    if used[p0[0]+xm,p0[1]+ym] <= avail[p0[0],p0[1]]:
        return True
    else:
        return False

num_steps = 0
empty_node = [24,22]
pos = [24,22]
print used[p0[0],p0[1]]
pg = biggest
print ""
print "Number of steps so far: %s" %num_steps
print "Going up"
reached_lowy = False
problem_found = False
while not reached_lowy and not problem_found:
    if move(0,-1,pos):
        pos = [pos[0],pos[1]-1]
        print "Position now: %s" %pos
        num_steps += 1
    else:
        print "SHIT! Houston, we got a problem. Going left"
        if move(-1,0,pos):
            pos = [pos[0]-1,pos[1]]
            #print "Position now: %s" %pos
            num_steps += 1
        else:
            problem_found = True
            print "SHIT! Houston, we got a problem"
    if pos[1] == 0:
        reached_lowy = True

print ""
print "Number of steps so far: %s" %num_steps
print "Going right"
reached_highx = False
problem_found = False
while not reached_highx and not problem_found:
    if move(1,0,pos):
        pos = [pos[0]+1,pos[1]]
        #print "Position now: %s" %pos
        num_steps += 1
    else:
        problem_found = True
        print "SHIT! Houston, we got a problem"
    if pos[0] == pg[0]:
        reached_highx = True
    
print ""
print "Number of steps so far: %s. Position now: %s" %(num_steps,pos)
print "Now starting to move the target left towards 0,0"

reached_home = False
problem_found = False
while not reached_home and not problem_found:
    print ""
    ok_to_go_left = False
    while not ok_to_go_left and not problem_found:
        if move(0,1,pos):
            pos = [pos[0],pos[1]+1]
            print "Position now: %s" %pos
            num_steps += 1
            if ok_to_go(-1,0,pos):
                ok_to_go_left = True
        else:
            problem_found = True
            print "SHIT! Houston, we got a problem"
    i = 0
    ok_to_go_down = False
    if not problem_found:
        while (ok_to_go_left and i < 2 and not problem_found) or (ok_to_go_left and i >= 2 and not ok_to_go_down and pos[0]>=0 and not problem_found):
            print "Going left"
            if move(-1,0,pos):
                pos = [pos[0]-1,pos[1]]
                print "Position now: %s" %pos
                num_steps += 1
                i += 1
                if ok_to_go(0,-1,pos):
                    ok_to_go_down = True
            else:
                print "SHIT! Houston, we got a problem. Going further up"
                if move(0,1,pos):
                    pos = [pos[0],pos[1]+1]
                    print "Position now: %s" %pos
                    num_steps += 1
                else:
                    problem_found = True
                    print "SHIT! Houston, we got a problem"
        print "Going down towards x=0"
        while pos[1] != 0 and not problem_found:
            if move(0,-1,pos):
                pos = [pos[0],pos[1]-1]
                print "Position now: %s" %pos
                num_steps += 1
            else:
                problem_found = True
                print "SHIT! Houston, we got a problem"
        print "Going right"
        while i > 1  and not problem_found:
            if move(1,0,pos):
                pos = [pos[0]+1,pos[1]]
                print "Position now: %s" %pos
                num_steps += 1
                i -= 1
            else:
                problem_found = True
                print "SHIT! Houston, we got a problem"
    if pos == [1,0]:
        reached_home = True
        
print "Star 2: Number of steps: %s" %num_steps


# In[ ]:



