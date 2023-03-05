


# Driver code
def main():
    inputs = [0, 5, 7, 10, 14]

    # Let's uncomment this to see the benefit of using dynamic programming with tabulation
    # inputs.append(60)

    for i in range(len(inputs)):
        print(str(i + 1) + ". " + str(inputs[i]) + "th Fibonacci number is:", get_fibonacci(inputs[i]))
        print("-" * 100, "\n", sep="")


if __name__ == "__main__":
    main()