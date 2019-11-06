##Banco de dados
bd = int(input("Quantidade de BD: "))
arquivo = []
total = 0
for i in range(0,bd):
    arquivo.append(int(input("Quantidade de linhas: ")))
    total = total + arquivo[i]
##Entrada
dadosref = 0
dadosref1 = 0
dadosref2 = 0
for i in range(0,bd):
    if arquivo[i] <= 4:
        dadosref = dadosref + 1
    if arquivo[i] >= 5 and arquivo[i] <= 15:
        dadosref1 = dadosref1 + 1
    if arquivo[i] >= 16:
        dadosref2 = dadosref2 + 1
entsimples = []
entmedio = []
entcomplexo = []
if dadosref <= 1:
    entsimples.append(dadosref)
elif dadosref == 2:
    entsimples.append(dadosref)
elif dadosref >= 3:
    entmedio.append(dadosref)
if dadosref1 <= 1:
    entsimples.append(dadosref1)
elif dadosref1 == 2:
    entmedio.append(dadosref1)
elif dadosref1 >= 3:
    entcomplexo.append(dadosref1)
if dadosref2 <= 1:
    entmedio.append(dadosref2)
elif dadosref2 == 2:
    entcomplexo.append(dadosref2)
elif dadosref2 >= 3:
    entcomplexo.append(dadosref2)
somasimples = 0
somamedio = 0
somacomplexo = 0
for i in range(0,len(entsimples)):
    somasimples = entsimples[i] * 3 + somasimples
for i in range(0,len(entmedio)):
    somamedio = entmedio[i] * 4 + somamedio
for i in range(0,len(entcomplexo)):
    somacomplexo = entcomplexo[i] * 6 + somacomplexo
##print("Entrada simples:", somasimples)
##print("Entrada médio:", somamedio)
##print("Entrada complexo:", somacomplexo)
##Saída
saidadadosref = 0
saidadadosref1 = 0
saidadadosref2 = 0
for i in range(0,bd):
    if arquivo[i] <= 5:
        saidadadosref = saidadadosref + 1
    if arquivo[i] >= 6 and arquivo[i] <= 19:
        saidadadosref1 = saidadadosref1 + 1
    if arquivo[i] >= 20:
        saidadadosref2 = saidadadosref2 + 1
if total <=5:
    saidadadosref = saidadadosref +1
if total >= 6 and total <= 19:
    saidadadosref1 = saidadadosref1 +1
if total >= 20:
    saidadadosref2 = saidadadosref2 +1
saidasimples = []
saidamedio = []
saidacomplexo = []
if saidadadosref <= 1:
    saidasimples.append(saidadadosref)
elif saidadadosref >= 2 and saidadadosref <= 3:
    saidasimples.append(saidadadosref)
elif saidadadosref >= 4:
    saidamedio.append(saidadadosref)
if saidadadosref1 <= 1:
    saidasimples.append(saidadadosref1)
elif saidadadosref1 >= 2 and saidadadosref1 <= 3:
    saidamedio.append(saidadadosref1)
elif saidadadosref1 >= 4:
    saidacomplexo.append(saidadadosref1)
if saidadadosref2 <= 1:
    saidamedio.append(saidadadosref2)
elif saidadadosref2 >= 2 and saidadadosref2 <= 3:
    saidacomplexo.append(saidadadosref2)
elif saidadadosref2 >= 4:
    saidacomplexo.append(saidadadosref2)
sdsimples = 0
sdmedio = 0
sdcomplexo = 0
for i in range(0,len(saidasimples)):
    sdsimples = saidasimples[i] * 4 + sdsimples
for i in range(0,len(saidamedio)):
    sdmedio = saidamedio[i] * 5 + sdmedio
for i in range(0,len(saidacomplexo)):
    sdcomplexo = saidacomplexo[i] * 7 + sdcomplexo
##print("Saida simples:", sdsimples)
##print("Saida médio:", sdmedio)
##print("Saida complexo:", sdcomplexo)
##Consulta
consultadadosref = 0
consultadadosref1 = 0
consultadadosref2 = 0
for i in range(0,bd):
    if arquivo[i] <= 4:
        consultadadosref = consultadadosref + 1
    if arquivo[i] >= 5 and arquivo[i] <= 15:
        consultadadosref1 = consultadadosref1 + 1
    if arquivo[i] >= 16:
        consultadadosref2 = consultadadosref2 + 1
if total <=4:
    consultadadosref = consultadadosref +1
if total >= 5 and total <= 15:
    consultadadosref1 = consultadadosref1 +1
if total >= 16:
    consultadadosref2 = consultadadosref2 +1
consultasimples = []
consultamedio = []
consultacomplexo = []
if consultadadosref <= 1:
    consultasimples.append(consultadadosref)
elif consultadadosref == 2:
    consultasimples.append(consultadadosref)
elif consultadadosref >= 3:
    consultamedio.append(consultadadosref)
if consultadadosref1 <= 1:
    consultasimples.append(consultadadosref1)
elif consultadadosref1 == 2:
    consultamedio.append(consultadadosref1)
elif consultadadosref1 >= 3:
    consultacomplexo.append(consultadadosref1)
if consultadadosref2 <= 1:
    consultamedio.append(consultadadosref2)
elif consultadadosref2 == 2:
    consultacomplexo.append(consultadadosref2)
elif consultadadosref2 >= 3:
    consultacomplexo.append(consultadadosref2)
consimples = 0
conmedio = 0
concomplexo = 0
for i in range(0,len(consultasimples)):
    consimples = consultasimples[i] * 3 + consimples
for i in range(0,len(consultamedio)):
    conmedio = consultamedio[i] * 4 + conmedio
for i in range(0,len(consultacomplexo)):
    concomplexo = consultacomplexo[i] * 6 + concomplexo
##print("Consulta simples:", consimples)
##print("Consulta médio:", conmedio)
##print("Consulta complexo:", concomplexo)
##Arquivos
arqdadosref = 0
arqdadosref1 = 0
arqdadosref2 = 0
for i in range(0,bd):
    if arquivo[i] <= 19:
        arqdadosref = arqdadosref + 1
    if arquivo[i] >= 20 and arquivo[i] <= 50:
        arqdadosref1 = arqdadosref1 + 1
    if arquivo[i] >= 51:
        arqdadosref2 = arqdadosref2 + 1
arqsimples = []
arqmedio = []
arqcomplexo = []
if arqdadosref <= 1:
    arqsimples.append(arqdadosref)
elif arqdadosref >= 2 and arqdadosref <= 5:
    arqsimples.append(arqdadosref)
elif arqdadosref >= 6:
    arqmedio.append(arqdadosref)
if arqdadosref1 <= 1:
    arqsimples.append(arqdadosref1)
elif arqdadosref1 >= 2 and arqdadosref1 <= 5:
    arqmedio.append(arqdadosref1)
elif arqdadosref1 >= 6:
    arqcomplexo.append(arqdadosref1)
if arqdadosref2 <= 1:
    arqmedio.append(arqdadosref2)
elif arqdadosref2 >= 2 and arqdadosref2 <= 5:
    arqcomplexo.append(arqdadosref2)
elif arqdadosref2 >= 6:
    arqcomplexo.append(arqdadosref2)
arqsomasimples = 0
arqsomamedio = 0
arqsomacomplexo = 0
for i in range(0,len(arqsimples)):
    arqsomasimples = arqsimples[i] * 7 + arqsomasimples
for i in range(0,len(arqmedio)):
    arqsomamedio = arqmedio[i] * 10 + arqsomamedio
for i in range(0,len(arqcomplexo)):
    arqsomacomplexo = arqcomplexo[i] * 15 + arqsomacomplexo
##print("Arquivo simples:", arqsomasimples)
##print("Arquivo médio:", arqsomamedio)
##print("Arquivo complexo:", arqsomacomplexo)
##Interfaces
intdadosref = 0
intdadosref1 = 0
intdadosref2 = 0
for i in range(0,bd):
    if arquivo[i] <= 19:
        intdadosref = intdadosref + 1
    if arquivo[i] >= 20 and arquivo[i] <= 50:
        intdadosref1 = intdadosref1 + 1
    if arquivo[i] >= 51:
        intdadosref2 = intdadosref2 + 1
if total <= 19:
    intdadosref = intdadosref +1
if total >= 20 and total <= 50:
    intdadosref1 = intdadosref1 +1
if total >= 51:
    intdadosref2 = intdadosref2 +1
intsimples = []
intmedio = []
intcomplexo = []
if intdadosref <= 1:
    intsimples.append(intdadosref)
elif intdadosref >= 2 and intdadosref <= 5:
    intsimples.append(intdadosref)
elif intdadosref >= 6:
    intmedio.append(intdadosref)
if intdadosref1 <= 1:
    intsimples.append(intdadosref1)
elif intdadosref1 >= 2 and intdadosref1 <= 5:
    intmedio.append(intdadosref1)
elif intdadosref1 >= 6:
    intcomplexo.append(intdadosref1)
if intdadosref2 <= 1:
    intmedio.append(intdadosref2)
elif intdadosref2 >= 2 and intdadosref2 <= 5:
    intcomplexo.append(intdadosref2)
elif intdadosref2 >= 6:
    intcomplexo.append(intdadosref2)
intsomasimples = 0
intsomamedio = 0
intsomacomplexo = 0
for i in range(0,len(intsimples)):
    intsomasimples = intsimples[i] * 5 + intsomasimples
for i in range(0,len(intmedio)):
    intsomamedio = intmedio[i] * 7 + intsomamedio
for i in range(0,len(intcomplexo)):
    intsomacomplexo = intcomplexo[i] * 10 + intsomacomplexo
##print("Saida simples:", intsomasimples)
##print("Saida médio:", intsomamedio)
##print("Saida complexo:", intsomacomplexo)
##Calculos finais
fpb = somasimples + somamedio + somacomplexo + sdsimples + sdmedio + sdcomplexo + intsomasimples + intsomamedio + intsomacomplexo + arqsomasimples + arqsomamedio + arqsomacomplexo + consimples + conmedio + concomplexo
ni = 1.35
fpr = round(fpb * ni)
print(fpr)
print('''[1] - Cobol
[2] - Pascal
[3] - C++
[4] - Java, Delph, Visual Basic
[5] - SQL, HTML''')
locfp = int(input("Escolha uma opção: "))
prod = 0
if locfp == 1:
    prod = fpr * 100
if locfp == 2:
    prod = fpr * 90
if locfp == 3:
    prod = fpr * 30
if locfp == 4:
    prod = fpr * 20
if locfp == 5:
    prod = fpr * 15
print('''[1] - Sistema Comercial
[2] - Sistema Eletrônico
[3] - Sistema Web''')
sistema = int(input("Qual tipo de sistema: "))
if sistema == 1:
    prodmes = prod / 2500
if sistema == 2:
    prodmes = prod / 3600
if sistema == 3:
    prodmes = prod / 3300
vh = int(input("Qual o valor da hora: "))
custo = prodmes * 132 * vh
print('R${:.2f}'.format(custo))