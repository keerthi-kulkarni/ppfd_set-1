def sort_numbers(numbers,reverse=False):
  return sorted(numbers,reverse=reverse)
my_list=[23,33,1,2,7]
print("Ascending order list: ",sort_numbers(my_list,reverse=False))
print("Descending order list: ",sort_numbers(my_list,reverse=True))