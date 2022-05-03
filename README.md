# Web Crawler
El progrma desarrollado nos permite indexar paginas web, buscando la interrelacion entre cada una de estas para su posterior uso en un buscador ademas de calificarlas seguun su importancia usando ciertos parametros establecidos.

Desarrollado por:
- Alexis Espinoza Villanueva
- Renato Oscar Corrales Peña

El programa se desarrolló a partir del siguiente diccionario:

    https://drive.google.com/file/d/1hHQu9N7hyl9FI-LlcI1-vtDTKB0Cs3xI/view?usp=sharing
    
En el cual las claves son urls de páginas web y los valores representan el contenido de cada url o página.

# Instrucciones de ejecución
1.El usuario deberá tener python e ingresar

    >>> python3 perm1c_grupo_9.py
    
   2. Al iniciar el programa se le mostrará la página web, los links entrantes, los links salientes y el valor de importancia de la página(como un valor numérico).
    
    página: https://ucsp.edu.pe/cs111/index.html
    
    e   = 0
    s   = 5
    rank = 0.0
    
   3. El valor de e siendo los links entrantes.
   
     e   = 0
    
   4. El valor de siendo los links salientes.
  
     s  = 5
        
   5. El valor rank siendo la importancia de la página en un valor numérico calculado de la siguiente manera: rank = e/(s+1) 
   
     rank = 0.0
       
