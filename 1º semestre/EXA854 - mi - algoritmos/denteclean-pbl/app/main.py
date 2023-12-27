import sys
from utils.chooseAccessType import chooseAccessType


def program(typeUser: str):
    print(typeUser)


def main():
    args = sys.argv[1:]

    if (len(args)):
        if args[0] == "dentist":
            return program(args[0])
        elif args[0] == "frontDesk":
            return program(args[0])

    program(chooseAccessType())


if __name__ == "__main__":
    main()
