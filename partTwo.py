import math  

def main():
    print(pythag(int(input("Enter a side length: ")), int(input("Enter the other side length: "))))

def pythag(A,B):
    return math.sqrt(A**2 + B**2)

main()
