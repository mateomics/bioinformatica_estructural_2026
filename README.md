# Structural Bioinformatics Projects 2026

**Authors:** Mateo Jiménez Sotelo & Ismael Maximiliano De Los Santos Huesca

## Overview

This repository contains practical projects developed during a Structural Bioinformatics module.

The exercises explore the relationship between protein sequence, structure, and function through modern computational approaches, including protein folding, structural alignment, structure comparison, and AI-based protein structure prediction.

---

## Topics Covered

### Day 1 — Protein Folding with Foldit

Introduction to protein structure through the Foldit platform.

Concepts explored:

* Protein folding principles
* Hydrophobic core formation
* Hydrogen bonding
* α-helices and β-sheets
* Disulfide bridges
* Effects of amino acid substitutions
* Protein conformational optimization

The goal was to understand how physicochemical interactions shape protein structure and stability.

---

### Day 2 — Structural Alignment and Comparison

Protein structures from the Protein Data Bank (PDB) were compared using structural alignment approaches.

Topics explored:

* Structural similarity
* RMSD calculation
* Sequence identity
* Fold conservation
* Foldseek
* FoldMason

Example comparison:

```text
Structure A: 3BJI
Structure B: 1X86
Aligned residues: 299
Sequence identity: 22.07%
RMSD: 5.16 Å
```

This exercise illustrates how proteins can maintain structural similarity despite low sequence identity.

---

### Day 3 — AlphaFold2 Validation

An experimentally determined protein structure (PDB: 5TPT) was compared against an AlphaFold2 prediction.

Metrics analyzed:

* Structural superposition
* RMSD
* Sequence identity
* Model agreement

Results:

```text
Aligned residues: 197
Sequence identity: 100%
RMSD: 1.27 Å
```

The low RMSD indicates strong agreement between the AlphaFold2 prediction and the experimentally determined structure.

---

### Day 4 — AlphaFold3 Structure Prediction

Structure prediction and quality assessment of the transcription factor EGR1 using AlphaFold3.

Analyses included:

* Protein sequence retrieval
* Multiple sequence alignment generation
* Template identification
* Structure prediction
* Confidence assessment
* Model quality evaluation
* Structural visualization

Quality metrics explored:

* pLDDT
* Predicted aligned error (PAE)
* Ramachandran analysis
* Local quality estimates

---

## Repository Structure

```text
.
├── Dia1/
│   ├── docs/
│   └── results/
│
├── Dia2/
│   ├── data/
│   ├── docs/
│   ├── results/
│   └── src/
│
├── Dia3/
│   ├── data/
│   ├── figures/
│   ├── results/
│   └── src/
│
└── Dia4/
    ├── data/
    ├── figures/
    ├── results/
    └── src/
```

---

## Software and Resources

* Foldit
* Protein Data Bank (PDB)
* Foldseek
* FoldMason
* AlphaFold2
* AlphaFold3
* Python
* Bash
* PyMOL
* Structural biology databases

---

## Skills Demonstrated

* Structural bioinformatics
* Protein structure analysis
* Structural alignment
* RMSD interpretation
* Fold comparison
* Protein visualization
* AlphaFold model evaluation
* AI-based protein structure prediction
* Computational biology workflows

---

## Learning Outcomes

This project provides practical experience with modern structural bioinformatics workflows, ranging from fundamental protein folding concepts to state-of-the-art AI-driven structure prediction methods.

The collection highlights how experimental structures and computational predictions can be integrated to study protein architecture and function.
