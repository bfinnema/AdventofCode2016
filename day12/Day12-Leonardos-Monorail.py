
# coding: utf-8

# In[13]:

class Register:
    def __init__(self, name, val):
        self.name = name
        self.val = val
        self.jump = 0
        
    def get_name(self):
        return self.name
    
    def get_val(self):
        return self.val
    
    def set_reg(self,val):
        self.val = val
        
    def cpy(self,reg):
        self.val = reg.get_val()
        
    def inc(self):
        self.val += 1

    def dec(self):
        self.val -= 1
        
def read_input(filename):
    with open(filename) as f:
        instructions = []
        for line in f:
            str = line[:-1]
            instructions.append(str.split())
    return instructions

def exec_instr(pc):
    instr = instructions[pc]
    regval = 10
    for reg in registers:
        if instr[0] == 'cpy' and instr[2] in reg_list and reg.get_name() == instr[2]:
            creg = reg
        elif instr[0] == 'jnz':
            if instr[1] in reg_list2 and reg.get_name() == instr[1]:
                creg = reg
                regval = creg.get_val()
        elif (instr[0] == 'inc' or instr[0] == 'dec') and instr[1] in reg_list and reg.get_name() == instr[1]:
            creg = reg
    if instr[0] == 'cpy':
        if instr[1] in reg_list:
            for reg in registers:
                if reg.get_name() == instr[1]:
                    rreg = reg
            creg.cpy(rreg)
        else:
            creg.set_reg(int(instr[1]))
        pc += 1
    elif instr[0] == 'inc':
        creg.inc()
        pc += 1
    elif instr[0] == 'dec':
        creg.dec()
        pc += 1
    elif instr[0] == 'jnz':
        if regval != 0:
            pc += int(instr[2])
        else:
            pc += 1
    else:
        pc += 1
    return pc

instructions = read_input('input.txt')
reg_list = ['a','b','c','d']
reg_list2 = 'abcd'

registers = [Register('a',0),Register('b',0),Register('c',0),Register('d',0)]
program_counter = 0

while program_counter < len(instructions):
    program_counter = exec_instr(program_counter)

print "Star 1 RESULT:"
for reg in registers:
    print 'Register %s, Value %s' %(reg.get_name(),reg.get_val())

registers = [Register('a',0),Register('b',0),Register('c',1),Register('d',0)]
program_counter = 0

while program_counter < len(instructions):
    program_counter = exec_instr(program_counter)

print "Star 2 RESULT:"
for reg in registers:
    print 'Register %s, Value %s' %(reg.get_name(),reg.get_val())


# In[ ]:




# In[ ]:



