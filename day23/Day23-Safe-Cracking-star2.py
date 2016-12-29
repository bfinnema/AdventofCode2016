
# coding: utf-8

# In[1]:

from collections import defaultdict

def read_instructions(filename):
    content = []
    with open(filename) as input_file:
        for lines in input_file:
            content.append(lines[:-1])
    return content

class BunnyComputer():
    def __init__(self, instruction_list):
        self.instruction_list = instruction_list
        self.program_counter = 0
        self.num_instr_exec = 0
        self.tgl_pc = 0
        self.registers = defaultdict(int)
        self.__instr_set = {
            'cpy': self.__cpy,
            'inc': self.__inc,
            'dec': self.__dec,
            'jnz': self.__jnz,
            'tgl': self.__tgl
        }
        self.__tgl_instr = {
            'cpy': self.__cpy_tgl,
            'inc': self.__inc_tgl,
            'dec': self.__dec_tgl,
            'jnz': self.__jnz_tgl,
            'tgl': self.__tgl_tgl
        }

    def __cpy(self, x, y):
        if x.isalpha() and y.isalpha():
            x = self.registers[x]
            self.registers[y] = int(x)
        elif x.isalpha():
            fake = 0   # Do nothing
            #self.registers[x] = int(y)
        elif y.isalpha():
            self.registers[y] = int(x)
        else:
            fake = 0   # Do nothing

    def __inc(self, x):
        if self.program_counter == 5:
            self.registers[x] += (self.registers['b'] * self.registers['d'])
        else:
            self.registers[x] += 1

    def __dec(self, x):
        self.registers[x] -= 1

    def __jnz(self, x, y):
        if x.isalpha():
            x = self.registers[x]
        if y.isalpha():
            y = self.registers[y]
        if int(x) != 0:
            self.program_counter += int(y) - 1
            
    def __tgl(self, x):
        self.tgl_pc = self.program_counter + self.registers[x]-1
        if self.tgl_pc < len(self.instruction_list):
            instr_reg = self.instruction_list[self.tgl_pc].split()
            self.__tgl_instr[instr_reg[0]](*instr_reg[1:])
        
    def __cpy_tgl(self, x, y):
        self.instruction_list[self.tgl_pc] = "jnz "+x+" "+y
        
    def __inc_tgl(self, x):
        self.instruction_list[self.tgl_pc] = "dec "+x
        
    def __dec_tgl(self, x):
        self.instruction_list[self.tgl_pc] = "inc "+x
        
    def __jnz_tgl(self, x, y):
        self.instruction_list[self.tgl_pc] = "cpy "+x+" "+y
        
    def __tgl_tgl(self, x):
        self.instruction_list[self.tgl_pc] = "inc "+x

    def __execute(self):
        instruction_register = self.instruction_list[self.program_counter].split()
        self.program_counter += 1
        self.num_instr_exec += 1
        self.__instr_set[instruction_register[0]](*instruction_register[1:])

    def run(self):
        while self.program_counter < len(self.instruction_list): # and self.num_instr_exec < 200:
            self.__execute()

def star2(inst_list):
    monorail = BunnyComputer(inst_list)
    monorail.registers["a"] = 12
    monorail.run()
    return monorail.registers["a"]

if __name__ == '__main__':
    INPUT = read_instructions('./input.txt')
    print("Star 2: ", star2(INPUT))


# In[ ]:



