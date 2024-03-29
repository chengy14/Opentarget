import json
import gzip
#from pprint import pprint
with gzip.open("/mnt/home/chengy14/evidence_data.json.gz", "r") as f, open("disease_evidence.csv","w") as d:
    d_columns = 'disease_label\tdisease_id\tdisease_therapeutic_area_label\n'
    d.write(d_columns)
    
    # read line 
    line = f.readline()
    while line:
        # convert to json object
        line = json.loads(line.strip())
        # d data
        
        for key,value in line.items():
            #if key == 'drug':
               #drug_name=line['drug']['molecule_name']
            if key == 'disease':
               disease_label = line['disease']['efo_info']['label']
               disease_id_ = line['disease']['id']
               disease_therapeutic_area_label=line['disease']['efo_info']['therapeutic_area']['labels'][0]
        d.write('\t'.join([str(disease_label),str(disease_id_),str(disease_therapeutic_area_label)])+ "\n")
        line=f.readline()
    