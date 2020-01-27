#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # add condition that checks if the two dicts are the same length
  if len(recipe) != len(ingredients):
    return 0
  # declare variables
  greatest_possible_batches = 0
  counter = 0
  result_list = []
  recipe_list_values = list(recipe.values())
  ingredients_list_values = list(ingredients.values())
  # loop through each ingredient until the recipe value cant fit inside the ingredients value
  for index in range(len(recipe_list_values)):
    while recipe_list_values[index] <= ingredients_list_values[index]:
    
  # find out how many batches can be made for each ingredient
      ingredients_list_values[index] -= recipe_list_values[index]
      counter += 1
    result_list.append(counter)
    counter = 0
  
  # find the greatest common number between each ingredient
  greatest_possible_batches = min(result_list)

  # return the greatest possible number of batches
  return greatest_possible_batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5}
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))