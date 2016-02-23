from sys import argv

if len(argv) != 4:
    print "Number of args not equal to 3..."
    exit(0)

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

