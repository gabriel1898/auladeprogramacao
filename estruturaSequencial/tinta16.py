def custo():
  area = input ("valor area")
  litros = float(area)/3
  print (litros)
  latasFloat = float(litros)/18
  latasInt = int(latasFloat)
  if (latasFloat > latasInt): 
    latasInt = latasInt + 1
  print (latasFloat)
  print (latasInt)
  custo = latasInt*80
  print (custo)

