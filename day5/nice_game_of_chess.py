import hashlib

print hashlib.md5("abc3231929").hexdigest()
door_id = "uqwqemis"
index = 0
num_pw_char = 0
pw = ""
print ""

run1 = True
if run1:
    while num_pw_char < 8:
        right_hash_found = False
        while not right_hash_found:
            hash_input = door_id + str(index)
            #print hash_input
            hash0 = hashlib.md5(hash_input).hexdigest()
            #print hash0
            index += 1
            #print hash0[:5]
            if hash0[:5] == "00000":
                right_hash_found = True
                print "hash0: %s, index: %s" %(hash0,index)
        pw += hash0[5]
        num_pw_char += 1

    print pw

pw2 = ['-','-','-','-','-','-','-','-']
num_pw_char = 0
index = 0
while num_pw_char < 8:
    right_hash_found = False
    while not right_hash_found:
        hash_input = door_id + str(index)
        hash0 = hashlib.md5(hash_input).hexdigest()
        index += 1
        if hash0[:5] == "00000":
            print "hash0: %s, index: %s" %(hash0,index)
            if hash0[5] in "01234567" and pw2[int(hash0[5])] == '-':
                right_hash_found = True
                pw2[int(hash0[5])] = hash0[6]
                print pw2
    num_pw_char += 1

print pw2
password = ''
for l in pw2:
    password += l
print password

