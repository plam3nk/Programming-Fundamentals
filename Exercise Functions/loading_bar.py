def loading_bar(num):
    count = num / 10
    loading_list = []
    for dot in range(1, 10 + 1):
        if count >= dot:
            loading_list.append("%")
        else:
            loading_list.append(".")
    bar = ("".join(loading_list))
    if count == 10:
        print("100% Complete!")
        print(f"[{bar}]")
    else:
        print(f"{num}% [{bar}]")
        print("Still loading...")


input_number = int(input())
loading_bar(input_number)
