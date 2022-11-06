countries = input().split(", ")
capitals = input().split(", ")
result = zip(countries, capitals)

result_dict = {key: value for key, value in result}

for country in result_dict.keys():
    print(f"{country} -> {result_dict[country]}")