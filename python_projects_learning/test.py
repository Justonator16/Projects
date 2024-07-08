test = [0,3,7,2,5,8,4,6,0,1]

for i in range(len(test)):
  if i+1 < len(test):
    if test[i+1] > test[i]:
      test[i] , test[i+1] = test[i+1] , test[i]

def sort_number_asc(number_list):
  for i in range(len(number_list)):
    if i+1 < len(number_list):
      if number_list[i+1] > number_list[i]:
        number_list[i] , number_list[i+1] = number_list[i+1] , number_list[i]
  
  number_list_sorted_asc = []  
  for i in range(1,len(number_list)):
      number_list_sorted_asc.append(number_list[-i])
  number_list_sorted_asc.append(number_list[0])
  
  return number_list_sorted_asc
  
print(sort_number_asc(test))

asc_sorted_list = sort_number_asc(test)
pattern_checker = 0
patterns = []
for i in range(len(asc_sorted_list)):
  if i+1 < len(asc_sorted_list) :
    difference = (asc_sorted_list[i+1]) - (asc_sorted_list[i])
    if (asc_sorted_list[i] + difference) == asc_sorted_list[i+1]:
      pattern_checker += 1
      print(pattern_checker)
  else:
      patterns.append(pattern_checker)
      pattern_checker = 0

print(patterns)


  