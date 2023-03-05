


# Driver code to test the above function
if __name__ == '__main__':

    n_list = [0, 1, 2, 4, 6]

    # Let's uncomment this to see the benefit of using dynamic programming with tabulation
    # n_list.append(22)

    for i in range(len(n_list)):
        print(i + 1, ".\tn: ", n_list[i], sep="")
        print("\n\tnth catalan number:", catalan(n_list[i]))
        print('-' * 100)