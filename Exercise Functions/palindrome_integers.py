def palindrome(lst):
    for number in lst:
        if number == number[::-1]:
            print("True")
        else:
            print("False")


numbers_list_str = input().split(", ")
palindrome(numbers_list_str)
