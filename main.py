a = eval(input("Ievadit skaitļus: "))

def countNumbers(teksts):
  summa = 0
  for simbols in teksts:
    summa = summa + int(simbols)
  return summa
print(countNumbers(a))