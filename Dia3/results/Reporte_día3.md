## Modelamiento de una estructura a partir de la secuencia peptídica

Para este ejercicio se utilizarán distintos algoritmos de modelamiento de proteínas a partir de su secuencia con el fin de comparar la resolución de los mismos mediante métricas como el pLDDT.

Para este ejercicio se seleccionó una proteína del PDB de interés con el objetivo de comparar la estructura reportada con la predicha por algoritmos como AlphaFold2.

## 5TPT

### Estructura reportada

Esta es una proteína con estructura cristalográfica reportada en el PDB [RCSB PDB - 5TPT: The Crystal Structure of Amyloid Precursor-Like Protein 2 (APLP2) E2 Domain](https://www.rcsb.org/structure/5TPT) y corresponde al dominio E2 de la proteína precursora amiloidea, la cual está involucrada en la supervivencia, adhesión celular, desarrollo neuronal y enfermedades como el Alzheimer.  
![Fig1](5tpt_cristalograStr.jpeg)  
Fig 1. Estructura cristalográfica de la proteína 5TPT

### Predicción

Mediante el algoritmo de AlphaFold2 disponible en [AlphaFold2.ipynb - Colab](https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb#scrollTo=AzIKiDiCaHAn) utilizamos la secuencia `DVDVYFETSADDNEHARFQKAKEQLEIRHRNRMDRVKKEWEEAELQAKNLPKAERQTLIQHFQAMVKALEKEAASEKQQLVETHLARVEAMLNDRRRMALENYLAALQSDPPRPHRILQALRRYVRAENKDRLHTIRHYQHVLAVDPEKAAQMKSQVMTHLHVIEERRNQSLSLLYKVPYVAQEIQEEIDELLQEQR` para realizar la predicción con los siguientes parámetros:

- num_relax = 0
    
- template mode = none
    
- msa_mode = mmseqs2_uniref_env
    
- pair_mode = unpaired_paired
    
- model type = auto (en el caso de este monómero == alphafold2_ptm)
    
- recycle_early_stop_tolerance = auto (para el tipo de modelo --> num_recycles = 20)
    
- relax_max_iterations = 200
    
- pairing_strategy = greedy
    
- max_msa = auto
    
- num_seeds = 1
    

#### Resultado de la última iteración

![Fig2](5TPT_alphaFold2_predicted_lstItr.png)  
Fig 2. Última iteración (005) de la predicción AlphaFold2

#### Estructura 3D

![Fig3](5TPT_alphaFold2_predicted_renderStr.png)  
Fig 3. Estructura final predicha por el algoritmo, nuevamente coloreada por el pLDDT

![Fig4](pLDDT_scale.png)  
Fig 4. Escala de color de la calificación por pLDDT

### Comparación

Una vez realizadas estas predicciones, podemos proceder a comparar las estructuras mediante el script previamente utilizado `prog3.1_modified.py` (ruta relativa del repositorio /Dia2/src/prog3.1_modified.py).

```bash
# total residuos: pdb1 = 197 pdb2 = 197

# total residuos alineados = 197


# coordenadas originales = original.pdb
# superposicion optima:

# archivo PDB = align_fit.pdb
# RMSD = 1.27 Angstrom

# porcentaje de identidad en alineamiento de archivos ../../Dia3/data/5TPT.pdb y ../../Dia3/data/5TPT_pred_lstItr.pdb: 100.00%
```

### Comparación en base a otras metricas 
Para completar el analisis realizado se utilizo la herramienta de [swissmodel](https://swissmodel.expasy.org/assess/85LJQe/01), con el obejtivo de obtener metricas de similitud basada enn la estructura como el TM-score y la RSSMD y otras independientes del mismo como el IDDT.  

| Medida | Valor | 
|:-------:|:------:| 
| IDDT | 0.38 |
| TM-score | 0.51 | 
| RMSD | 1.11 | 


![Fig5](swiss_img.png)
Fig 5.Solapamiento entre estructura cristalografica y la predicdha coloreada por el por el IDDT

### Conclusión 
Los algoritmos de predicción en base a la estructura utilizan distintas aproximaciones para realizar la resolución estructural en base a la secuencia cruda, dentro el mismo procedimiento se busca homología entre secuencias para inferir posibles estructuras putativas en base a la homología o la inferencia de contactos por correlaciones entre sitios, en particular alfa fold2 parte de los alineamientos multiples para obtener información co-evolutiva entre las secuencias con el ideal de obtener distancias, contactos y angulos, como un algoritmo de aprendizaje de maquina basado en redes neuronales profundas obtiene distancias predichas de carbonos $\beta$ y anogulos $\psi$ y $\phi$ de la secuencia proteica, posteriormente hace la minimización de gradientes y relajación del esqueleto así como refinamiento de las cadenas laterales. Ya que este metodo se basa en la información registrada en las bases de datos de referencia que se tiene la predicción de nuestra secuencia que tiene una estructura cristalografica resgistrada tiene una mayor confianza, reflejada en su alto pLDDT en su estructura y alta similaridad con la estructura de referencia obtenida en PDB, con un bajon en el IDDT debido a unos choques ubicados en las partes exteriores de las alfas helices.
