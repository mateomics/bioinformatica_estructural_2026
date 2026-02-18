#!/bin/bash
ss="$1"
aa="$2"
id="$3"
#Programa que devuelve las secuencias fasta de los archivos *ss.fa y *aa.fa 
#Argumentos 
#   $1:path archivo *ss.fa
#   $2:path archivo *aa.fa
#   $3:id de secuencia a devolver
    
#guardamos los argumentos
ss=$1
aa=$2
id=$3 

#creamos el directorio de salida
if [[ ! -d "../results" ]]; then
    mkdir ../results
fi
outfile="../results/${id}_merge.fa"

#obtenemos las lineas referentes al id del fasta
seq_ss=$(awk -v id="$id" '$0 ~ "^>"id {flag=1; next}/^>/ {flag=0} flag{printf "%s", $0}' "$ss")

seq_aa=$(awk -v id="$id" '$0 ~ "^>"id {flag=1; next}/^>/ {flag=0} flag{printf "%s", $0}' "$aa")

#creamos el archivo de salida
echo ">$id" > "$outfile"
echo "${seq_aa}${seq_ss}" >> "$outfile"