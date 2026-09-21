numbers = [10, 5,5, 20, 5,]

def count_frequency(numbers: list[int]) -> dict[int, int]:
    frequency_map = {}
    for number in numbers:
        if number in frequency_map:
            frequency_map[number] +=1
        else:
            frequency_map[number] = 1
    return frequency_map


def find_most_frequent(numbers: list[int]) -> int:
    frequency_map = {}
    most_frequent_count = 0
    most_frequent_key = None
    for number in numbers:
        if number in frequency_map:
            frequency_map[number] +=1
        else:
            frequency_map[number] = 1

    for key , value in frequency_map.items():
         if value > most_frequent_count:
            most_frequent_count = value
            most_frequent_key = key

    return most_frequent_key    

def find_first_non_repeating(numbers: list[int]) -> int:
    frequency_map = {}

    for number in numbers:
        if number in frequency_map:
            frequency_map[number] +=1
        else:
            frequency_map[number] = 1

    for number in numbers:
       if frequency_map[number] == 1:
           return number
def find_first_repeating(numbers: list[int]) -> int:
    frequency_map = {}
    for number in numbers:
        if number in frequency_map:
                return number
        else:
            frequency_map[number] = 1

def two_sum(numbers: list[int], target: int) -> list[int]:
     sum_map = {}
     for index , number in enumerate(numbers):
        needed =  target - number
        if needed in sum_map:
            return [sum_map[needed],index]
        else:
            sum_map[number] = index

def has_pair_with_sum(numbers: list[int], target: int) -> bool:
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return False


if __name__ == "__main__":
  print("Count Frequency",count_frequency(numbers))
  print("Most Frequency element",find_most_frequent(numbers))
  print("first Non Frequency element",find_first_non_repeating(numbers))
  print("fits Frequency element",find_first_repeating(numbers))
  print("two sum",two_sum([7, 11, 15,2],9))
  print("has_pair_with_sum",has_pair_with_sum([1, 2, 3, 4, 6, 8, 9],11))