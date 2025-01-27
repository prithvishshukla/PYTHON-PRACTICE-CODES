# Recursive solution for Tower of Hanoi puzzle
def toh(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    toh(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}") 
    toh(n - 1, auxiliary, source, target)

def main():
    while True:
        try:
            n = int(input("Enter the number of disks: "))
            if n <= 0:
                print("Number of disks must be a positive integer. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    print("\nThe sequence of moves involved in the Tower of Hanoi are:")
    toh(n, 'A', 'B', 'C')
if __name__ == "__main__":
    main()
