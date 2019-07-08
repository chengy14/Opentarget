from more_itertools import unique_everseen
with open ('disease_evidence.csv','r') as f, open('disease_info_removed.csv','w') as out:
     out.writelines(unique_everseen(f))