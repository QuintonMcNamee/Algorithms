#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # declare variables
  shoot = ['rock', 'paper', 'scissors']
  result = []
  temp = []

  # create recursive function
  def rps_recursive(x, temp=[]):

  # create base case
    if x == 0:
      return result.append(temp)
  
  # loop through rock, paper, scissors list
    for index in shoot:
      
  # call recursive function
      rps_recursive(x - 1, temp + [index])

  # call recursive function again
  rps_recursive(n)

  # return result
  return result

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')