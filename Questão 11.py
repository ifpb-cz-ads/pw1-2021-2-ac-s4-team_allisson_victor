preco = int(input("Digite o preco do produto: "))
desconto = int(input("Digite o valor de desconto: "))

descontado = preco*(desconto/100)
total = preco - descontado

print("O valor com o desconto é %d " %total)
print("O valor do desconto é %d porcento, foi descontado %d reais" %(desconto,descontado))