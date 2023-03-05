


# driver code
def main():
    # input streams of IP addresses
    ip_addresses = ["0000", "25525511135", "12121212",
                    "113242124", "199219239", "121212", "25525511335"]

    # loop to execute till the lenght of input IP addresses
    for i in range(len(ip_addresses)):
        print(i + 1, ".\t Input addresses: '", ip_addresses[i], "'", sep="")
        print("\t Possible valid IP Addresses are: ",
              restore_ip_addresses(ip_addresses[i]), sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()