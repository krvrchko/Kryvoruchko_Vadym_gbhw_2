def get_sign(x):
  if x[0] in '+-':
    return x[0]

source_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len(source_list):
  sign = get_sign(source_list[i])
  if source_list[i].isdigit() or (sign and source_list[i][1:].isdigit()):
    if sign:
      source_list[i] = sign + source_list[i][1:].zfill(2)
    else: 
      source_list[i] = source_list[i].zfill(2)
  
  i += 1  

i = 0
while i < len(source_list):
  source_list.insert(i, '"')
  i += 2

del source_list[0]
del source_list[9]
del source_list[10]
del source_list[11]
  
for i in source_list:
 print(i, end=' ')
  

