hours = [12,12,38,24,24]
days = 0

for i in range(len(hours)):
    for j in range(i+1,len(hours)):
        sum_days = hours[i] + hours[j]
        if sum_days % 24 == 0:
            days += 1

print(days)

