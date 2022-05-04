# Web Crawler
El programa desarrollado nos permite indexar paginas web, buscando la interrelación entre cada una de estas para su posterior uso en un buscador además de calificarlas segun su importancia usando ciertos parametros establecidos.

Desarrollado por:
- Alexis Espinoza Villanueva
- Renato Oscar Corrales Peña

El programa se desarrolló a partir del siguiente diccionario:

    https://drive.google.com/file/d/1hHQu9N7hyl9FI-LlcI1-vtDTKB0Cs3xI/view?usp=sharing
    
En el cual las claves son urls de páginas web y los valores representan el contenido de cada url o página.

# Instrucciones de ejecución
1.El usuario deberá tener python e ingresar

    >>> python3 perm1c_grupo_9.py
    
2.Al iniciar el programa se le mostrará un ranking de páginas web, según la cantidad de los links salientes.
  
    1. https://ucsp.edu.pe/cs111/index.html con un valor de 5
    ...

3.Seguido a este, se muestra ranking según la cantidad de links entrantes.

    1. https://ucsp.edu.pe/cs111/python.html con un valor de 3
    ...
    
4.Finalmente, el programa nos muestra un ranking según la importancia de las páginas web.
 
    1. https://ucsp.edu.pe/cs111/python.html con un valor de 3.0
    ...
    
La importancia del link se calcula de la siguiente manera e/(s+1) siendo:
+ e: Cantidad de los links entrantes
+ s: Cantidad de los links salientes
