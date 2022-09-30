from tkinter.tix import Select
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os

mydb = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'practice')
print(mydb)
data = []
# if mydb: 
#     print("The connection is successful")
# else:
#     print("The connection is failed")
# sql = 'Select * From close_contacts'
mycursor = mydb.cursor(dictionary=True)
# mycursor.execute(sql)
# print(mycursor)
# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)
# sql = "UPDATE close_contacts SET Date = 'Jul20' WHERE Date BETWEEN 20200701 AND 20200731"
# mycursor.execute(sql)

sql = """Select sum(`Alpha Delta Pi House`) + sum(`Belk Hall`) + sum(`CF Lynch Hall`) + sum(`Chi omega House`) + sum(`Elm Hall`) + 
sum(`Greek Village House 12`) + sum(`Greek Village House 4`) + sum(`Greek Village House 8`) + sum(`Hawthorn Hall`) + 
sum(`Holshouser Hall`) + sum(`Hunt Hall`) + sum(`Laurel Hall`) + sum(`Levine Hall`) + sum(`Martin Hall`) + sum(`Miltimore Hall`) + 
sum(`Oak Hall`) + sum(`Pine Hall`) + sum(`Sanford Hall`) + sum('Scott Hall') + sum(`Sigma Kappa House`) + sum(`Wallis Hall`) + 
sum(`Witherspoon Hall`) + sum(`Zeta Tau Alpha House`) AS total_sum_july
FROM Close_Contacts
Where Year_Month_Day = 'July_2020'"""
mycursor.execute(sql)
for result in mycursor:
    print(result)
    data.append(result['total_sum_july'])
sql = """Select sum(`Alpha Delta Pi House`) + sum(`Belk Hall`) + sum(`CF Lynch Hall`) + sum(`Chi omega House`) + sum(`Elm Hall`) + 
sum(`Greek Village House 12`) + sum(`Greek Village House 4`) + sum(`Greek Village House 8`) + sum(`Hawthorn Hall`) + 
sum(`Holshouser Hall`) + sum(`Hunt Hall`) + sum(`Laurel Hall`) + sum(`Levine Hall`) + sum(`Martin Hall`) + sum(`Miltimore Hall`) + 
sum(`Oak Hall`) + sum(`Pine Hall`) + sum(`Sanford Hall`) + sum('Scott Hall') + sum(`Sigma Kappa House`) + sum(`Wallis Hall`) + 
sum(`Witherspoon Hall`) + sum(`Zeta Tau Alpha House`) AS total_sum_august
FROM Close_Contacts
Where Year_Month_Day = 'August_2020'"""
mycursor.execute(sql)
for result in mycursor:
    print(result)
    data.append(result['total_sum_august'])
sql = """Select sum(`Alpha Delta Pi House`) + sum(`Belk Hall`) + sum(`CF Lynch Hall`) + sum(`Chi omega House`) + sum(`Elm Hall`) + 
sum(`Greek Village House 12`) + sum(`Greek Village House 4`) + sum(`Greek Village House 8`) + sum(`Hawthorn Hall`) + 
sum(`Holshouser Hall`) + sum(`Hunt Hall`) + sum(`Laurel Hall`) + sum(`Levine Hall`) + sum(`Martin Hall`) + sum(`Miltimore Hall`) + 
sum(`Oak Hall`) + sum(`Pine Hall`) + sum(`Sanford Hall`) + sum('Scott Hall') + sum(`Sigma Kappa House`) + sum(`Wallis Hall`) + 
sum(`Witherspoon Hall`) + sum(`Zeta Tau Alpha House`) AS total_sum_september
FROM Close_Contacts
Where Year_Month_Day = 'September_2020'"""
mycursor.execute(sql)
for result in mycursor:
    print(result)
    data.append(result['total_sum_september'])
sql = """Select sum('Alpha Delta Pi House 1') + sum('Belk Hall') + sum('CF Lynch Hall') + sum('Chi omega House') + sum('Elm Hall') + 
sum('Greek Village House 12') + sum('Greek Village House 4') + sum('Greek Village House 8') + sum('Hawthorn Hall') + sum('Holshouser Hall') + sum('Hunt Hall') + sum('Laurel Hall') + sum('Levine Hall') + sum('Martin Hall') + sum('Miltimoe Hall') + 
sum('Oak Hall') + sum('Pine Hall') + sum('Sanford Hall') + sum('Scott Hall') + sum('Sigma Kappa Hall') + sum('Wallis Hall') + 
sum('Witherspoon Hall') + sum('Zeta Tau Alpha House') AS total_sum_october
FROM Close_Contacts
Where Year_Month_Day = 'October_2020'"""
mycursor.execute(sql)
for result in mycursor:
    print(result)
    data.append(result['total_sum_october'])
sql = """Select sum(`Alpha Delta Pi House`) + sum(`Belk Hall`) + sum(`CF Lynch Hall`) + sum(`Chi omega House`) + sum(`Elm Hall`) + 
sum(`Greek Village House 12`) + sum(`Greek Village House 4`) + sum(`Greek Village House 8`) + sum(`Hawthorn Hall`) + 
sum(`Holshouser Hall`) + sum(`Hunt Hall`) + sum(`Laurel Hall`) + sum(`Levine Hall`) + sum(`Martin Hall`) + sum(`Miltimore Hall`) + 
sum(`Oak Hall`) + sum(`Pine Hall`) + sum(`Sanford Hall`) + sum('Scott Hall') + sum(`Sigma Kappa House`) + sum(`Wallis Hall`) + 
sum(`Witherspoon Hall`) + sum(`Zeta Tau Alpha House`) AS total_sum_november
FROM Close_Contacts
Where Year_Month_Day = 'November_2020'"""
mycursor.execute(sql)
for result in mycursor:
    print(result)
    data.append(result['total_sum_november'])
sql = """Select sum(`Alpha Delta Pi House`) + sum(`Belk Hall`) + sum(`CF Lynch Hall`) + sum(`Chi omega House`) + sum(`Elm Hall`) + 
sum(`Greek Village House 12`) + sum(`Greek Village House 4`) + sum(`Greek Village House 8`) + sum(`Hawthorn Hall`) + 
sum(`Holshouser Hall`) + sum(`Hunt Hall`) + sum(`Laurel Hall`) + sum(`Levine Hall`) + sum(`Martin Hall`) + sum(`Miltimore Hall`) + 
sum(`Oak Hall`) + sum(`Pine Hall`) + sum(`Sanford Hall`) + sum('Scott Hall') + sum(`Sigma Kappa House`) + sum(`Wallis Hall`) + 
sum(`Witherspoon Hall`) + sum(`Zeta Tau Alpha House`) AS total_sum_december
FROM Close_Contacts
Where Year_Month_Day = 'December_2020'"""
mycursor.execute(sql)
for result in mycursor:
    print(result)
    data.append(result['total_sum_december'])
sql = """Select sum(`Alpha Delta Pi House`) + sum(`Belk Hall`) + sum(`CF Lynch Hall`) + sum(`Chi omega House`) + sum(`Elm Hall`) + 
sum(`Greek Village House 12`) + sum(`Greek Village House 4`) + sum(`Greek Village House 8`) + sum(`Hawthorn Hall`) + 
sum(`Holshouser Hall`) + sum(`Hunt Hall`) + sum(`Laurel Hall`) + sum(`Levine Hall`) + sum(`Martin Hall`) + sum(`Miltimore Hall`) + 
sum(`Oak Hall`) + sum(`Pine Hall`) + sum(`Sanford Hall`) + sum('Scott Hall') + sum(`Sigma Kappa House`) + sum(`Wallis Hall`) + 
sum(`Witherspoon Hall`) + sum(`Zeta Tau Alpha House`) AS total_sum_january
FROM Close_Contacts
Where Year_Month_Day = 'January_2021'"""
mycursor.execute(sql)
for result in mycursor:
    print(result)
    data.append(result['total_sum_january'])
sql = """Select sum(`Alpha Delta Pi House`) + sum(`Belk Hall`) + sum(`CF Lynch Hall`) + sum(`Chi omega House`) + sum(`Elm Hall`) + 
sum(`Greek Village House 12`) + sum(`Greek Village House 4`) + sum(`Greek Village House 8`) + sum(`Hawthorn Hall`) + 
sum(`Holshouser Hall`) + sum(`Hunt Hall`) + sum(`Laurel Hall`) + sum(`Levine Hall`) + sum(`Martin Hall`) + sum(`Miltimore Hall`) + 
sum(`Oak Hall`) + sum(`Pine Hall`) + sum(`Sanford Hall`) + sum('Scott Hall') + sum(`Sigma Kappa House`) + sum(`Wallis Hall`) + 
sum(`Witherspoon Hall`) + sum(`Zeta Tau Alpha House`) AS total_sum_feburary
FROM Close_Contacts
Where Year_Month_Day = 'Feburary_2021'"""
mycursor.execute(sql)
for result in mycursor:
    print(result)
    data.append(result['total_sum_feburary'])
sql = """Select sum(`Alpha Delta Pi House`) + sum(`Belk Hall`) + sum(`CF Lynch Hall`) + sum(`Chi omega House`) + sum(`Elm Hall`) + 
sum(`Greek Village House 12`) + sum(`Greek Village House 4`) + sum(`Greek Village House 8`) + sum(`Hawthorn Hall`) + 
sum(`Holshouser Hall`) + sum(`Hunt Hall`) + sum(`Laurel Hall`) + sum(`Levine Hall`) + sum(`Martin Hall`) + sum(`Miltimore Hall`) + 
sum(`Oak Hall`) + sum(`Pine Hall`) + sum(`Sanford Hall`) + sum('Scott Hall') + sum(`Sigma Kappa House`) + sum(`Wallis Hall`) + 
sum(`Witherspoon Hall`) + sum(`Zeta Tau Alpha House`) AS total_sum_march
FROM Close_Contacts
Where Year_Month_Day = 'March_2021'"""
mycursor.execute(sql)
for result in mycursor:
    print(result)
    data.append(result['total_sum_march'])
sql = """Select sum(`Alpha Delta Pi House`) + sum(`Belk Hall`) + sum(`CF Lynch Hall`) + sum(`Chi omega House`) + sum(`Elm Hall`) + 
sum(`Greek Village House 12`) + sum(`Greek Village House 4`) + sum(`Greek Village House 8`) + sum(`Hawthorn Hall`) + 
sum(`Holshouser Hall`) + sum(`Hunt Hall`) + sum(`Laurel Hall`) + sum(`Levine Hall`) + sum(`Martin Hall`) + sum(`Miltimore Hall`) + 
sum(`Oak Hall`) + sum(`Pine Hall`) + sum(`Sanford Hall`) + sum('Scott Hall') + sum(`Sigma Kappa House`) + sum(`Wallis Hall`) + 
sum(`Witherspoon Hall`) + sum(`Zeta Tau Alpha House`) AS total_sum_april
FROM Close_Contacts
Where Year_Month_Day = 'April_2021'"""
mycursor.execute(sql)
for result in mycursor:
    print(result)
    data.append(result['total_sum_april'])
sql = """Select sum(`Alpha Delta Pi House`) + sum(`Belk Hall`) + sum(`CF Lynch Hall`) + sum(`Chi omega House`) + sum(`Elm Hall`) + 
sum(`Greek Village House 12`) + sum(`Greek Village House 4`) + sum(`Greek Village House 8`) + sum(`Hawthorn Hall`) + 
sum(`Holshouser Hall`) + sum(`Hunt Hall`) + sum(`Laurel Hall`) + sum(`Levine Hall`) + sum(`Martin Hall`) + sum(`Miltimore Hall`) + 
sum(`Oak Hall`) + sum(`Pine Hall`) + sum(`Sanford Hall`) + sum('Scott Hall') + sum(`Sigma Kappa House`) + sum(`Wallis Hall`) + 
sum(`Witherspoon Hall`) + sum(`Zeta Tau Alpha House`) AS total_sum_may
FROM Close_Contacts
Where Year_Month_Day = 'May_2021'"""
mycursor.execute(sql)
for result in mycursor:
    print(result)
    data.append(result['total_sum_may'])

print(data)

PB1 = pd.DataFrame([['July_2020',0],['August_2020',0],['September_2020',0],['October_2020',0],['November_2020',36],['December_2020',24],['January_2021',91],['Feburary_2021',47]
,['March_2021',92],['April_20201',122],['May_2020',4]], columns= ['Months', 'Total_Sum_Close_Contacts'])
print(PB1)
PB1.plot(x='Months', kind='bar', stacked=False, edgecolor = 'Black', linewidth = 1.5, color = ['Red', 'Green', 'RoyalBlue'])
#plt.title("Wastewater Data Analysis", fontname = "Times New Roman", fontsize = 14, color = 'k')
plt.xlabel('Months', fontname = 'Times New Roman', fontsize = 14)
plt.ylabel('Close Contacts', fontname = 'Times New Roman', fontsize = 12)
plt.grid(False)
plt.xticks(weight = 'bold', rotation = 50, fontname = 'Times New Roman', fontsize = 12)
plt.yticks(weight = 'bold', fontname = 'Times New Roman', fontsize = 12)
plt.legend(prop={'family': 'Times New Roman'}, fontsize = 10)
os.chdir("/Users/neha/Desktop")
plt.savefig("Close_Contacts_Analysis.pdf", bbox_inches = 'tight')
plt.show()
