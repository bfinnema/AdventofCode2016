
# coding: utf-8

# In[11]:

import itertools

class Scrambler:
    def __init__(self,operations,password):
        self.operations = operations
        self.pw = password
        self.scrambled_pw = password
        self.ops_counter = 0
        self.__ops_set = {
            'swap position': self.__swap_position,
            'swap letter': self.__swap_letter,
            'rotate left': self.__rotate_left,
            'rotate right': self.__rotate_right,
            'rotate based': self.__rotate_posbas,
            'reverse positions': self.__reverse_positions,
            'move position': self.__move_position
        }
        
    def __swap_position(self,q,s1,s2,z):
        p = self.pw
        x = int(q)
        y = int(z)
        if y > x:
            p = p[0:x]+p[y]+p[x+1:y]+p[x]+p[y+1:]
        if x > y:
            p = p[0:y]+p[x]+p[y+1:x]+p[y]+p[x+1:]
        self.pw = p
        
    def __swap_letter(self,a,s1,s2,b):
        p = self.pw
        for i in range(len(p)):
            if p[i] == a:
                x = i
            if p[i] == b:
                y = i
        if y > x:
            p = p[0:x]+p[y]+p[x+1:y]+p[x]+p[y+1:]
        if x > y:
            p = p[0:y]+p[x]+p[y+1:x]+p[y]+p[x+1:]
        self.pw = p
        
    def __rotate_left(self,q,s1):
        x = int(q)
        self.pw = self.pw[x:] + self.pw[:x]
        
    def __rotate_right(self,q,s1):
        x = int(q)
        self.pw = self.pw[-x:] + self.pw[:-x]
        
    def __rotate_posbas(self,s1, s2, s3, s4,a):
        p = self.pw
        for i in range(len(p)):
            if p[i] == a:
                x = i
        p = p[-1] + p[:-1]
        p = p[-x:] + p[:-x]
        if x >= 4:
            p = p[-1] + p[:-1]
        self.pw = p
        
    def __reverse_positions(self,q,s1,z):
        p = self.pw
        x = int(q)
        y = int(z)
        p = p[:x] + p[x:y+1][::-1] + p[y+1:]
        self.pw = p
        
    def __move_position(self,q,s1,s2,z):
        p = self.pw
        x = int(q)
        y = int(z)
        if y > x:
            p = p[:x] + p[x+1:y+1] + p[x] + p[y+1:]
        else:
            p = p[:y] + p[x] + p[y:x] + p[x+1:]
        self.pw = p
        
    def __execute(self):
        operation = self.operations[self.ops_counter].split()
        self.ops_counter += 1
        ops = operation[0] + ' ' + operation[1]
        self.__ops_set[ops](*operation[2:])

    def run(self):
        while self.ops_counter < len(self.operations):
            self.__execute()

def read_input(filename):
    with open(filename) as f:
        operations = []
        for line in f:
            operations.append(line[:-1])
    return operations

def star1(operations,pw_input):
    scrambler = Scrambler(operations,pw_input)
    scrambler.run()
    return scrambler.pw

def star2(operations,scr_pw):
    all_pw = list(itertools.permutations(["a", "b", "c", "d", "e", "f", "g", "h"]))
    passwords = []
    for i in all_pw:
        uns_pw = i[0] + i[1] + i[2] + i[3] + i[4] + i[5] + i[6] + i[7]
        scrambler = Scrambler(operations,uns_pw)
        scrambler.run()
        if scrambler.pw == scr_pw:
            print "Found the un-scrambled password: %s" %uns_pw
            passwords.append(uns_pw)
    return passwords

if __name__ == '__main__':
    INPUT = read_input('./input.txt')
    pw_input = 'abcdefgh'
    print("Star 1: ", star1(INPUT,pw_input))
    scr_pw = 'fbgdceah'
    print("Star 2: ", star2(INPUT,scr_pw))


# In[ ]:




# In[ ]:



