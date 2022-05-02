# Web Crawler
El progrma fue desarrollado programa nos permite indexar paginas web, buscando la interrelacion entre cada una de estas para su posterior uso en un buscador ademas de calificarlas seguun su importancia usando ciertos parametros establecidos

Desarrollado por:
- Alexis Espinoza Villanueva
- RenatoOscar Corrales Peña

##Intrucciones de ejecucion
1.El usuario debera tener python e ingresar

    ```
    >>> perm1cgrupo9.py
    ```
    
   2.Al iniciar el programa se le mostrara la pagina web, los links entrantes, los links salientes y el valor de importancia de la pagina(como un valor numerico).
    
    página: https://ucsp.edu.pe/cs111/index.html
    
    e   = 0
    s   = 5
    rank = 0.0
    
   3.El valor de e siennndo los links entrantes.
   
        e   = 0
    
   4. El valor de ssiendo los links salientes.
    
    s  = 5
        
   5.El valor rank siendo la importancia de la pagina en un valor numerico calculado de la siguiente manera: rank = e/s 
   
        rank = 0.0
        
 #Posible situacion
 En casso de que el valor de los links salientes sea 0 se aplicara la siguiente formula para hallar la importancia(rank): e/s+1
