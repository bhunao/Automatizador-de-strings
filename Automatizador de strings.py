#Automation of Strings
#Split the String

print("Este código foi criado para automatizar e facilitar a colocação de um conjunto de strings entre aspas e separar as strings por virgula.")
start = input("Dejesa algo escrito antes de cada linha ? : ")
divisor = input("""Deseja colocar as Strings dentro de "" ou '' """)
divisor = divisor[0]
print("Digite 'FIM' quando quiser parar.")


end = []


while True:
  data = input("Digite: ")
  if data.lower() == 'fim':
    break
  data_split = data.split()
  data = start + " ("
  for string in range(len(data_split)):
    if string == len(data_split)-1:
      data += f"{divisor}{data_split[string]}{divisor})"
    else:
      data += f"{divisor}{data_split[string]}{divisor}, "
  end.append(data)
  
for line in end:
  print(line)