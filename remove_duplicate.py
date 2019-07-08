

with open ("/mnt/home/chengy14/evidence_test_disease_to_drug.csv",'r') as in_file, open('evidence_test_disease_to_drug_removed.csv','w') as out_file:
    seen = set() # set for fast O(1) amortized lookup
    for line in in_file:
        if line in seen: continue # skip duplicate

        seen.add(line)
        out_file.write(line)
