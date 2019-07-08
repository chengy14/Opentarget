from more_itertools import unique_everseen
# drug file is needed to remove duplicates too
with open ('disease_evidence.csv','r') as f, open('disease_info_removed.csv','w') as out:
     out.writelines(unique_everseen(f))
