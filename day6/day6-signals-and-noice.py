def read_input_message(filename):
    with open(filename) as f:
        positions = []
        for line in f:
            chars = []
            for char in line[:-1]:
                chars.append(char)
            positions.append(chars)
    return positions

def columns(positions):
    col = []
    x = 0
    for char in positions[0]:
        temp_col = ''
        for position in positions:
            temp_col += position[x]
        col.append(temp_col)
        x += 1
    return col

def most_freq_char(col):
    count_letters = []
    for l in set(col):
        count_letters.append([l,col.count(l)])
    return sorted(count_letters, key = lambda x: x[1], reverse=True)[0][0]

def least_freq_char(col):
    count_letters = []
    for l in set(col):
        count_letters.append([l,col.count(l)])
    return sorted(count_letters, key = lambda x: x[1], reverse=False)[0][0]

positions = read_input_message('message.txt')
cols = columns(positions)
word = ''
for col in cols:
    word += most_freq_char(col)

print "First part of day 6: The message is: %s" %word

word = ''
for col in cols:
    word += least_freq_char(col)

print "Second part of day 6: The message is: %s" %word

