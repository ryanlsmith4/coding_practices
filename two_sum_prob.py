my_list = [1, 6, 4, 8, 9, 3]
my_target = 10


def two_sum(list, target):
  first = None
  second = None 

  for num in list:
    desired = target - num

    if desired in list:
      second = list.index(desired)

    if num + desired == target:
      first = list.index(num)
      return [list[first], list[second]]

    return 'None Found'
      
  

if __name__ == "__main__":
    print(two_sum(my_list, my_target))