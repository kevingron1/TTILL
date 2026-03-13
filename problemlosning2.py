def ordered_list():
    for item in cars:
        cars.append(item, 1)
    return ordered_list

cars = ["Porsche", "Ferrari", "Lamborghini"]

print(ordered_list)