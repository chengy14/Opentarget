import csv
from operator import itemgetter

with open("/mnt/home/chengy14/evidence_test_gene_to_drug_removed.csv", 'r') as f:
    data = [line for line in csv.reader(f)]
    data.sort(key=itemgetter(0))  # 1 being the column number

with open('evidence_test_gene_to_drug_removed_sorted.csv', 'w') as f:
    newRecord = 'geneid\tgene_name\tsymbol\ttarget_name\ttarget_type\tdrug_name\tdrug_molecule_type\n'
    
    f.write(newRecord)
    csv.writer(f).writerows(data)