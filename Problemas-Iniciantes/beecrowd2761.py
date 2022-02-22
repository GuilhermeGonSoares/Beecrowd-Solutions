entrada = input().split()

n1 = int(entrada[0])
n2 = float(entrada[1])
caractere = str(entrada[2])
frase = ""
if len(entrada) > 4:
    for i in range(3, len(entrada)-1):
        frase += entrada[i] + " "
    frase += entrada[i+1]
else:
    frase = entrada[3]
frase = frase.strip()

print("%d%.6f%c%s" %(n1,n2,caractere,frase))
print("%d\t%.6f\t%c\t%s" %(n1,n2,caractere,frase))
print("%10d%10.6f%10c%10s" %(n1,n2,caractere,frase))
