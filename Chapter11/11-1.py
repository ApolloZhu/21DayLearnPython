import os

lib = []

with open("lib.txt",encoding="utf-8") as file:
    lib += [line.strip().split(" ", 3) for line in file.readlines()]

if os.path.isdir("pho"):
    pho = [name.split(".",1) for name in os.listdir("pho")]
    for i, real, identifier, addr in lib:
        for name, extension in pho:
            if identifier == name:
                os.rename("pho/"+identifier+"."+extension, "pho/"+real+"."+extension)
                break
            elif real == name:
                break
        else:
            print("No photo for", real)
