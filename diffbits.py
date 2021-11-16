from colorama import Fore, Back, Style, init
from sys import argv
from os import path
init()

def main(filePath):
    with open(filePath,'r') as f:
        linije = f.readlines()
    length = 0
    for i in range(0,len(linije)):
        linije[i]=linije[i].rstrip()
        length = len(linije[i]) if len(linije[i]) > length else length
    diff_array = []
    for i in range(0,length):
        try:
            diff_array.append("s") if all(str(item[i])=='0' for item in linije) or all(str(item[i])=='1' for item in linije) else diff_array.append("d")
        except IndexError:
            diff_array.append("l")
    for item in linije:
        output(item,diff_array)

def output(string,diff_array):
    try:
        for diff,string in zip(diff_array, string):
            if diff == "d":
                print(Fore.WHITE + string, end="")
            elif diff == "s":
                print(Fore.GREEN + string, end="")
            elif diff == "l":
                print(Fore.YELLOW + string, end="")
    except IndexError:
        pass
    print()

if __name__ == "__main__":
    if(argv[1:]):
        main(path.basename(argv[1]))
    else:
        print("no file passed \n")
        pass
    print(Style.RESET_ALL)
