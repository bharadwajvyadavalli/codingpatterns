# Scoring options are 1, 2, and 4



def main():
    total_scores = [3, 5, 10, 25, 0]

    # You can uncomment the line below and check how this bottom-up solution executes without a time-out

    # total_scores.append(35)

    for i in range(len(total_scores)):
        num_ways = scoring_options(total_scores[i])
        print(i + 1, ".", "\tNumber of ways to reach the score ", total_scores[i], ": ", num_ways, sep="")
        print("-" * 100)
        print()


if __name__ == '__main__':
    main()