import os

file1 = input("First file location: ")
file2 = input("Second file location: ")

def swap(first, second):
    fle1 = open(first, 'r')
    fle2 = open(second, 'r')
    data1 = fle1.readlines()
    data2 = fle2.readlines()
    fle1.close()
    fle2.close()
    fle1 = open(first, 'w')
    fle2 = open(second, 'w')
    fle1.write('')
    fle2.write('')

    for i in data1:
        fle2.write(i)
    for i in data2:
        fle1.write(i)

f_1 = os.path.exists(file1)
f_2 = os.path.exists(file2)

if(f_1 == True and f_2 == True):
    swap(file1, file2)
    print("Swapped files successfully")
else:
    print("Something went wrong")