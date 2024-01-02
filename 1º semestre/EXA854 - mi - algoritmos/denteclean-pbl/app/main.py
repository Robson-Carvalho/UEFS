import sys

from dentist import dentist
from frontDesk import frontDesk

def main():
    args = sys.argv[1:]

    if (len(args)):
        if args[0] == "dentist":
            dentist()
        elif args[0] == "frontDesk":
            frontDesk()


if __name__ == "__main__":
    main()
