<<<<<<< HEAD
from decorators import decor

@decor("green")
def welcome():
    print("Welcome to the File Handler Program!")

welcome()

=======
from file_stuff import FileCombiner
from decorators import color_text

@color_text
def print_msg(msg):
    return msg

if __name__ == "__main__":
    file1 = FileCombiner("file1.txt")
    file2 = FileCombiner("file2.txt")

    combined = file1 + file2

    print(print_msg("Files combined! Contents below:\n"))

    for line in combined.read_lines():
        print(line)
>>>>>>> ce8ba7d9c905e0742be7865e558e2fa2e255d720
