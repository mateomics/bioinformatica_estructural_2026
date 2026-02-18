## Algoritmos en bioinformática estructural   
Las biomoléculas como los ácidos nucleicos son los principales canales del flujo de la información genómica. 


## Intro 
Enlaces peptidicos entre los aminoacidos (20 canonicos) son la materia prima para formar las proteinas, esta union covalente entre el amino terminal y el carboxilo hacen que los grados de libertad de las proteinas, al ser un enlace muy rigido, sean menores. 

### Interaciones no covalentes 

#### Hidrofóbicas
Interacciones entre solutos hidrofóbicos en soluciones acuosas
#### Van der Waals 
Entre átomos no cargados, como el solapamiento de sus orbitales externos por la ausencia de carga
#### Interacciones electroestáticas 
Inversamente proporcionales a la distancia entre atomos de cargas propias o inducidas, conocidos tambien co,o puentes salinos
#### Puentes H  
Longitud fija entre moléculas de carga opuesta.  


# Proteínas 

## Estructura primaría 
Es la representación más plana 


## Estructura secundaría 
Es la representación en donde se involucran las interacciones no covalentes formando estructuras comunes  

### Alfa hélice 
Dextrógira o levógira se crea cuando se hacen giro de alrededor de $5.4 A^°$ de distancia entre la formación de un enlace de hidrogeno. 

![](https://th.bing.com/th/id/R.b211b6f246b4507a54b8ddc4abd88506?rik=dpn5KUeaDrDznQ&riu=http%3a%2f%2f1.bp.blogspot.com%2f_iTcZbbl8vBQ%2fTLxgTJU7u5I%2fAAAAAAAAAFQ%2fa3vECfgdBDQ%2fs1600%2fAlfa%2bhelice.gif&ehk=72Ky9EZ0SB1Y6NUwoclW0Yw0j0Wu1%2bxFl5ron%2fTPfOY%3d&risl=&pid=ImgRaw&r=0)



### Beta plegada 
Se da como una conformación estructural de las proteínas en donde la secuencia de aminoácidos se alinea mediante hojas consecutivas que pueden ser **paralelas** o **antiparalelas** 

![](https://th.bing.com/th/id/R.c5b9dbbf98bad6e83c384b1d4e2b3ac9?rik=dg7W60qJg9CQCg&riu=http%3a%2f%2f3.bp.blogspot.com%2f-ThoILNTeCTc%2fUxvid7tlqjI%2fAAAAAAAAcF8%2fFlhDjU8m2Tw%2fs1600%2fbeta.gif&ehk=4FSBuYDFc0q4Ukq2cWeZiBiAyZUDblypTKydiYNDwxA%3d&risl=&pid=ImgRaw&r=0) 


>Se puede hacer una distinción de estas estructuras a través de los grados de libertad que sí tienen las secuencias de anotación cómo los enlaces $\phi$ y $\psi$ que son los enlaces entre en amino terminal y el carboxilo de cada carbono alfa respectivamente.  

![](https://wou.edu/chemistry/files/2019/07/ramachandran-improved-1024x898.png)





### Nomenclatura 
Así como existe un single letter code para la estructura primaria e identificar los aminoácidos, existe una identificación del estado de su estructura secundario llamados estados, existen algunos que discriminan entre 3 esenciales: **H** para alfa hélices **Q** para beta plegadas y **C** para cualquier otra, sin embargo, existen otros muchos para identificar hasta 8 estados:  
- **G** hélice 310 con vuelta de 3 residuos

- **H** α-hélice con vuelta de 4 residuos

- **I** π-hélice con vuelta de 5 residuos

- **T** giros de 3-5 residuos con puentes de H entre residuos vecinos

- **E** conformación extendida de lámina  β

- **B** puente  β  entre segmentos de tres residuos en conformación extendida  β

- **S** giro de gran curvatura sin puentes de H

- **C** resto de conformaciones


## Estructura terciaria
Se puede describir como la formación de dominios, es decir que cuentan como una unidad funcional, bioinformaticamenete se puede caracterizar como un alineamiento de un grupo de proteínas que cuentan con esa secuencia conservada. 

### Proteínas globulares 
Son el tipo de estructura secundaría más común dentro del citoplasma ya que se caracterizan por ser glóbulos en los que los aminoácidos hidrofóbicos se asocian en el core de la proteína por la presencia en una disolución acuosa.  

#### Matriz de contactos 
Una matriz de contactos puede servir como la representación de las estructuras que se encuentran en 

#### Dominios en CATH DB 
[CATH: Protein Structure Classification Database at UCL](https://www.cathdb.info/) 


## Alineamientos y superposiciones 
Relación entre la conservación de la estructura y de la secuencia, algunos autores han explorado como la conservación de la secuencia altera la estructura secundaría (RMSD root median square desviation), lo que se ha visto es que la perdida de la identidad en la secuencia causa una divergencia estructural exponencial que también es dependiente de la región estructural donde ocurren las mutaciones. 

**A si mismo la estructura es más conservada que la secuencia de las proteínas**. 


## PDB 
Esto se maneja mediante ficheros de textos y sus formatos:

### PDB 
Maneja las coordenadas atómicas mediante sus coordenadas cartesianas de sus átomos, así mismo se optaba por nombrar por combinaciones de 4 caracteres iniciadas por un número como IDs.

### mmCIF 
Es mejor para representar proteínas complejas con muchas cadenas. 

>gemmi permite convertir entre ambos formatos 






