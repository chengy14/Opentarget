import json
import gzip
#from pprint import pprint
with gzip.open("/mnt/home/chengy14/evidence_data.json.gz", "r") as f, open("drug_info.csv","w") as d:
    d_columns = 'drug_name\tdrug_max_phase_for_all_diseases\tmolecule_type\n'
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
               drug_max_phase_for_all_diseases=line['drug']['max_phase_for_all_diseases']['label']
               molecule_type=line['drug']['molecule_type']
        d.write('\t'.join([str(drug_name),str(drug_max_phase_for_all_diseases),str(molecule_type)])+ "\n")
        line=f.readline()
    