from __future__ import print_function
from pathlib import Path
from math import sqrt
import SVD
import argparse as agp

""" prog3.1 Calcula la superposicion en 3D equivalente a un alineamiento de 
secuencia de dos proteinas del PDB. Genera un fichero PDB con la superposicion 
obtenida. """

__author__  = 'Bruno Contreras-Moreira' 

# 0) parametros del algoritmo: 
def leer_fasta_alineado(filepath):
	"""
	Lee el FASTA y devuelve
	un diccionario {dominio: secuencia}
	"""
	secuencias = {}
	header = None

	with open(filepath) as f:
		for line in f:
			line = line.strip()
			if not line:
				continue

			if line.startswith(">"):
				header = line[1:]
				secuencias[header] = ""
				continue
			secuencias[header] += line

	return secuencias

# 1) subrutinas
def lee_coordenadas_PDB(filename):
	""" Devuelve una lista de residuos, cada uno con las coordenadas de sus atomos. """
	
	coords = []
	pdbfile = open(filename, 'r')
	try:
		res, prev_resID = '', ''
		for line in pdbfile:
			if line[0:3] == 'TER':
				break
			if line[0:4] != 'ATOM':
				continue

			resID = line[17:26]

			if resID != prev_resID:
				if res != '':
					coords.append(res)
				res = line
			else:
				res += line

			prev_resID = resID

		if res != '':
			coords.append(res)

	finally:
		pdbfile.close()

	return coords


def coords_alineadas(align1, coords1, align2, coords2):
	""" Devuelve dos listas con las coordenadas CA alineadas. """
	
	total1, total2 = -1, -1
	align_coords1, align_coords2 = [], []

	if (length := len(align1)) != len(align2):
		print("# coords_alineadas: alineamientos tienen != longitud")
		return ([], [])

	for r in range(0, length):
		res1 = align1[r:r+1]
		res2 = align2[r:r+1]

		if res1 != '-':
			total1 += 1
		if res2 != '-':
			total2 += 1
		if res1 == '-' or res2 == '-':
			continue

		align_coords1.append(extrae_coords_atomo(coords1[total1], ' CA '))
		align_coords2.append(extrae_coords_atomo(coords2[total2], ' CA '))

	return (align_coords1, align_coords2)


def porcentaje_identidad(align1, align2):
	""" Devuelve el porcentaje de identidad entre dos alineamientos. """
	
	identicos, total = 0, 0

	for i in range(0, len(align1)):
		if (res1 := align1[i]) == '-' or (res2 := align2[i]) == '-':
			continue
		total += 1
		if res1 == res2:
			identicos += 1

	return 100.0 * identicos / total if total > 0 else 0.0


def extrae_coords_atomo(res, atomo_seleccion):
	""" Extrae coordenadas XYZ de un atomo especifico. """
	
	atom_coords = []
	for atomo in res.split("\n"):
		if atomo[12:16] == atomo_seleccion:
			atom_coords = [
				float(atomo[30:38]),
				float(atomo[38:46]),
				float(atomo[46:54])
			]
	return atom_coords


def calcula_superposicion_SVD(pdbh1, pdbh2, originalPDBname, fittedPDBname, test=False):
	""" Calcula matriz de rotacion y RMSD usando SVD. """

	def calcula_centro(coords):
		centro = [0, 0, 0]
		for coord in coords:
			for dim in range(0, 3):
				centro[dim] += coord[dim]
		for dim in range(0, 3):
			centro[dim] /= len(coords)
		return centro

	def calcula_coordenadas_centradas(coords, centro):
		ccoords, total = [], 0
		for coord in coords:
			ccoords.append(coord[:])
			for dim in range(0, 3):
				ccoords[total][dim] -= centro[dim]
			total += 1
		return ccoords

	def calcula_coordenadas_rotadas(coords, rotacion):
		rcoords = [0, 0, 0]
		for i in range(0, 3):
			tmp = 0.0
			for j in range(0, 3):
				tmp += coords[j] * rotacion[i][j]
			rcoords[i] = tmp
		return rcoords

	pdbfile = open(originalPDBname, 'w')
	print("HEADER %s\n" % pdbh1['file'], file=pdbfile)
	for res in pdbh1['coords']:
		print(res, file=pdbfile)
	print("TER\n", file=pdbfile)

	print("HEADER %s\n" % pdbh2['file'], file=pdbfile)
	for res in pdbh2['coords']:
		print(res, file=pdbfile)
	print("TER\n", file=pdbfile)
	pdbfile.close()

	coords1, coords2 = pdbh1['align_coords'], pdbh2['align_coords']

	centro1 = calcula_centro(coords1)
	centro2 = calcula_centro(coords2)

	ccoords1 = calcula_coordenadas_centradas(coords1, centro1)
	ccoords2 = calcula_coordenadas_centradas(coords2, centro2)

	matriz = [[0,0,0],[0,0,0],[0,0,0]]
	peso = 1.0 / len(ccoords1)

	for i in range(0, 3):
		for j in range(0, 3):
			tmp = 0.0
			for k in range(0, len(ccoords1)):
				tmp += ccoords1[k][i] * ccoords2[k][j] * peso
			matriz[i][j] = tmp

	[U, Sigma, V] = SVD.svd(matriz)

	rotacion = [[0,0,0],[0,0,0],[0,0,0]]
	for i in range(0, 3):
		for j in range(0, 3):
			rotacion[i][j] = (
				U[j][0]*V[i][0] +
				U[j][1]*V[i][1] +
				U[j][2]*V[i][2]
			)

	rmsd = 0.0
	for n in range(0, len(coords1)):
		coords1_rot = calcula_coordenadas_rotadas(ccoords1[n], rotacion)
		for i in range(0, 3):
			desv = ccoords2[n][i] - coords1_rot[i]
			rmsd += desv * desv

	rmsd /= len(coords1)

	pdbfile = open(fittedPDBname, 'w')

	print("HEADER %s (rotated)\n" % pdbh1['file'], file=pdbfile)

	for res in pdbh1['coords']:
		for atomo in res.split("\n"):
			if atomo == '':
				break

			atcoords = extrae_coords_atomo(res, atomo[12:16])

			atcoords[0] -= centro1[0]
			atcoords[1] -= centro1[1]
			atcoords[2] -= centro1[2]

			coords_rot = calcula_coordenadas_rotadas(atcoords, rotacion)

			atcoords[0] = centro2[0] + coords_rot[0]
			atcoords[1] = centro2[1] + coords_rot[1]
			atcoords[2] = centro2[2] + coords_rot[2]

			print("%s%8.3f%8.3f%8.3f%s" %
				(atomo[0:30], atcoords[0], atcoords[1], atcoords[2], atomo[54:]),
				file=pdbfile)

	print("TER\n", file=pdbfile)

	print("HEADER %s\n" % pdbh2['file'], file=pdbfile)
	for res in pdbh2['coords']:
		print(res, file=pdbfile)
	print("TER\n", file=pdbfile)

	pdbfile.close()

	return sqrt(rmsd)


def parser(): 
	"""
	Funcion para parsear argumentos de linea de comandos
	""" 
	#creamos el parser
	parser = agp.ArgumentParser(description="Parser para el programa prog3.1_modified.py") 
	#agregamos los argumentos
	parser.add_argument("-f", "--fasta",
						default="./foldmason_aa.fa", 
						type=str, 
						required=True, 
						help="Path del archivo FASTA con las secuencias alineadas") 
	parser.add_argument("-i", "--id", 
						type=str, 
						required=True, 
						help="IDs de las proteinas a analizar, separados por comas") 
	parser.add_argument("-d", "--data",
						default="",
						type=str,
						help="Path del directorio que contiene los archivos")
	#leemos los argumentos pasados y los guardamos en un objeto
	args = parser.parse_args() 
	return args

def main():
	"""
	Funcion principal del programa, que se encarga de ejecutar el flujo completo del programa 
	"""
	#Obtenemos y asignamos los argumentos de linea de comandos
	args = parser()
	path=args.data
	secuencias = leer_fasta_alineado(path + args.fasta)
	ids = [path + id.strip() for id in args.id.split(",")] 

	pdb = [{"file": (id + ".pdb"), "align": secuencias[Path(id).stem]} for id in ids]

	pdb[0]['coords'] = lee_coordenadas_PDB(pdb[0]['file'])
	pdb[1]['coords'] = lee_coordenadas_PDB(pdb[1]['file'])

	print("# total residuos: pdb1 = %s pdb2 = %s\n" %
		(len(pdb[0]['coords']), len(pdb[1]['coords'])))

	(pdb[0]['align_coords'], pdb[1]['align_coords']) = coords_alineadas(
		pdb[0]['align'], pdb[0]['coords'],
		pdb[1]['align'], pdb[1]['coords']
	)

	print("# total residuos alineados = %s\n" %
		(len(pdb[0]['align_coords'])))

	rmsd = calcula_superposicion_SVD(
		pdb[1], pdb[0],
		'original.pdb',
		'align_fit.pdb'
	)

	print("\n# coordenadas originales = original.pdb\n# superposicion optima:\n")
	print("# archivo PDB = align_fit.pdb\n# RMSD = %1.2f Angstrom\n" % (rmsd))

	print(f"# porcentaje de identidad en alineamiento de archivos "
		f"{pdb[0]['file']} y {pdb[1]['file']}: "
		f"{porcentaje_identidad(pdb[0]['align'], pdb[1]['align']):.2f}%\n")


if __name__ == "__main__":
	main()