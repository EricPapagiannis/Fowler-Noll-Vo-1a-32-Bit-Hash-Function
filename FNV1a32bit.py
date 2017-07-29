'''
3a
Give a hash table that contains the following seven names:
Albert, Danielle, Igor, Felix, Manfred, Olive, Walter
The hash table is an array of length 7 (valid indexes are from 0 to 6
inclusive), using chaining for collisions. Each hash value is obtained by:
• Convert the string to a sequence of ASCII values; the first letter is byte0
• Reminder: ASCII iscase-sensitive.
• Run it through 32-bit FNV-1a.
• mod 7.
As a check, Albert gets hashed to 3
'''
def FNV1a32bit(name):
    c = 2166136261
    for char in name:
        c = ((c ^ ord(char)) * 16777619) % (2 ** 32)
    return c

print("Albert: " + str(FNV1a32bit("Albert") % 7))     # Albert   -> 3
print("Danielle: " + str(FNV1a32bit("Danielle") % 7)) # Danielle -> 1
print("Igor: " + str(FNV1a32bit("Igor") % 7))         # Igor     -> 2
print("Felix: " + str(FNV1a32bit("Felix") % 7))       # Felix    -> 2
print("Manfred: " + str(FNV1a32bit("Manfred") % 7))   # Manfred  -> 2
print("Olive: " + str(FNV1a32bit("Olive") % 7))       # Olive    -> 1
print("Walter: " + str(FNV1a32bit("Walter") % 7))     # Walter   -> 1
'''
The hash table:
[0]
[1]->[Danielle]->[Olive]->[Walter]
[2]->[Igor]->[Felix]->[Manfred]
[3]->[Albert]
[4]
[5]
[6]
'''

'''
3b
Find and report one more English word or proper name that has the same second
letter as your last name’s, and collides with Albert if inserted into the above
hash table.
'''
last_name = "Papagiannis"
file_object  = open("/usr/share/dict/words", "r")
for line in file_object:
    my_index = FNV1a32bit(line.strip()) % 7
    albert_index = FNV1a32bit("Albert") % 7
    # Second letter is a, the collision will occur when my_index == 3
    if line[1] == last_name[1] and my_index == albert_index:
        print(line.strip(), my_index)
# The word I pick is Paula, when hashed, Paula is 3, which collides with Albert,
# and has the same second letter as my last name's, "a".
