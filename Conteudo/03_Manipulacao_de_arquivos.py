
file = 'arquivo.txt'

## Abertura de arquivo

# abertura para escrita
arquivo_escrita = open(file, "w")   #write
arquivo_escrita.write("Texto a ser escrito")
arquivo_escrita.close()

# abertura somente para leitura
arquivo_leitura = open(file, "r")   #read
leitura = arquivo_leitura.read()
print(leitura)
arquivo_leitura.close()




