
# coding: utf-8

# In[38]:

def read_input_rooms(filename):
    with open(filename) as f:
        for line in f:
            rooms.append(line)
    return rooms

def decode_rooms(rooms):
    sectorid_sum = 0
    for room in rooms:
        #print ""
        #print room[:-1]
        room_split = room[:-1].split('-')
        secid_checksum = room_split.pop(-1)
        enc_name = ""
        for x in room_split:
            enc_name += x
        #print enc_name
        enc_name_set = set(enc_name)
        #print enc_name_set
        count_letters = []
        for l in enc_name_set:
            count_letters.append([l,enc_name.count(l)])
        #print count_letters
        count_letters_sorted1 = sorted(count_letters)
        #print count_letters_sorted1
        count_letters_sorted = sorted(count_letters_sorted1, key = lambda x: x[1], reverse=True)
        #print count_letters_sorted
        calculated_checksum = count_letters_sorted[0][0]+count_letters_sorted[1][0]+count_letters_sorted[2][0]+count_letters_sorted[3][0]+count_letters_sorted[4][0]
        #print calculated_checksum
        si_cs = secid_checksum.split('[')
        sectorid = int(si_cs[0])
        checksum = si_cs[1][:-1]
        #print "sectorid: %s, checksum: %s" %(sectorid, checksum)
        rooms_decoded.append([enc_name,sectorid,checksum])
        if checksum == calculated_checksum:
            sectorid_sum += sectorid
            #print sectorid_sum
#        else:
#            print ""
#            print room[:-1]
#            print enc_name
#            print enc_name_set
#            print count_letters_sorted
#            num = 0
#            for x in count_letters_sorted:
#                num += x[1]
#            print "number of letters in enc_name: %s, sum in count_letters_sorted: %s" %(len(enc_name), num)
#            print calculated_checksum
#            print "sectorid: %s, checksum: %s" %(sectorid, checksum)
    
    return sectorid_sum

def shift_letter(letter,sectorid):
    mod_si = sectorid%26
    #new_letter = chr((ord(letter)+mod_si-96)%26+96)
    #print "Letter: %s, sectorid: %s, modulus si: %s, new_letter: %s" %(letter,sectorid,mod_si,new_letter)
    return chr((ord(letter)+mod_si-96)%26+96)

def decrypt_room_name(room_decoded):
    decrypted_room_name = ""
    for l in room_decoded[0]:
        decrypted_room_name += shift_letter(l,room_decoded[1])
    return decrypted_room_name

rooms = []
rooms = read_input_rooms("rooms.txt")
#print rooms

rooms_decoded =[]
sectorid_sum = decode_rooms(rooms)
print sectorid_sum
#print rooms_decoded

for room in rooms_decoded:
    decrypted_room_name = decrypt_room_name(room)
    room.append(decrypted_room_name)
    if decrypted_room_name[:5] == "north":
        print room
    #print decrypted_room_name

#for room in rooms_decoded:
#    print room
#print rooms_decoded


# In[ ]:



