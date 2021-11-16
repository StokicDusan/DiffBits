from colorama import Fore, Back, Style, init
import sys, os
init()

def divide(string):
    return [char for char in string]

def main(filePath):
    file1 = open(filePath,'r')
    linije = file1.readlines()
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
    for i in range(0,len(linije)):
        output(linije[i],length,diff_array)

def output(string,length,diff_array):
    try:
        for i in range(0,length):
            if diff_array[i] == "d":
                print(Fore.WHITE + string[i], end="")
            elif diff_array[i] == "s":
                print(Fore.GREEN + string[i], end="")
            elif diff_array[i] == "l":
                print(Fore.YELLOW + string[i], end="")
    except IndexError:
        pass
    print()

if __name__ == "__main__":
    if(sys.argv[1:]):
        main(os.path.basename(sys.argv[1]))
    else:
        print("no file passed \n")
        pass
    print(Style.RESET_ALL)
