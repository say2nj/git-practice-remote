import sys

var1 = sys.argv[1]

a = 150
b = 20
a,b = b,a

def main():
    if var1:
        print('Hello World!')
    #else:
    #    print('No Way Here')

main()