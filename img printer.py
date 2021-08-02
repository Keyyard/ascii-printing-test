import time

def function():
    pic = open("me.txt", "r")
    lines = pic.read().splitlines()
    for line in lines:
        print(line)
        time.sleep(0.1)


def loading(load):
    while (load<100):
        print(load, "%")
        load +=1
        time.sleep(0.05)
        if (load%25==0):
            time.sleep(0.5)

quest1 = "Type out your full name to print your image: "
i = 0
load = 0
for char in quest1:
    time.sleep(0.1)
    print(quest1[i], end="")
    i += 1
x = 0
name = input()
while (name != "Trinh Hieu"):
    try_again = "Could you try again?: "
    for char in try_again:
        time.sleep(0.1)
        print(try_again[x], end="")
        x += 1
    x = 0
    name = input()
printing = "Printing the image..."
y = 0
for char in printing:
    time.sleep(0.1)
    print(printing[y], end="")
    y += 1
loading(load)
function()
input()