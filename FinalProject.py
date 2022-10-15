# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 15:31:28 2021

@author: Admin
"""

import csv
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy
import matplotlib.pyplot as plt
import cartopy.feature as cfeature
import numpy as np


#################read in flight data#########################3
text = open('C:/Users/Admin/Documents/ATOC/Final Project/FlightData.csv')
data = csv.reader(text)
header = next(data)
rows = []
for row in data:
    rows.append(row)

######################initialize data sets###################
total2021 = []    
average2021 = []
total2020 = []    
average2020 = []
total2019 = []
average2019 =[]

#######################parse the data#####################
dates = []
for i in range(0,365):
    for j in range(0,7):
        if j == 0:
            dates.append(rows[i][j])
        if j == 1:
            try:
                average2021.append(int(rows[i][j]))
            except ValueError:
                pass
        if j == 2:
            try:
                total2021.append(int(rows[i][j]))
            except ValueError:
                pass
        if j == 3:
            average2020.append(int(rows[i][j]))
        if j == 4:
            total2020.append(int(rows[i][j]))
        if j == 5:
            average2019.append(int(rows[i][j]))
        if j == 6:
            total2019.append(int(rows[i][j]))
            
###############plot the data########################

# Moving Average
dates2021 = dates[0:314]
plt.figure(0)
plt.plot(dates2021,average2021, label = '2021')
plt.plot(dates,average2020, label = '2020')
plt.plot(dates,average2019, label = '2019')
plt.legend()
plt.title('7 Day Moving Average of Flights')
ticks = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
labels = ['January 1st' , 'February 1st', 'March 1st', 'April 1st', 'May 1st', 'June 1st', 'July 1st', 'August 1st', 'September 1st', 'October 1st', 'Novemeber 1st', 'December 1st']
plt.xticks(ticks, labels, rotation = 45)

#Total Number of flights
plt.figure(1)
plt.plot(dates2021,total2021, label = '2021')
plt.plot(dates,total2020, label = '2020')
plt.plot(dates,total2019, label = '2019')
plt.legend()
plt.title('Total Number of Flights')
ticks = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
labels = ['January 1st' , 'February 1st', 'March 1st', 'April 1st', 'May 1st', 'June 1st', 'July 1st', 'August 1st', 'September 1st', 'October 1st', 'Novemeber 1st', 'December 1st']
plt.xticks(ticks, labels, rotation = 45)

####################Individual Airline Data###############################
def AirlineStatistics(file):
    text = open(file)
    data = csv.reader(text)
    header = next(data)
    rows = []
    for row in data:
        rows.append(row)
    TotalFlights = int(rows[4][1])
    AverageDelayDeparture = float(rows[4][2])
    AverageDelayArrival = float(rows[4][5])
    TotalCancelled = int(rows[4][8])
    TotalDiverted = int(rows[4][10])
    TotalLate = int(rows[8][1])
    AverageDelayDepartureLate = float(rows[8][2])
    AverageDelayArrivalLate = float(rows[8][5])
    return rows, TotalFlights, AverageDelayDeparture, AverageDelayArrival, TotalCancelled, TotalDiverted, TotalLate, AverageDelayDepartureLate, AverageDelayArrivalLate


######### Top 5 Airlines #########
#Delta
fileDelta2020 = 'C:/Users/Admin/Documents/ATOC/Final Project/Airline.csv'
rowsDelta2020, TotalFlightsDelta2020, AverageDelayDepartureDelta2020, AverageDelayArrivalDelta2020, TotalCancelledDelta2020, TotalDivertedDelta2020, TotalLateDelta2020, AverageDelayDepartureLateDelta2020, AverageDelayArrivalLateDelta2020 = AirlineStatistics(fileDelta2020)

fileDelta2021 = 'C:/Users/Admin/Documents/ATOC/Final Project/Delta2021.csv'
rowsDelta2021, TotalFlightsDelta2021, AverageDelayDepartureDelta2021, AverageDelayArrivalDelta2021, TotalCancelledDelta2021, TotalDivertedDelta2021, TotalLateDelta2021, AverageDelayDepartureLateDelta2021, AverageDelayArrivalLateDelta2021 = AirlineStatistics(fileDelta2021)
        
fileDelta2019 = 'C:/Users/Admin/Documents/ATOC/Final Project/Delta2019.csv'
rowsDelta2020, TotalFlightsDelta2019, AverageDelayDepartureDelta2019, AverageDelayArrivalDelta2019, TotalCancelledDelta2019, TotalDivertedDelta2019, TotalLateDelta2019, AverageDelayDepartureLateDelta2019, AverageDelayArrivalLateDelta2019 = AirlineStatistics(fileDelta2019)         

#American     
fileAmerican2019 = 'C:/Users/Admin/Documents/ATOC/Final Project/American2019.csv'
rowsAmerican2019, TotalFlightsAmerican2019, AverageDelayDepartureAmerican2019, AverageDelayArrivalAmerican2019, TotalCancelledAmerican2019, TotalDivertedAmerican2019, TotalLateAmerican2019, AverageDelayDepartureLateAmerican2019, AverageDelayArrivalLateAmerican2019 = AirlineStatistics(fileAmerican2019) 

fileAmerican2020 = 'C:/Users/Admin/Documents/ATOC/Final Project/American2020.csv'
rowsAmerican2020, TotalFlightsAmerican2020, AverageDelayDepartureAmerican2020, AverageDelayArrivalAmerican2020, TotalCancelledAmerican2020, TotalDivertedAmerican2020, TotalLateAmerican2020, AverageDelayDepartureLateAmerican2020, AverageDelayArrivalLateAmerican2020 = AirlineStatistics(fileAmerican2020)        

fileAmerican2021 = 'C:/Users/Admin/Documents/ATOC/Final Project/American2021.csv'
rowsAmerican2021, TotalFlightsAmerican2021, AverageDelayDepartureAmerican2021, AverageDelayArrivalAmerican2021, TotalCancelledAmerican2021, TotalDivertedAmerican2021, TotalLateAmerican2021, AverageDelayDepartureLateAmerican2021, AverageDelayArrivalLateAmerican2021 = AirlineStatistics(fileAmerican2021)

#Southwest
fileSouthwest2019 = 'C:/Users/Admin/Documents/ATOC/Final Project/Southwest2019.csv'
rowsSouthwest2019, TotalFlightsSouthwest2019, AverageDelayDepartureSouthwest2019, AverageDelayArrivalSouthwest2019, TotalCancelledSouthwest2019, TotalDivertedSouthwest2019, TotalLateSouthwest2019, AverageDelayDepartureLateSouthwest2019, AverageDelayArrivalLateSouthwest2019 = AirlineStatistics(fileSouthwest2019) 

fileSouthwest2020 = 'C:/Users/Admin/Documents/ATOC/Final Project/Southwest2020.csv'
rowsSouthwest2020, TotalFlightsSouthwest2020, AverageDelayDepartureSouthwest2020, AverageDelayArrivalSouthwest2020, TotalCancelledSouthwest2020, TotalDivertedSouthwest2020, TotalLateSouthwest2020, AverageDelayDepartureLateSouthwest2020, AverageDelayArrivalLateSouthwest2020 = AirlineStatistics(fileSouthwest2020)

fileSouthwest2021 = 'C:/Users/Admin/Documents/ATOC/Final Project/Southwest2021.csv'
rowsSouthwest2021, TotalFlightsSouthwest2021, AverageDelayDepartureSouthwest2021, AverageDelayArrivalSouthwest2021, TotalCancelledSouthwest2021, TotalDivertedSouthwest2021, TotalLateSouthwest2021, AverageDelayDepartureLateSouthwest2021, AverageDelayArrivalLateSouthwest2021 = AirlineStatistics(fileSouthwest2021)

#United
fileUnited2019 = 'C:/Users/Admin/Documents/ATOC/Final Project/United2019.csv'
rowsUnited2019, TotalFlightsUnited2019, AverageDelayDepartureUnited2019, AverageDelayArrivalUnited2019, TotalCancelledUnited2019, TotalDivertedUnited2019, TotalLateUnited2019, AverageDelayDepartureLateUnited2019, AverageDelayArrivalLateUnited2019 = AirlineStatistics(fileUnited2019) 

fileUnited2020 = 'C:/Users/Admin/Documents/ATOC/Final Project/United2020.csv'
rowsUnited2020, TotalFlightsUnited2020, AverageDelayDepartureUnited2020, AverageDelayArrivalUnited2020, TotalCancelledUnited2020, TotalDivertedUnited2020, TotalLateUnited2020, AverageDelayDepartureLateUnited2020, AverageDelayArrivalLateUnited2020 = AirlineStatistics(fileUnited2020)

fileUnited2021 = 'C:/Users/Admin/Documents/ATOC/Final Project/United2021.csv'
rowsUnited2021, TotalFlightsUnited2021, AverageDelayDepartureUnited2021, AverageDelayArrivalUnited2021, TotalCancelledUnited2021, TotalDivertedUnited2021, TotalLateUnited2021, AverageDelayDepartureLateUnited2021, AverageDelayArrivalLateUnited2021 = AirlineStatistics(fileUnited2021)


#################### Analyzing Airline Data #####################################

#Bar charts (Delay Departure)
DelayDepartures2019 = (AverageDelayDepartureDelta2019, AverageDelayDepartureAmerican2019, AverageDelayDepartureSouthwest2019, AverageDelayDepartureUnited2019)
DelayDepartures2020 = (AverageDelayDepartureDelta2020, AverageDelayDepartureAmerican2020, AverageDelayDepartureSouthwest2020, AverageDelayDepartureUnited2020)
DelayDepartures2021 = (AverageDelayDepartureDelta2021, AverageDelayDepartureAmerican2021, AverageDelayDepartureSouthwest2021, AverageDelayDepartureUnited2021)


N = 4
indicies = np.arange(N)
width = 0.25
plt.figure(3)
plt.bar(indicies, DelayDepartures2019, width, label = '2019')
plt.bar(indicies+width, DelayDepartures2020, width, label = '2020')
plt.bar(indicies+ (2*width), DelayDepartures2021, width, label = '2021')
plt.legend(loc='best')
plt.title('Average Departure Delay by Airline')
plt.ylabel('Delay (minutes)')
plt.xticks((indicies + width/2), ('Delta', 'American', 'Southwest', 'United'))
plt.show()

#TOtal Late flights
TotalLate2019 = (TotalLateDelta2019, TotalLateAmerican2019, TotalLateSouthwest2019, TotalLateUnited2019)
TotalLate2020 = (TotalLateDelta2020, TotalLateAmerican2020, TotalLateSouthwest2020, TotalLateUnited2020)
TotalLate2021 = (TotalLateDelta2021, TotalLateAmerican2021, TotalLateSouthwest2021, TotalLateUnited2021)
plt.figure(4)
plt.bar(indicies, TotalLate2019, width, label = '2019')
plt.bar(indicies+width, TotalLate2020, width, label = '2020')
plt.bar(indicies+ (2*width), TotalLate2021, width, label = '2021')
plt.legend(loc='best')
plt.title('Total number of Late Flights by Airline')
plt.ylabel('Flights')
plt.xticks((indicies + width/2), ('Delta', 'American', 'Southwest', 'United'))
plt.show()

#Total Cancelled Flights
TotalCancelled2019 = (TotalCancelledDelta2019, TotalCancelledAmerican2019, TotalCancelledSouthwest2019, TotalCancelledUnited2019)
TotalCancelled2020 = (TotalCancelledDelta2020, TotalCancelledAmerican2020, TotalCancelledSouthwest2020, TotalCancelledUnited2020)
TotalCancelled2021 = (TotalCancelledDelta2021, TotalCancelledAmerican2021, TotalCancelledSouthwest2021, TotalCancelledUnited2021)
plt.figure(5)
plt.bar(indicies, TotalCancelled2019, width, label = '2019')
plt.bar(indicies+width, TotalCancelled2020, width, label = '2020')
plt.bar(indicies+ (2*width), TotalCancelled2021, width, label = '2021')
plt.legend(loc='best')
plt.title('Total number of Cancelled Flights by Airline')
plt.ylabel('Flights')
plt.xticks((indicies + width/2), ('Delta', 'American', 'Southwest', 'United'))
plt.show()
################### Major Airport Data #############################################
# Examining percent decrease in flights pre/post covid by red and blue states:
    
# Blue States: California (LAX), Colorado (DEN), New York (JFK)
# Red: Texas (DFW), Arizona (PHX), Florida (MCO)

def AirportAnalysis(filepre, filecovid):
    textpre = open(filepre)
    datapre = csv.reader(textpre)
    headerpre = next(datapre)
    rowspre = []
    for rowpre in datapre:
        rowspre.append(rowpre)
    totalFlightsPre = int(rowspre[5][1])
    
    textcovid = open(filecovid)
    datacovid = csv.reader(textcovid)
    headercovid = next(datacovid)
    rowscovid = []
    for rowcovid in datacovid:
        rowscovid.append(rowcovid)
    totalFlightsCovid = int(rowscovid[5][1])
    
    PercentDifference = ((totalFlightsCovid - totalFlightsPre) / totalFlightsPre) * 100
    PercentDifference = round(PercentDifference,2)
    return PercentDifference
    
    
# Blue States    
fileLAXCovid = 'C:/Users/Admin/Documents/ATOC/Final Project/LAXCovid.csv'
fileLAXPreCovid = 'C:/Users/Admin/Documents/ATOC/Final Project/LAXPreCovid.csv'
PercentDifferenceLAX = AirportAnalysis(fileLAXPreCovid,fileLAXCovid)

fileDENCovid = 'C:/Users/Admin/Documents/ATOC/Final Project/DENCovid.csv'
fileDENPreCovid = 'C:/Users/Admin/Documents/ATOC/Final Project/DENPreCovid.csv'
PercentDifferenceDEN = AirportAnalysis(fileDENPreCovid,fileDENCovid)

fileJFKCovid = 'C:/Users/Admin/Documents/ATOC/Final Project/JFKCovid.csv'
fileJFKPreCovid = 'C:/Users/Admin/Documents/ATOC/Final Project/JFKPreCovid.csv'
PercentDifferenceJFK = AirportAnalysis(fileJFKPreCovid,fileJFKCovid)

#Red States
fileDFWCovid = 'C:/Users/Admin/Documents/ATOC/Final Project/DFWCovid.csv'
fileDFWPreCovid = 'C:/Users/Admin/Documents/ATOC/Final Project/DFWPreCovid.csv'
PercentDifferenceDFW = AirportAnalysis(fileDFWPreCovid,fileDFWCovid)

filePHXCovid = 'C:/Users/Admin/Documents/ATOC/Final Project/PHXCovid.csv'
filePHXPreCovid = 'C:/Users/Admin/Documents/ATOC/Final Project/PHXPreCovid.csv'
PercentDifferencePHX = AirportAnalysis(filePHXPreCovid,filePHXCovid)

fileMCOCovid = 'C:/Users/Admin/Documents/ATOC/Final Project/MCOCovid.csv'
fileMCOPreCovid = 'C:/Users/Admin/Documents/ATOC/Final Project/MCOPreCovid.csv'
PercentDifferenceMCO = AirportAnalysis(fileMCOPreCovid,fileMCOCovid)


####################### Representing Airport Data ##############################




central_lat = 40.0150
central_lon = -105.2705
extent = [-140, -60, 20, 60]
LAXlong = 118.4
LAXlat = 33.9
DENlong = -104.6
DENlat = 39.8
JFKlong = -73.7
JFKlat = 40.6
DFWlong = -96.7
DFWlat = 32.77
PHXlong = -112
PHXlat = 33.4
MCOlong = -81
MCOlat = 28.4

figure = plt.figure(figsize=(8,6))

ax = figure.add_subplot(1,1,1, projection=ccrs.PlateCarree())
ax.coastlines(resolution='50m')
ax.add_feature(cartopy.feature.OCEAN)
ax.add_feature(cartopy.feature.LAND, edgecolor='black')
ax.add_feature(cartopy.feature.LAKES, edgecolor='black')
ax.add_feature(cartopy.feature.RIVERS)
ax.add_feature(cartopy.feature.STATES, edgecolor='grey')
ax.set_extent(
    [-135, -60, 20, 55],
    crs=ccrs.PlateCarree()
)
plt.plot(-118.4,33.9,'bo',markersize=7,transform=ccrs.PlateCarree())
ax.text(-LAXlong+1.5,LAXlat,'54.71% decrease',transform=ccrs.Geodetic(),fontsize=8)
ax.text(-LAXlong-4,LAXlat,'LAX',transform=ccrs.Geodetic(),fontsize=8)

plt.plot(DENlong,DENlat,'mo',markersize=7,transform=ccrs.PlateCarree())
ax.text(DENlong+1.5,DENlat,'33.09% decrease',transform=ccrs.Geodetic(),fontsize=8)
ax.text(DENlong-4,DENlat,'DEN',transform=ccrs.Geodetic(),fontsize=8)

plt.plot(JFKlong,JFKlat,'bo',markersize=7,transform=ccrs.PlateCarree())
ax.text(JFKlong+1.5,JFKlat,'65.73% decrease',transform=ccrs.Geodetic(),fontsize=8)
ax.text(JFKlong-4,JFKlat,'J FK',transform=ccrs.Geodetic(),fontsize=8)

plt.plot(DFWlong,DFWlat,'ro',markersize=7,transform=ccrs.PlateCarree())
ax.text(DFWlong+1.5,DFWlat,'29.86% decrease',transform=ccrs.Geodetic(),fontsize=8)
ax.text(DFWlong-4,DFWlat,'DFW',transform=ccrs.Geodetic(),fontsize=8)

plt.plot(PHXlong,PHXlat-2,'ro',markersize=7,transform=ccrs.PlateCarree())
ax.text(PHXlong+1.5,PHXlat-2,'37.02% decrease',transform=ccrs.Geodetic(),fontsize=8)
ax.text(PHXlong-4,PHXlat-2,'PHX',transform=ccrs.Geodetic(),fontsize=8)

plt.plot(MCOlong,MCOlat-2,'mo',markersize=7,transform=ccrs.PlateCarree())
ax.text(MCOlong+1.5,MCOlat ,'40.43% decrease',transform=ccrs.Geodetic(),fontsize=8)
ax.text(MCOlong-4,MCOlat,'MCO',transform=ccrs.Geodetic(),fontsize=8)

plt.show()


