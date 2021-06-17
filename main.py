import os
import pathlib
import sys


from os import listdir
from os.path import isfile, join

def display_annotations(path):
  with open(path,'r') as f:
    for line in f:
      if 'x:Class=' in line:
        stringa=line.split('"')
        print("The workflow type is {}.xaml\n".format(stringa[3]))
      if 'Annotation.AnnotationText' in line:
        stringa=line.split('"')
        #print(stringa)
        print("Annotation: {}".format(stringa[1]))
        l=len(stringa)
        if 'DisplayName' in line:
          stringa=line.split('"')
          print('Display Name: {}'.format(stringa[3]))
        print("Type {}\n".format(stringa[l-2]))
  return None



def getListOfFiles(dirName):
    # cria uma lista de arquivos e subdiretórios 
    # nomes no diretório dado 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Itera sobre todas as entradas
    for entry in listOfFile:
        # Cria um caminho completo
        fullPath = os.path.join(dirName, entry)
        # Se a entrada for um diretório, obtenha a lista de arquivos neste diretório 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles  
# Dá o diretório atual
basepath=os.getcwd()
print("Path: "+basepath)


dirName =basepath
# Obtem a lista de todos os arquivos na árvore de diretórios em determinado caminho
listOfFiles = getListOfFiles(dirName)

# Obtem a lista de todos os arquivos na árvore de diretórios em determinado caminho
listOfFiles = list()
for (dirpath, dirnames, filenames) in os.walk(dirName):
    listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    


# Print os arquivos 
for elem in listOfFiles:
  print(elem)  
  print("")
  if elem.endswith(".txt") or elem.endswith(".xaml"):
    display_annotations(elem)
  print ("****************") 

# Salva uma referência à saída padrão original  
original_stdout = sys.stdout 

# Escreve o resultado em document.txt
with open('document.txt', 'w') as f:
  sys.stdout = f # Altera a saída padrão para o arquivo que criamos.
  #print ('Esta mensagem será gravada em um arquivo.')
  for elem in listOfFiles:
    print(elem)  
    print("")
    if elem.endswith(".txt") or elem.endswith(".xaml"):
      display_annotations(elem)
    print ("****************")
  sys.stdout = original_stdout # Redefine a saída padrão para seu valor original



    
    

  
  






     
  


     
      


