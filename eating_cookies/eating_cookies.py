#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  # declare variables
  counter = 0

  # declare base cases
  if n < 0:
    return 0
  elif n == 1 or n == 0:
    return 1
  elif n == 2:
    return 2

  # if not a base case, loop through 
  else:
    list_1 = [1, 1, 2]
    for x in range(2, n):
      print(list_1)
      counter = list_1[-1] + list_1[-2] + list_1[-3]
      list_1.append(counter)
  return counter

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')