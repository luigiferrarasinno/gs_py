valores_solo=[]
valores_solo2=[]
valores_solo3=[]

def menu_zona1():
 valores_solo.insert(0, int(input("Digite o valor do ph: ")))
 valores_solo.insert(1, int(input("Digite a quantidade de adubação em kg/h com todos os tipos: ")))
 valores_solo.insert(2, int(input("Digite a quantidade de plantas daninhas: ")))
 valores_solo.insert(3, int(input("Digite a quantidade de pragas: ")))
 valores_solo.insert(4, int(input("Digite o valor de drenagem: ")))
 
 if 6 < valores_solo[0] < 8:
    print("O pH está ideal.")
 elif valores_solo[0] > 6:
    print("O pH está abaixo do ideal.")
 else:
    print("o ph esta acima do ideal")
        
 if 160 < valores_solo[1] < 200:
    print("a quantidade de adubação está ideal.")
 elif valores_solo[1] > 160:
     print("a quantidade de adubação está abaixo.")
 else:
     print("a quantidade de adubação esta acima do ideal")
        
 if 0< valores_solo[2] < 2:
     print("a quantidade de plantas daninhas esta ideial")
 else :
    print("a quantidade de plantas daninhas esta acima do ideal")

 if 0< valores_solo[3] < 2:
     print("a quantidade de pragas esta ideal")
 else:
     print("a quantidade de pragas esta acima do ideal")
        
 if 5 < valores_solo[4] < 15:
     print("a drenagem está ideal.")
 elif valores_solo[4] > 5:
     print("a drenagem está abaixo.")
 else:
     print("a drenagem acima do ideal")
     
def menu_zona2():
 valores_solo2.insert(0, int(input("Digite o valor do ph: ")))
 valores_solo2.insert(1, int(input("Digite a quantidade de adubação em kg/h com todos os tipos: ")))
 valores_solo2.insert(2, int(input("Digite a quantidade de plantas daninhas: ")))
 valores_solo2.insert(3, int(input("Digite a quantidade de pragas: ")))
 valores_solo2.insert(4, int(input("Digite o valor de drenagem: ")))
 
 if 6 < valores_solo2[0] < 8:
    print("O pH está ideal.")
 elif valores_solo2[0] > 6:
    print("O pH está abaixo do ideal.")
 else:
    print("o ph esta acima do ideal")
        
 if 6 < valores_solo2[1] < 8:
    print("a quantidade de adubação está ideal.")
 elif valores_solo2[1] > 6:
     print("a quantidade de adubação está abaixo.")
 else:
     print("a quantidade de adubação esta acima do ideal")
        
 if 0< valores_solo2[2] < 2:
     print("a quantidade de plantas daninhas esta ideial")
 else:
    print("a quantidade de plantas daninhas esta acima do ideal")

 if 0< valores_solo2[3] < 2:
     print("a quantidade de pragas esta ideal")
 else:
     print("a quantidade de pragas esta acima do ideal")
        
 if 5 < valores_solo2[4] < 15:
     print("a drenagem está ideal.")
 elif valores_solo2[4] > 5:
     print("a drenagem está abaixo.")
 else:
     print("a drenagem esta acima do ideal")
     
def menu_zona3():
 valores_solo3.insert(0, int(input("Digite o valor do ph: ")))
 valores_solo3.insert(1, int(input("Digite a quantidade de adubação em kg/h com todos os tipos: ")))
 valores_solo3.insert(2, int(input("Digite a quantidade de plantas daninhas: ")))
 valores_solo3.insert(3, int(input("Digite a quantidade de pragas: ")))
 valores_solo3.insert(4, int(input("Digite o valor de drenagem: ")))
 
 if 6 < valores_solo3[0] < 8:
    print("O pH está ideal.")
 elif valores_solo3[0] > 6:
    print("O pH está abaixo do ideal.")
 else:
    print("o ph esta acima do ideal")
        
 if 6 < valores_solo3[1] < 8:
    print("a quantidade de adubação está ideal.")
 elif valores_solo3[1] > 6:
     print("a quantidade de adubação está abaixo.")
 else:
     print("a quantidade de adubação esta acima do ideal")
        
 if 0< valores_solo3[2] < 2:
     print("a quantidade de plantas daninhas esta ideial")
 else:
    print("a quantidade de plantas daninhas esta acima do ideal")


 if 0< valores_solo3[3] < 2:
     print("a quantidade de pragas esta ideal")
 else:
     print("a quantidade de pragas esta acima do ideal")
        
 if 5< valores_solo3[4] < 15:
     print("a drenagem está ideal.")
 elif valores_solo3[4] > 5:
     print("a drenagemestá abaixo.")
 else:
     print("a drenagem esta acima do ideal")
     
temperatura = int(input("Digite a temperatura do ambiente: "))
if 20 <= temperatura <= 35:
    print("A temperatura está ideal")
elif temperatura < 20:
    print("Temperatura muito baixa")
else:
    print("Temperatura acima do ideal")


precipitação = int(input("Digite a precipitação do ambiente: "))
if 1000 <= precipitação <= 2500:
    print("A precipitação está ideal")
elif precipitação < 1000:
    print("precipitação muito baixa")
else:
    print("precipitação acima do ideal")

umidade = int(input("Digite a umidade do ambiente em %: "))
if 60 <= umidade <= 80:
    print("A umidade está ideal")
elif umidade < 60:
    print("umidade muito baixa")
else:
    print("umidade acima do ideal")


while True:
 opção=int(input("digite:\n1 para informações sobre zona 1\n2 para informações sobre zona 2\n3 para informações sobre zona 3\n "))
 match opção:
     case 1:
         menu_zona1()
     case 2:
         menu_zona2()
     case 3:
         menu_zona3()
     case _:
         print("opção invalida")
    


        