# while 
# while exp_booleana
num = 1
while num <=10:
    print(num)
    num += 1 

#for -> interable
my_str = "hola"
for letter in my_str:
    print(letter, end='')
print()

my_list = ["a", "b", "c", 12]
for item in my_list:
    print(item, end='')
print()

# function range()
# range(fin)
for i in range(3):
    print (i, end='')
print()
#range(ini:fin)
for i in range(3, 6):
    print (i, end='')
print()
# range(ini:fin:step)
for i in range (1, 11, 2):
    print (i, end='')