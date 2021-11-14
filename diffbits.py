from colorama import Fore, Back, Style, init
init()

def divide(string):
	return [char for char in string]

def main():
    string1 = input("String 1: ")
    string2 = input("String 2: ")

    print("")

    length = len(string1) if len(string1) > len(string2) else len(string2)
    diff_array = []
    for i in range(0,length):
        try:
            diff_array.append("d") if string1[i] != string2[i] else diff_array.append("s")
        except IndexError:
            diff_array.append("l")
    print(diff_array)
    output(string1,length,diff_array)
    print("")
    output(string2,length,diff_array)
    print("")

def output(string,length,diff_array):
	try:
		for i in range(0,length):
			if diff_array[i] == "d":
				print(Fore.WHITE + string[i], end="")
			if diff_array[i] == "s":
				print(Fore.GREEN + string[i], end="")
			if diff_array[i] == "l":
				print(Fore.YELLOW + string[i], end="")
	except IndexError:
		pass

main()
print(Style.RESET_ALL)
