import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#pip install pytrends
from pytrends.request import TrendReq

summerApparel =['sunglasses', 'bathing suit', 'shorts', 'sandals', 'towels']
timeframe = 'today 5-y'
pytrends = TrendReq()

#Menue for the user with the choices
def displaymenu():
    print("""
    Summer Aparel Trends in North America
    __
    1. Mexico Data
    2. United States Data
    3. Canada Data
    4. Compare keywords
    5. Exit
    """)

def getData(country):
    pytrends.build_payload(kw_list=summerApparel, timeframe= timeframe, geo = country)
    # Interest Over Time
    overtimedf = pytrends.interest_over_time()
    print(overtimedf.head())

def graphData(graph,country):
    if graph == 'YES' or 'yes' or 'Yes':
         #Interest By Region
        regiondf = pytrends.interest_by_region(resolution=country)
        #looking at rows where all values are not equal to 0
        regiondf = regiondf[(regiondf != 0).all(1)]
        #drop all rows that have null values in all columns
        regiondf.dropna(how='all',axis=0, inplace=True)
        #visualise
        regiondf.plot(y=summerApparel, kind ='bar')
        #regiondf.show()


#MAIN FUNCTION -> Program running
def main():

    while True: 
        displaymenu()
        choice = input('Enter your choice:')
        print(choice)

        if choice == "1":
            country = 'MX'
            getData(country)
            graph = input('Would you like to graph this data? \n1. YES \n2. NO:')
            graphData(graph, country)

        elif choice == "2":
            country ='US'
            getData(country)
            graph = input('Would you like to graph this data?\n 1. YES \n2. NO:')
            print('Your answer was', graph)
            print('You will now see a graph for', country, 'data')
            graphData(graph, country)
          
        elif choice == "3":
            country ='CA'
            getData(country)
            graph = input('Would you like to graph this data? \n 1. YES \n 2. NO:')
            print('Your answer was', graph)
            graphData(graph, country)
            

        elif choice == "4":
            #dataComparison()
            print('dataComparison') #Needs to be build

        elif choice == "5":
            break   
        else: 
            print("Enter a valid choice")
            

if __name__ == "__main__":
    main()




