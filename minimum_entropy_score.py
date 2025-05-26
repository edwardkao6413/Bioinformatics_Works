import math
import pandas as pd

### example case
# from Bio import AlignIO
# from Bio.Align import MultipleSeqAlignment
# from Bio.Seq import Seq
# from Bio.SeqRecord import SeqRecord
# seqs_a = [SeqRecord(Seq('ACGT')), SeqRecord(Seq('AGGT')), SeqRecord(Seq('AC-T'))]
# seqs_b = [SeqRecord(Seq('GCGGATATGGCGAT')), SeqRecord(Seq('GCAGATCTGGCGA-')), SeqRecord(Seq('GCGCATATTGCG--'))]

## Multiple Sequence Alignment object
# demo_msa_a = MultipleSeqAlignment(seqs_a)
# demo_msa_b = MultipleSeqAlignment(seqs_b)

def mes_score(msa):
    """
    input msa: multiple sequence alignment object from biopython (Bio.Align.MultipleSeqAlignment).
    
    minimum entropy score: Assess the quality of multiple sequence alignment by calculating a score for each column in the alignment.
    The score for each column is derived using entropy-based formula, which reflects the diversity of characters at that position.
    The total alignment score is calculated by summing the scores from all columns.
    Lower score indicates a better alignment.

    We treat a gap the same as any other character.
    """


    alignments_lst = [sequ.seq for sequ in msa]
    if len(alignments_lst) <= 2:
        return None
    
    df = pd.DataFrame()
    for i in range(len(alignments_lst)):
        df[i + 1] = list(alignments_lst[i])
    seq_ttln = len(alignments_lst)
    score = 0

    for seq_pos in range(len(df)):
        seq_freq = df.iloc[seq_pos].value_counts()
        if len(seq_freq) == 1:
            pass
        else:
            seq_freq_lst = list(seq_freq.values)
            for freq in seq_freq_lst:
                uncert = -(freq * math.log2(freq / seq_ttln))
                score += uncert
        
    return score