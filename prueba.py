fh = open("burger-king-items.txt")
for line in fh:
    if line.startswith('Item'): continue
    words = line.split()
    item = words[0]
    print(item)

    serving_size = words[1]
    calories = words[2]
    fat_cal = words[3]
    protein = words[4]
    fat = words[5]
    sat_fat = words[6]
    trans_fat = words[7]
    chol = words[8]
    sodium = words[9]
    carbs = words[10]
    fiber = words[11]
    sugar = words[12]
    meat = words[13]
    breakfast = words[14]
    not_breakfast = words[15]
    carbsxmeat = words[16]

    print(serving_size, calories, fat_cal)
