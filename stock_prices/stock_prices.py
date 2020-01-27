#!/usr/bin/python

import argparse

prices_list = [1050, 270, 1540, 3800, 2]
prices_list_2 = [100, 90, 80, 50, 20, 10]

def find_max_profit(prices):
  # declare necessary variables and set variable equal to first index
  temp = 0
  current_min_price_so_far = prices[temp]
  max_profit_so_far = 0

  # loop through prices list
  for x in range(len(prices)-1):
    for index in range(1, len(prices)-1):

  # find the difference between the first index and the rest of the indices
      if prices[index] - current_min_price_so_far > max_profit_so_far:
        max_profit_so_far = (prices[index] - current_min_price_so_far)
  # repeat until all possible comparaisons have been made
  # (THIS STEP WAS IMPLIMETED ON LINE 14 BY ADDING ANOTHER FOR LOOP)
      print("index: ", prices[index], " - ", current_min_price_so_far)
      print("list: ", prices)
      print("profit: ", max_profit_so_far)
  # return the greatest profit
    print(temp)
    temp += 1
    current_min_price_so_far = prices[temp]
  return max_profit_so_far

print(find_max_profit(prices_list_2))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))