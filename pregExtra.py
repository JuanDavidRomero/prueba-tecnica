urlList = []
def findURL(checkL):
    subDomains = ["www", "ww2.", "ftp", "mail"]
    start = 0
    while True:
        #Se realiza la separacion de las url en el texto
        position = checkL.find("http://", start)
        if position == -1:
            position = checkL.find("https://", start)
            if position == -1:
                break
        end = checkL.find(")", position)
        if end == -1:
            end = len(checkL)
        url = checkL[position:end]

        #Se detecta el dominio
        startDomain = 0
        for i, domains in enumerate(subDomains):
            startDomain = url.find(domains, 0) + len(domains) + 1
            if startDomain -len(domains) - 1 != -1 and startDomain < 15:
                break 
            elif startDomain -len(domains) - 1 == -1 or i == len(subDomains) - 1 or startDomain > 15:
                startDomain = url.find("//", 0) + 2
                #print(startDomain)
                if i == len(subDomains) - 1 or startDomain > 15:
                    break

        endDomain = url.find('"', startDomain)
        if endDomain == -1:
            endDomain = url.find("/", startDomain)
        urlDomain = url[startDomain:endDomain]
        #Se agrega dominio a una lista
        urlList.append(urlDomain)
        start = end

#Se inicia leyendo el fragmento de marcado de HTML 
with open('fragmento.txt', 'r') as file:
    position = 0

    nLines = int(file.readline().strip())
    for i in range(nLines):
        findURL (file.readline())
#Se ordena y se imprime lista de dominios
finalList = ';'.join(sorted(urlList))
print (finalList)