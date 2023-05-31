#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    resultat = 0

    if len(sys.argv) > 1:
        for index in range(1, len(sys.argv)):
            resultat += int(sys.argv[index])

print("{:d}".format(resultat))
