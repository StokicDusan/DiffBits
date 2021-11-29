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
    for linija in linije:
        output(linija,diff_array)

def output(linija,diff_array):
    try:
        for linija,diff in zip(linija, diff_array):
            if diff == "d":
                print(Fore.WHITE + linija, end="")
            elif diff == "s":
                print(Fore.GREEN + linija, end="")
            elif diff == "l":
                print(Fore.YELLOW + linija, end="")
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
