import gzip
import json


with gzip.open("/mnt/home/chengy14/association_data.json.gz", "r") as f, open('gene_association.csv', 'w') as file1, open('disease_association.csv', 'w') as file2:
    file1_columns = 'symbol\tname\tid\n'
    file1.write(file1_columns)
    
    file2_columns = 'disease_labels\tdisease_id\target-disease_id\n'
    file2.write(file2_columns)
    # read line 
    line = f.readline()
    while line:
        # convert to json object
        line = json.loads(line.strip())
        # file1 data
        gene = line['target']['gene_info']['symbol']
        name = line['target']['gene_info']['name']
        target_id = line['target']['id']
        # file2 data
        id_ = line['id']
        labels = line['disease']['efo_info']['therapeutic_area']['labels'][0]
        #codes = line['disease']['efo_info']['therapeutic_area']['codes'][0]
        #path = line['disease']['efo_info']['path'][0][0]
        id_disease = line['disease']['id']
        # write file1 and file2
        file1.write('\t'.join([gene, name, target_id])+ "\n")
        file2.write('\t'.join([labels,id_disease, id_])  + "\n")
        line = f.readline()
