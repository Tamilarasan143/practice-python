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
            

      
if __name__ == "__main__":
 print("Max Element",find_max_element(numbers))
 print("Second largest Element",find_second_largest(numbers))
 print("Min largest Element",find_min_element(numbers))
 print("Target Element counter",count_occurrences(numbers,10))
 print("Find first Element" , find_first_duplicate(numbers))
 print("Remove duplicates and return unique",remove_duplicates(numbers))
#  print("Missing patten Number",find_missing_number([1,2,3,5]))
find_missing_number([1,2,3,5])