from csv import reader
from csv import writer
import random

# Open and read the first csv
with open('masterList.csv', 'r') as file:
    master = reader(file)
    master_list = list(master)
    all_names = set(map(tuple, master_list))
    #print(all_names)
print("number of total records " + str(len(all_names)))
file.close()

# open the tracker csv
with open('trackerList.csv', 'r') as used_name_file:
        used_names = reader(used_name_file)
        used_names_list = list(used_names)
        used_names_set = set(map(tuple, used_names_list))
        #print(used_names_set)
        print("number of used names so far " + str(len(used_names_set)))

# Reconcile between used names and the master list
z = all_names.difference(used_names_set)
master_list = list(z)

# check that it has been converted back into a list
# print(master_list)
print("number of records left you can use " + str(len(master_list)))

# select a random Brine Value
brineName = random.choice(master_list)
print(brineName)


newBrineName = [brineName[0]]
newBrineName = (" ".join(map(str, newBrineName)))
print(newBrineName)

print("Welcome to Brine " + str(newBrineName) + "!")

# write new brine item to csv tracker so it doesn't get used in the future

with open('trackerList.csv', 'a') as tracker_file:
     tracker = reader(tracker_file)
     addBrineName = writer(tracker_file)
     addBrineName.writerow(brineName)
     tracker_file.close()