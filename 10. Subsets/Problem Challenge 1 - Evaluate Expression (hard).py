'''

'''

#mycode



def main():
  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("1+2*3")))

  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("2*3-4-5")))


main()




#answer
def diff_ways_to_evaluate_expression(input):
  return diff_ways_to_evaluate_expression_rec({}, input)


def diff_ways_to_evaluate_expression_rec(map, input):
  if input in map:
    return map[input]

  result = []
  # base case: if the input string is a number, parse and return it.
  if '+' not in input and '-' not in input and '*' not in input:
    result.append(int(input))
  else:
    for i in range(0, len(input)):
      char = input[i]
      if not char.isdigit():
        # break the equation here into two parts and make recursively calls
        leftParts = diff_ways_to_evaluate_expression_rec(
          map, input[0:i])
        rightParts = diff_ways_to_evaluate_expression_rec(
          map, input[i+1:])
        for part1 in leftParts:
          for part2 in rightParts:
            if char == '+':
              result.append(part1 + part2)
            elif char == '-':
              result.append(part1 - part2)
            elif char == '*':
              result.append(part1 * part2)

  map[input] = result
  return result


def main():
  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("1+2*3")))

  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("2*3-4-5")))


main()



'''
Time complexity 
The time complexity of this algorithm will be exponential and will be similar to Balanced Parentheses. 
Estimated time complexity will be O(N*2^N) but the actual time complexity ( O(4^n/\sqrt{n}) ) is bounded by the Catalan number and is beyond the scope of a coding interview.

Space complexity 
The space complexity of this algorithm will also be exponential, estimated at O(2^N) though the actual will be ( O(4^n/\sqrt{n})).

Memoized version 
The problem has overlapping subproblems, 
as our recursive calls can be evaluating the same sub-expression multiple times. 
To resolve this, we can use memoization and store the intermediate results in a HashMap. 
In each function call, we can check our map to see if we have already evaluated this sub-expression before. 
'''
