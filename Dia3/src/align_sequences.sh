#!/bin/bash 
#$-N
#script utilzado para hacer el merge de dos secuencias fasta o más para posteriormente realizar el alineamiento multiple mediante clustalo 
#Argumentos 
#   $1:path del primer fasta
#   $2:path del segundo fasta
#   $3:id de secuencia 1 
#   #4:id secuencia 2(opcional si se busca el mismo id en los dos archivos) 

#asignamos los argumentos
fasta1=$1
fasta2=$2
id1=$3

if [[ -z $4 ]]; then
    id2=$3 
else 
    id2=$4
fi

#creamos las salidas 
#creamos el directorio de salida
if [[ ! -d "../results" ]]; then
    mkdir ../results
fi
out_merge="../data/${id}_merge.fa"
out_alig="../results/${id}_merge.fa"

#Primeros recuperamos las secuencias 
seq_1=$(awk -v id="$id1" '$0 ~ "^>"id {flag=1; next}/^>/ {flag=0} flag{printf "%s", $0}' "$fasta1")

seq_2=$(awk -v id="$id2" '$0 ~ "^>"id {flag=1; next}/^>/ {flag=0} flag{printf "%s", $0}' "$fasta2") 

echo ">$id1" > "$out_merge"
echo "${seq_1}\n>${id2}\n${seq_2}" >> "$out_merge"
#realizamos el alienamiento con clustalo 

clustalo -i "$out_merge" --iter 2 --use-kimura -o "$out_alig" --outfmt sta  --threads 4 
