import sys
from script import run

if len(sys.argv) == 2:
    run(sys.argv[1])
elif len(sys.argv) == 1:
    run(input("please enter the filename of an mdl script file: \n"))
else:
    print("Too many arguments.")



# run("test.mdl")

# colors = ["shiny_purple", "shiny_teal", "dull_yellow", "orange", "red"]
#
# def ef(x):
#   return int(round((-0.00749 * x * x) + (3.22875 * x) + 93.54545))
#
# startX = 450
# endX = -12.5
# numImages = 100
# dx = ((endX - startX) * 1.0 / numImages)
# x = startX - dx
# for i in range(1, numImages + 1):
#   print(i)
#   cIndex = i//4 % len(colors)
#   x += dx
#   x = int(round(x))
#   y = ef(x)
#   with open("basketball.mdl", "r") as f:
#     lines = f.readlines()
#   for j,line in enumerate(lines):
#     line = line.strip().split(" ")
#     if line[0] == "save":
#       line[1] = "pic" + str(i) + ".png\n"
#       lines[j] = " ".join(line)
#     if line[0] == "sphere":
#       line[1],line[2],line[3] = colors[cIndex],str(x),str(y)
#       lines[j] = " ".join(line) + "\n"
#   with open("basketball.mdl", "w") as f: f.writelines(lines)
#   run("basketball.mdl")
