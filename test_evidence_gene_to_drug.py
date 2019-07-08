import json
import gzip
#from pprint import pprint
with gzip.open("/mnt/home/chengy14/evidence_data.json.gz", "r") as f, open("evidence_test_gene_to_drug.csv","w") as d:
    d_columns = 'geneid\tgene_name\tsymbol\ttarget_name\ttarget_type\tdrug_name\tdrug_molecule_type\n'
    d.write(d_columns)
    
    # read line 
    line = f.readline()
    while line:
        # convert to json object
        line = json.loads(line.strip())
        # d data
        
        for key,value in line.items():
            if key == 'drug':
               drug_name=line['drug']['molecule_name']
               molecule_type=line['drug']['molecule_type']
            if key == 'target':
               geneid = line['target']['gene_info']['geneid']
               gene_name = line['target']['gene_info']['name']
               symbol=line['target']['gene_info']['symbol']
               
               for secondkey in line['target']:
                   if secondkey == 'target_name':
                      target_name=line['target']['target_name']
                   elif secondkey == 'target_class':
                      target_class=line['target']['target_class'][0]
               target_type=line['target']['target_type']
        d.write('\t'.join([str(geneid),str(gene_name),str(symbol),str(target_name),str(target_type),str(drug_name),str(molecule_type)])+ "\n")
        line=f.readline()
    