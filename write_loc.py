import csv

# These columns may vary depending on what pops you have added to the game
# Change as necessary
id_column = 0
name_column = 14
culture_column = 1
religion_column = 2
tradegoods_column = 3
civilization_column = 12
barbarian_column = 13
province_rank_column = 13
area_column = 16
# Pop values
citizen_column = 4
freemen_column = 4
slaves_column = 9
tribesmen_column = 10
# Pops for the 1815 mod
lower_strata_column = 6
middle_strata_column = 7
upper_strata_column = 11
proletariat_column = 8

generated_localisation = open("GENERATED_LOCALISATION.yml","w")

setup_csv = open("province_setup.csv")
reader = csv.reader(setup_csv, delimiter=",")

def write_loc():
    with generated_localisation as f2:
        f2.write("l_english:\n")
        for row in reader:
            f2.write( " PROV" + row[id_column] + ":0 " + row[name_column] + "\n" )


write_loc()
