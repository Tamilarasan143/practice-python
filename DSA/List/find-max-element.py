import enum
numbers = [10, 20 , 20 ,10 , 5]      


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

if __name__ == "__main__":
 print(find_max_element(numbers))
 print(find_second_largest(numbers))
 print(find_min_element(numbers))
 print(count_occurrences(numbers,10))
