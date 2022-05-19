import random # History Loop
import os # By Mondobe

prompts = []
with open("lines.txt") as file:
    prompts = file.readlines()
decades = []
decades += range(1770, 2020, 10)
cantuse = []
while True:
    os.system("clear")
    decade = random.choice(decades)
    decades.remove(decade)
    cantuse += [str(decade) + "s"]
    cantuse.sort()
    print("cannot use: " + str(cantuse) + ", prompt is: \n" +
          random.choice(prompts))
    input("ready?")