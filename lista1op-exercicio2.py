inputSeg = int(input('Por favor, entre com o número de segundos que deseja converter: '))
if inputSeg >= 86400 :
    dias = inputSeg//86400
    segResto = inputSeg % 86400
    horas = segResto // 3600
    segResto = segResto % 3600
    minutos = segResto // 60
    segResto = segResto % 60
elif inputSeg < 86400 :
    dias = 0
    horas = inputSeg // 3600
    segResto = inputSeg % 3600
    minutos = segResto // 60
    segResto = segResto % 60
elif inputSeg < 3600:
    dias = 0
    horas = 0
    minutos = inputSeg // 60
    segResto = minutos % 60
else:
    dias = 0
    horas = 0
    minutos = 0
    inputSeg

print( dias, "dias,", horas, "horas,", minutos, "minutos e", segResto, "segundos." )