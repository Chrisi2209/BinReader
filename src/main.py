import os
import sys

def show_binary():
    # if no path 
    try:
        if sys.argv[1] == "--help":
            print("""Program for showing binary files.
Pass the path to your binary file as the first argument.
Optionally you can use the arguments "bin", "dec" or "hex" after
the path to display the numbers in binary, decimal or hexa-decimal.
If no such argument is given, it defaults to hex.""")
        bin_file = sys.argv[1]
    except(IndexError):
        # if there is no path, error
        print("No path was given. Try --help")
        return

    # function to convert the bytes object into a string
    # if it is hex, a hex representation will be printed
    # if it is bin, a bin representation will be printed
    base_func = hex
    number_zfill = 2  # how many digits each number has
    if len(sys.argv) == 3:
        if sys.argv[2] == "bin":
            base_func = bin
            number_zfill = 8
        elif sys.argv[2] == "dec":
            base_func = lambda x: "0d" + str(x)
            number_zfill = 3
        elif sys.argv[2] == "hex":
            base_func = hex
            number_zfill = 2
        else:
            print("Invalid arguments")
            return
    
    
    with open(bin_file, "rb") as f:
        for byte in f.read():
            # get the bin/hex string of the byte
            binary_string = base_func(byte)[2:].zfill(number_zfill)

            # the binary file is printed out
            print(binary_string, end=" ")
        # go to next line after line ends
        print()


if __name__ == "__main__":
    show_binary()