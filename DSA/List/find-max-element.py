import enum
numbers = [10,10 ,20 , 20  , 5]      


def find_max_element(numbers:list[int]):
    if len(numbers) <= 1 :
        return numbers
    max_element = numbers[0]
    for number in numbers:
        if max_element < number:
          max_element = number
    return max_element
def find_second_largest(numbers:list[int]):
    if not numbers:
        raise ValueError("List can not be empty")
    max_element = numbers[0]
    second_element = None
    #breakpoint()
    for number in numbers[1:]:
        if number > max_element:
            second_element = max_element
            max_element = number
        elif number != max_element and (second_element is None or number > second_element):
             second_element = number
    if second_element is None:
      raise ValueError("No second largest distinct element")
    return second_element
            
            
def find_min_element(numbers: list[int]) -> int:
    if not numbers:
        raise ValueError("List can not be empty")
    min_element = numbers[0]
    for number in numbers:
        if number < min_element:
            min_element = number

    return min_element

def count_occurrences(numbers: list[int], target: int) -> int:
   if not numbers:
        raise ValueError("List can not be empty")
   counter = 0
   for number in numbers:
    if number == target:
        counter += 1

   return counter

def find_first_duplicate(numbers: list[int]) -> int:
    unique_element = set()
    first_duplicate = None
    for number in numbers:
        if number in unique_element and first_duplicate is None:
            first_duplicate = number
        unique_element.add(number)
    if first_duplicate is None:
        raise ValueError("There is no duplicates found in this list")
    return first_duplicate 

def remove_duplicates(numbers: list[int]) -> list[int]:
      unique_element = set()
      unique_element_list = list()
      for number in numbers:
        if number not in unique_element:
            unique_element_list.append(number)
        unique_element.add(number)
      return  unique_element_list
      
def find_missing_number(numbers: list[int]) -> int:
    n = len(numbers) + 1

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)

    return expected_sum - actual_sum
            
def group_anagrams(words: list[str]) -> list[list[str]]:
    groups= {}
    for word in words:
        key = "".join(sorted(word))
        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]
    return list(groups.values())

def reverse_array(numbers: list[int]) -> list[int]:
    left = 0
    right = len(numbers) - 1

    while left < right:
       numbers[left] , numbers[right] = numbers[right] , numbers[left]
       left += 1
       right -= 1

    return numbers
def is_palindrome(numbers: list[int]) -> bool:
   left = 0
   right = len(numbers) - 1

   while left < right:

    if numbers[left] != numbers[right]:
        return False

    left += 1
    right -= 1

   return True

def remove_duplicates(numbers: list[int]) -> int:
  slow = 0
  for fast in range(1, len(numbers)):
    if numbers[slow] != numbers[fast]:
        slow +=1
        numbers[slow] = numbers[fast]
  return numbers[:slow]


def move_zeroes(numbers: list[int]) -> list[int]:
    slow = 0
    for fast in range(len(numbers)):
        if numbers[fast] != 0:
           numbers[slow] = numbers[fast]
           slow += 1
    
    for index in range(slow, len(numbers)):
        numbers[index] = 0

    return numbers

def max_subArray_sum(numbers: list[int], k: int) -> int:
    n = len(numbers)
    if n <= k:
       return -1
    window_sum = sum(numbers[:k])
    max_sum = window_sum
    for index in range(n-k):
        print("index",index)
        window_sum = window_sum - numbers[index] + numbers[index + k]
        max_sum = max(window_sum,max_sum)
    return max_sum

def min_subarray_length(numbers: list[int], target: int) -> int:
   left = 0
   window_sum = 0
   min_length = float("inf")
   right = 0

   for right in range(len(numbers)):

       window_sum += numbers[right]
       right = right
       while window_sum >= target:
        # update minimum 
        min_length = min(min_length , right - left + 1)
        window_sum -= numbers[left]
        left += 1
   return min_length
def longest_two_distinct(numbers: list[int]) -> int:


    left = 0
    frequency = {}
    max_length = 0

    for right in range(len(numbers)):

        key = numbers[right]
        frequency[key] = frequency.get(key, 0) + 1

        while len(frequency) > 2:

            frequency[numbers[left]] -= 1

            if frequency[numbers[left]] == 0:
                del frequency[numbers[left]]

            left += 1

        window_length = right - left + 1
        max_length = max(max_length, window_length)

    return max_length

def build_prefix_sum(numbers: list[int]) -> list[int]:
    prefix = [0]

    for number in numbers:
     prefix.append(prefix[-1] + number)

    return prefix

#def range_sum(prefix: list[int], left: int, right: int) -> int:
if __name__ == "__main__":
 print("Max Element",find_max_element(numbers))
 print("Second largest Element",find_second_largest(numbers))
 print("Min largest Element",find_min_element(numbers))
 print("Target Element counter",count_occurrences(numbers,10))
 print("Find first Element" , find_first_duplicate(numbers))
 print("Remove duplicates and return unique",remove_duplicates(numbers))
 print("Missing patten Number",find_missing_number([1,2,3,5]))
 print("Group by words",group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
 print("Reverse Array", reverse_array([1,2,3,4,5]))
 print("is_palindrome", is_palindrome([1, 2, 3, 2, 1]))
 print("remove_duplicates",remove_duplicates([1,1,2,2,3,4,3,4]))
 print("move_zeroes",move_zeroes([0, 1, 0, 3, 12]))
 print("max_subArray_sum",max_subArray_sum([2, 1, 5, 1, 3, 2],3))
 print("min_subarray_length",min_subarray_length([2, 3, 1, 2, 4, 3], 7))
 print("longest_two_distinct",longest_two_distinct([1,2,1,2,3]))
 print("build_prefix_sum",build_prefix_sum([2, 4, 1, 5, 3]))