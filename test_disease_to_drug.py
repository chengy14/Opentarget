import json
import gzip
# READ data from gz File
with gzip.open("/mnt/home/chengy14/evidence_data.json.gz", "r") as f, open("evidence_test_disease_to_drug.csv","w") as d:
    d_columns = 'disease_label\tdisease_id\tdisease_therapeutic_area_label\tdrug_name\t\n'
    d.write(d_columns)
    
    # read line 
    line = f.readline()
    while line:
        # convert to json object
        line = json.loads(line.strip())
        # check whether dictionary contains 'drug' and 'disease'
        
        for key,value in line.items():
            if key == 'drug':
               drug_name=line['drug']['molecule_name']
            if key == 'disease':
               disease_label = line['disease']['efo_info']['label']
               disease_id_ = line['disease']['id']
               disease_therapeutic_area_label=line['disease']['efo_info']['therapeutic_area']['labels'][0]
        # write data into new file
        d.write('\t'.join([str(disease_label),str(disease_id_),str(disease_therapeutic_area_label),str(drug_name),])+ "\n")
        line=f.readline()
    
