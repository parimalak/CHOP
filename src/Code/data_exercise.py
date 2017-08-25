# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 12:42:43 2017

@author: Parimala Killada
"""

import sqlite3
import pandas as pd
conn = sqlite3.connect("/CHOP/Data/openmrs.db")
cur = conn.cursor()
#List of tables in SQLite database 
cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
results = cur.fetchall()
print(results)
cur.execute("SELECT * FROM patient limit 5;")
results = cur.fetchall()
print(results)
cur.execute("SELECT * FROM encounter limit 5;")
results = cur.fetchall()
print(results)
cur.execute("SELECT * FROM encounter_diagnosis limit 5;")
results = cur.fetchall()
print(results)
cur.execute("SELECT * FROM lab_result limit 5;")
results = cur.fetchall()
print(results)
cur.execute("SELECT * FROM diagnosis limit 5;")

results = cur.fetchall()
print(results)

#DB EXercise1
#Provide a list of male patients in the database and the counts of patients by gender
cur.execute("pragma table_info(encounter);")
results = cur.fetchall()
print(results)

#DB EXercise1

#Provide a list of male patients in the database and the counts of patients by gender

table = pd.read_sql("SELECT count(gender),gender FROM patient GROUP BY gender;",conn)
table.to_csv('/CHOP/src/output/output1.csv')

#cur.execute("SELECT count(gender),gender FROM patient GROUP BY gender;")
#results = cur.fetchall()
#print(results)
##[(1, ''), (3484, 'F'), (1800, 'M')]

table = pd.read_sql("SELECT mrn,id FROM patient WHERE gender ='M' ORDER BY mrn;",conn)
table.to_csv('/CHOP/src/output/output1_1.csv')

#cur.execute("SELECT mrn,id FROM patient WHERE gender ='M' ORDER BY mrn;")
#results = cur.fetchall()
#print(results)
#[('MRN000002', 2), ('MRN000006', 6), ('MRN000013', 13), ('MRN000016', 16), 
#('MRN000017', 17), ('MRN000018', 18), ('MRN000020', 20), ('MRN000036', 36), 
#('MRN000039', 39), ('MRN000044', 44), ('MRN000048', 48), ('MRN000053', 53), 
#('MRN000065', 65), ('MRN000075', 75), ('MRN000077', 77), ('MRN000092', 92), 
#('MRN000095', 95), ('MRN000098', 98), ('MRN000109', 109), ('MRN000118', 118),
#('MRN000122', 122), ('MRN000127', 127), ('MRN000131', 131), ('MRN000133', 133),
#...
#('MRN009288', 9288), ('MRN009293', 9293), ('MRN009300', 9300), ('MRN009305', 9305), 
#('MRN009306', 9306), ('MRN009307', 9307), ('MRN009309', 9309), ('MRN009316', 9316),
# ('MRN009321', 9321), ('MRN009322', 9322), ('MRN009324', 9324), ('MRN009334', 9334),
# ('MRN009342', 9342)]


###DB Exercise 2
#Count patients in database diagnosed with DERMITITIS at an encounter

table = pd.read_sql("SELECT count(distinct(E.patient_id)) As Patient_count from encounter E \
            join (select encounter_id as e_id from encounter_diagnosis \
            where diagnosis_id in \
            (select id from diagnosis WHERE name ='DERMATITIS')) as E_ID \
            on E.id =E_ID.e_id;",conn)
table.to_csv('/CHOP/src/output/output2.csv')

"""cur.execute("SELECT count(distinct(E.patient_id)) from encounter E \
            join (select encounter_id as e_id from encounter_diagnosis \
            where diagnosis_id in \
            (select id from diagnosis WHERE name ='DERMATITIS')) as E_ID \
            on E.id =E_ID.e_id;")
results = cur.fetchall()
print(results)
"""
##[(131,)]

##DB Exercise 3
#Provide a list patients, by MRN, who have had a CD4 count of less than 300.

table = pd.read_sql("SELECT distinct (p.mrn) FROM encounter e join \
            (select encounter_id as e_id from lab_result WHERE cd4 <300 ) \
            as E_ID on E_ID.e_id = e.id join patient p \
            on p.id = e.patient_id order by mrn;",conn)
table.to_csv('/CHOP/src/output/output3.csv')
"""
cur.execute("SELECT distinct (p.mrn) FROM encounter e join \
            (select encounter_id as e_id from lab_result WHERE cd4 <300 ) \
            as E_ID on E_ID.e_id = e.id join patient p \
            on p.id = e.patient_id order by mrn;")
results = cur.fetchall()
print(results)
"""
##[('MRN003396',), ('MRN000574',), ('MRN003353',), ('MRN001954',), ('MRN001846',), 
#('MRN003229',), ('MRN002724',), ('MRN002309',), ('MRN000048',), ('MRN000520',), 
#('MRN002773',), ('MRN001787',), ('MRN000461',), ('MRN003492',), ('MRN001029',), 
#('MRN000432',), ('MRN005616',), ('MRN001264',), ('MRN001204',), ('MRN001886',), 
#('MRN001717',), ('MRN002176',), ('MRN003454',), 
#..
#('MRN009203',), ('MRN009212',), ('MRN009223',), ('MRN009232',), ('MRN009238',), 
#('MRN009241',), ('MRN009243',), ('MRN009247',), ('MRN009253',), ('MRN009265',), 
#('MRN009278',), ('MRN009284',), ('MRN009298',), ('MRN009301',), ('MRN009303',), 
#('MRN009336',), ('MRN009338',), ('MRN009344',)]

##DB Exercise 4
#Count all female patients above the age of 30 in the database as of today’s date

table = pd.read_sql("SELECT count(Age) as older_than_30 from \
                    (select (strftime('%Y', 'now') - strftime('%Y', birthdate)) - \
(strftime('%m-%d', 'now') < strftime('%m-%d', birthdate)) AS Age \
From patient where gender ='F' and Age >30);",conn)
table.to_csv('/CHOP/src/output/output4.csv')

"""
cur.execute("SELECT count(Age) from (select (strftime('%Y', 'now') - strftime('%Y', birthdate)) - \
(strftime('%m-%d', 'now') < strftime('%m-%d', birthdate)) AS Age From patient where gender ='F' and Age >30);")
results = cur.fetchall()
print(results)
#[(2808,)]
"""

conn.close()
