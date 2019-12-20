print ("quanto voce ganha por hora?")
ganho = 100
print (ganho)
print ("quantas horas trabalhadas ao mes?")
horas = 200
print (horas)
print ("qual e o salario bruto?")
salario = ganho*horas
print (salario)
print ("quanto voce paga de INSS?")
INSS = 8/100*salario
print (INSS)
print ("quanto voce paga ao sindicato?")
sindicato = 5/100*salario
print (sindicato)
print ("quanto voce paga ao imposto de renda?")
imposto = 11/100*salario
print (imposto)
print ("qual e o salario liquido?")
liquido = salario - INSS - sindicato - imposto
print (liquido)