def sort(arr):
  #Caso base: la lista tenga uno o menos caracteres
  if len(arr)<=1:
    return arr
  else:
    #Se inicia analizando el primer caracter de la lista
    pivot= arr[0]
    left= []
    right= []
    middle= []
    #Almacena los caracteres en listas segun el orden en comparacion con pivot
    for element in arr:
      if element<pivot:
        left.append(element)
      elif element>pivot:
        right.append(element)
      else:
        middle.append(element)
    #Hace llamado recursivo para ordenar sublistas y retorna la lista final ordenada
    return sort(left) + middle +sort(right)

def classification(s):
  lowerC= []
  odd= []
  even= []
  upperC= []

  #Se realiza una clasificacion de los caracteres almacenandolos en las diferentes variables creadas 
  #segun su caracteristica
  for element in s:
    if element.islower():
      lowerC.append(element)
    elif element.isupper():
      upperC.append(element)
    elif element.isdigit():
      if int(element) % 2== 1:
        odd.append(element)
      else:
        even.append(element)

  #Se llama a la funcion quicksort para ordenarlos dentro de su clasificacion
  lowerC= sort(lowerC)
  upperC= sort(upperC)
  odd= sort(odd)
  even= sort(even)
  #Se retorna la lista final ordenada 
  return ''.join(lowerC + upperC + odd + even)

#Pide y manda lista
while True:
    s=input("Ingresa una cadena de caracteres alfanumericos: ")
    if len(s) >0 and len(s)<1000:
        print(classification(s))
    else:
        print("La cadena debe tener mas de 0 caracteres y menos de 1000 caracteres")
    keep = input("Desea agregar otra cadena? S/N: ")
    if keep == 'N':
      break;