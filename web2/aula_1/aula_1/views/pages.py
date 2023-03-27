from django.shortcuts import render
import math

def pag(request):
    lista = ""
    lista2 = ""
    tudo = ''
    oi = ''
    if request.method == "POST":
        sqnc = request.POST['dna'].upper()
        count_a = sqnc.count('A')
        count_g = sqnc.count('G')
        count_c = sqnc.count('C') 
        count_t = sqnc.count('T')

        for i in sqnc:
            if i == "A":
                lista+="T"
            elif i == "T":
                lista+="A"
            elif i == "C":
                lista+="G"
            elif i == "G":
                lista+="C"
            else:
                lista2 = "Erro"   
        

        if lista2 == "":
            tudo = f"A quantidade de Adenina é {count_a}, Guanina é {count_g}, Citosina é {count_c}, Timina é {count_t}"
            oi = f"Nucleotídeos da sequência que se liga com ela são: {lista}"

        if sqnc == "":
            oi = ''
            tudo = ''
            lista2 = "Você digitou vazio, digite uma sequencia válida!"

    return render(request, "index.html",{"dna":tudo, "lista": oi, "erro": lista2} )

def pag2(request):
    volume = ""
    if request.method == "POST":
        raio = request.POST['r'] 
        altura = request.POST['h'] 

        r = float(raio) * 1000
        h = float(altura) * 1000

        v = ((math.pi * r ** 2 * h) / 3)
        volume = f"O Volume da Terra plana é {v} Km3"

    return render(request, "index2.html",{"volume" :volume} )

def pag3(request):
    total = {}
    erro = ""
    resultado = ""
    if request.method == "POST":
        vogais = request.POST['vogais']
        v = vogais.lower()
        vogal = 'aeiou'
        for letra in vogal:
            total[letra] = v.count(letra)
        
        if vogais == "":
            total = ""
            erro = "Você digitou vazio"
        else:
            resultado =  f"Total de vogais é {total}"


    return render(request, "index3.html", {"vogais" : resultado, "erro" : erro})
    

def pag4(request):
    matriz = ''
    saida = ""
    if request.method == "POST":
        ordem = request.POST['entrada']
        m = int(ordem)
        matriz = [[0 for x in range(m) ] for y in range(m)]
        for i in range(m):
            matriz[i][i] = 1

        saida = f"A saida da matriz é {matriz}"
        

    return render(request, "index4.html", {"saida" : saida})

def pag5(request):
    saida = ""
    valor = ""
    if request.method == "POST":
        indice = request.POST['entrada']
        ind = int(indice)
        if ind == 0:
            valor = 0
        elif ind == 1 or ind == 2:
            valor = 1
        else:
            a, b = 1, 1
            for i in range(3, ind + 1):
                valor = a + b
                a, b = b, valor
                saida = f"Esse indice represeta {valor} na sequencia de  fibonacci "

    return render(request, "index5.html", {'saida': saida})


