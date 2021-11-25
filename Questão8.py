salário = int(input("Informe o Valor do Salario:"))
aumento = int(input("Informe a % do aumento no Salário:"))
Vaumento = salário*(aumento/100)
Vsalario = salário+Vaumento
Taumento = Vsalario - salário;
print("Seu salário de",salário,"vai para",Vsalario,"com aumento de",Taumento)
