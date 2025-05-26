# Bioinformatics_Works
Some bioinformatics python script and folder


1. `seed_extend.ipynb`: Including kmer index building, kmer extend, ungapped alignment, and local alignment. Input: 2 well-processed FASTA files and output will be the hits.
  
2. `UPGMA_phylogenetic_TreeBuilding.ipynb`: Including UPGMA code for building the phylogenetic tree, and input is MSA.seq and fasta seq file, output is the phylo tree. `A2utils.py` file should be downloaded together.

3. `Human Gut Microbiome Atlas/`: The comparison table of taxa id (msp_xxxx) and taxa name on Human Microbiome Atlas.

4. `minimum_entropy_score.py`: An alternate scoring system based on entropy score to assess the multiple sequence alignment quality, where $c_i$ is the number of occurrence of character i in a column and C is the number of sequences in the MSA.
![image](https://github.com/user-attachments/assets/742b29ed-1d34-4c97-b5d4-c9083896534f)

5. `Colless_imbalance.py`: Colless imbalance is a metric for the shape of phylo trees. $T_R$ and $T_L$ are the number of taxa descended from the right and left branches respectively of an interior node. $(n-1)(n-2)/2$ is the maximum possible value of the numerator, and the imbalanced value $I_c$ ranges from 0 to 1.


