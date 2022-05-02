web = {'https://ucsp.edu.pe/cs111/index.html': """<html>
<body>
<h1>Algoritmo CS111</h1>
<p>
Aqui encontraremos más información al respecto:
<ul>
<li> <a href="https://ucsp.edu.pe/cs111/pseudocodigo.html">Pseudocódigo</a>
<li> <a href="https://ucsp.edu.pe/cs111/implementacion.html">Implementación del algoritmo</a>
<li> <a href="https://ucsp.edu.pe/cs111/python.html">Documentación de Python</a>
</ul>

Podemos revisar comentarios adicional al respecto: 
<a href="https://ucsp.edu.pe/cs111/guido.html">Guido van Rossum</a> 
y <a href="https://ucsp.edu.pe/cs111/peter.html">Peter Norvig</a>.
</body>
</html>
""",
   'https://ucsp.edu.pe/cs111/peter.html': """<html>
<body>
<h1>Peter Norvig</h1>
<p>
Peter Norvig es un científico estadounidense, investigador en ciencias de la computación. Actualmente 
es director de investigación de la empresa Google. Ha publicado unos cincuenta artículos científicos 
sobre informática, en particular en el campo de la inteligencia artificial, el procesamiento automático 
del lenguaje natural , la recuperación de información y el diseño de software.

Con muchos años de expiencia en el lenguaje <a href="https://ucsp.edu.pe/cs111/python.html">Python</a>, 
creado por <a href="https://ucsp.edu.pe/cs111/guido.html">Guido van Rossum</a>.

</body>
</html>






""",
   'https://ucsp.edu.pe/cs111/guido.html': """<html>
<body>
<h1>Guido van Rossum</h1>
<p>
El es el creador de 
<a href="https://ucsp.edu.pe/cs111/python.html">Python</a>

</body>
</html>


""",
   'https://ucsp.edu.pe/cs111/python.html': """<html>
<body>
<h1>
Lenguaje de Programación Python
</h1>
<p>

<ol>
<li> Python 2.
<li> Python 3.
</ol>

</body>
</html>

""",
   'https://ucsp.edu.pe/cs111/implementacion.html': """<html>
<body>
<h1>
La Implementación del algoritmo
</h1>
<p>

<ol>
<li> En el siguiente link <a href="https://ucsp.edu.pe/cs111/guido.html">Guido van Rossum</a>.
<li> Cree las variables de manera correcta, siguiendo los estandares.
</ol>

</body>
</html>

""",
   'https://ucsp.edu.pe/cs111/pseudocodigo.html': """<html>
<body>
<h1>
Pseudocódigo
</h1>
<p>

<ol>
<li> 'https://ucsp.edu.pe/cs111/implementacion.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
</ol>

</body>
</html>

"""}

#
# Ingrese su código debajo de esta linea
# ############################################################

#Asignación

salientes = {}                      #Diccionario de links salientes
entrantes = {}                      #Diccionario de links entrantes
links_unicos = tuple(web.keys())    #Tupla con todos los links únicos

#Strings que se usaran para buscar en el texto los links

inicio = 'https:'                   
final = '.html'                     

#Armando el diccionario de links salientes

for pagina, texto in web.items():

   conjunto_url = set() #Conjunto en el que se guardaran todos los links salientes de la página
   
   #Bucle que se ejecutará hasta encontrar todos los links salientes de la página
   
   while True:

      #Se encuentra la posición inicial y final del link

      pos = texto.find(inicio)            
      pos2 = texto[pos:].find(final) + len(final) + pos     

      if texto.find(inicio) == -1:
         break

      conjunto_url.add(texto[pos:pos2])     #Se guarda el link en la lista
      texto = texto[pos2+1:]                #El nuevo texto empezará desde la posicion final de donde se extrajo el link
   
   salientes[pagina] = conjunto_url

#Armando el diccionario de links entrantes

for link in links_unicos:

    lista_entrantes = []    #Lista en la que se guardaran todos las páginas que son entrantes del link

    for pagina, lista_salientes in salientes.items():

        #Si el link esta en la lista de salientes de una página, significa que esa página es un entrante del link

        if link in lista_salientes:                  
            lista_entrantes.append(pagina) #Se guarda la página en la lista de entrantes

    entrantes[link] = lista_entrantes

print(f"\nLinks salientes: {salientes}\n")
print(f"Links entrantes: {entrantes}")

#Print de los rankings

for link in links_unicos:

   try:
      rank = len(entrantes[link])/len(salientes[link])  
   except ZeroDivisionError:
      rank = 0

   print(f"""página: {link}

e   = {len(entrantes[link])}
s   = {len(salientes[link])}
rank = {rank}\n""")




