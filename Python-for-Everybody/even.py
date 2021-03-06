


nums = [45, 45, 23, 43, 78, 33, 44, 23]

def count_evens(num):
    even_count = 0
    odd_count = 0
    for num in nums:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print("Even numbers in the list: ", even_count)
    print("Odd numbers in the list: ", odd_count)

count_evens(nums)
