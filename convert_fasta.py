from Bio import SeqIO

SeqIO.convert("/Users/rieke/Desktop/cod/cod.augustus.aa", "fasta","/Users/rieke/Desktop/cod_all_prots.fa",  "fasta-2line")

#SeqIO.convert("/Users/rieke/Desktop/razor_masked.fa", "fasta", "/Users/rieke/Desktop/raz_mask.fa", "fasta-2line")

#f = open('/Users/rieke/Desktop/razor_masked.fa', 'r')
#clean_records = []
#for record in SeqIO.parse(f, "fasta"):
#    record.seq = record.seq.rstrip('-')
 #   clean_records.append(record)

#with open('/Users/rieke/Desktop/razor_masked_clean.fa', 'w') as f:
 #   SeqIO.write(clean_records, f, 'fasta-2line')