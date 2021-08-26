import string
import networkx as nx
import matplotlib.pyplot as plt
import pprint

class Gis:
    # we will process the `gis.dat` file here. its parsed using the parseCityInfo() and parseEdges() functions
    def __init__(self):
        filename = 'gis'
        self.allCities = []
        self.alphabeticalCities = {}
        self.stateCities = {}
        self.allEdges = {}
        # we open the gis.dat file using with.
        with open(f'{ filename }.dat', 'r') as gisFile:
            self.gisData = gisFile.read().split('\n')

        cityNum = -1
        distStart = False
        skipLineCount = 0
        # parses all city details
        for idx, line in enumerate(self.gisData):
            if not line or line[0] == '*':
                continue
                # checks if line starts with a city
            # check if line contains a city
            if line[0] in string.ascii_letters:
                cityDetails = self.parseCityInfo(line)

                if not cityDetails['cityName'][0] in self.alphabeticalCities:
                    self.alphabeticalCities[cityDetails['cityName'][0]] = []
                if not cityDetails['stateCode'] in self.stateCities:
                    self.stateCities[cityDetails['stateCode']] = []

                cityDetails['id'] = len(self.allCities)
                self.alphabeticalCities[cityDetails['cityName'][0]].append(cityDetails)
                self.stateCities[cityDetails['stateCode']].append(cityDetails)
                self.allCities.append(cityDetails)
                cityNum += 1
                # checks if line has distance i.e weight
            elif line[0] in string.digits:
                if not distStart:
                    distStart = True
                    # call parseEdges to get all data.
                    skipLineCount = self.parseEdges(cityNum, idx)
                    if skipLineCount == 1:
                        distStart = False
                else:
                    if skipLineCount == 1:
                        distStart = False
                    else:
                        skipLineCount -= 1

        self.selectedCities = [False for _ in self.allCities]
        self.selectedEdges = {key:False for key in self.allEdges}
    # parses the text containing city info using split() and strip()
    def parseCityInfo(self, line):
        commaSeparated = line.split(',')
        cityName = commaSeparated[0]
        stateCode = commaSeparated[1].split('[')[0].strip()
        latitude = int(commaSeparated[1].split('[')[1]) / 100
        longitude = int(commaSeparated[2].split(']')[0]) / 100
        population = int(commaSeparated[2].split(']')[1])
        return {'cityName': cityName, 'stateCode': stateCode, 'latitude': latitude, 'longitude': longitude, 'population': population}

    def parseEdges(self, cityNum, gisFileIdx):
        distString = ""
        skipLineCount = 0
        while(True):
            skipLineCount += 1
            distString += self.gisData[gisFileIdx] + ' '
            gisFileIdx += 1
            if len(self.gisData) == gisFileIdx + 1 or self.gisData[gisFileIdx][0] not in string.digits:
                break

        distString = distString.strip()
        distList = [int(i) for i in distString.split(' ')]

        for idx, dist in enumerate(distList):
            self.allEdges[(cityNum, idx)] = dist


        return skipLineCount

    # selects all cities
    def selectAllCities(self):
        self.selectedCities = [True for _ in self.selectedCities]

    # unselects all cities
    def unselectAllCities(self):
        self.selectedCities = [False for _ in self.selectedCities]
    # selects all Edges
    def selectAllEdges(self):
        self.selectedEdges = {key:True for key in self.allEdges}
    # unselectalledges
    def unselectAllEdges(self):
        self.selectedEdges = {key:False for key in self.allEdges}
    # cleans edges when cities are deselected. called from `selectCities()`
    def cleanEdges(self):
        for cityIds in self.selectedEdges:
            if self.selectedEdges[cityIds]:
                if not self.selectedCities[cityIds[0]] or not self.selectedCities[cityIds[1]]:
                    self.selectedEdges[cityIds] = False
    def selectCities(self, attribute, lowerBound, upperBound = None):
        # different attributes are passed
        if attribute == 'name':
            for alphabet in self.alphabeticalCities:
                if alphabet not in string.ascii_uppercase[string.ascii_uppercase.index(lowerBound): string.ascii_uppercase.index(upperBound) + 1]:
                    for city in self.alphabeticalCities[alphabet]:
                        self.selectedCities[city['id']] = False

        if attribute == 'state':
            for state in self.stateCities:
                if state != lowerBound:
                    for city in self.stateCities[state]:
                        self.selectedCities[city['id']] = False

        elif attribute == 'latitude':
            for city in self.allCities:
                if lowerBound > city['latitude'] or upperBound < city['latitude']:
                    self.selectedCities[city['id']] = False

        elif attribute == 'longitude':
            for city in self.allCities:
                if lowerBound > city['longitude'] or upperBound < city['longitude']:
                    self.selectedCities[city['id']] = False

        elif attribute == 'population':
            for city in self.allCities:
                if lowerBound > city['population'] or upperBound < city['population']:
                    self.selectedCities[city['id']] = False
        self.cleanEdges()

    def selectEdges(self, lowerBound, upperBound):
        for cityIds in self.allEdges:
            if lowerBound > self.allEdges[cityIds] or upperBound < self.allEdges[cityIds]:
                self.selectedEdges[cityIds] = False


    def printCities(self, attribute = None, choice = None):
        selectedCitiesDetails = list(filter(lambda city: self.selectedCities[city['id']], self.allCities))
        if not attribute or attribute == 'name':
            sortedNameCities = sorted(selectedCitiesDetails, key = lambda city: city['cityName'])
            for city in sortedNameCities:
                self.printCity(city, choice)
        elif attribute == 'state':
            for state in self.stateCity:
                for city in self.stateCity[state]:
                    self.printCity(city, choice)
        elif attribute == 'latitude':
            sortedLatitudeCities = sorted(selectedCitiesDetails, key = lambda city: city['latitude'])
            for city in sortedLatitudeCities:
                self.printCity(city, choice)
        elif attribute == 'longitude':
            sortedLongitudeCities = sorted(selectedCitiesDetails, key = lambda city: city['longitude'])
            for city in sortedLongitudeCities:
                self.printCity(city, choice)
        elif attribute == 'population':
            sortedPopulationCities = sorted(selectedCitiesDetails, key = lambda city: city['population'])
            for city in sortedPopulationCities:
                self.printCity(city, choice)

    def printEdges(self):
        selectedEdgesDetails = {k:v for k,v in self.allEdges.items() if self.selectedEdges[k]}
        for k, v in selectedEdgesDetails.items():
            # print(k, v))
            print(f'({ k[0] }, { k[1] }): { v }')

    def printCity(self, city, choice):
        if choice == 'S' or not choice:
            print(f'ID: { city["id"] }\t{ city["cityName"] }: { city["stateCode"] }')
        elif choice == 'F':
            print(f'ID: { city["id"] }\tCity Name: { city["cityName"] } State: { city["stateCode"] } Latitude: { city["latitude"] } Longitude: { city["longitude"] } Population: { city["population"] }')
    
    def printPopulationDistr(self, partSize = None):
        populationList = []
        for city in self.allCities:
            if self.selectedCities[city['id']]:
                populationList.append(city['population'])
        maxPopulation = max(populationList)
        if not partSize:
            equalParts = maxPopulation // 3
            print(f'[0, { equalParts }]: { len([pop for pop in populationList if pop < equalParts ]) }')
            print(f'[{equalParts}, { equalParts * 2 }]: { len([pop for pop in populationList if pop >= equalParts and pop <= equalParts*2 ]) }')
            print(f'[{equalParts * 2}, { maxPopulation }]: { len([pop for pop in populationList if pop >= equalParts * 2]) }')
        else:
            low = 0
            high = partSize
            while high < maxPopulation:
                popCount = len([pop for pop in populationList if pop >= low and pop <= high])
                if popCount:
                    print(f'[{low}, { high }: { len([pop for pop in populationList if pop >= low and pop <= high]) }')
                low += partSize
                high += partSize
            print(f'[{low}, { high }: {len([pop for pop in populationList if pop >= low and pop <= high])}')

    def printPopulatedStates(self, num = None):
        if not num:
            num = 3
        totalPopulation = { k:0 for k, v in self.stateCities.items() }
        for state in self.stateCities:
            for city in self.stateCities[state]:
                totalPopulation[state] += city['population']
        topPop = sorted(totalPopulation.values(), reverse = True)[:num]
        topStates = [None] * num
        for state in totalPopulation:
            if totalPopulation[state] in topPop:
                topStates[topPop.index(totalPopulation[state])] = state
        for idx in range(len(topStates)):
            print(f'{ topStates[idx] }: { topPop[idx] }')

def main():
    gsystem = Gis()
    gsystem.selectAllCities()
    gsystem.selectAllEdges()
    delimiter = '\n*************************************\n'
    #### EXPERIMENT 1 ####
    gsystem.printCities()
    print(delimiter)
    # print full display
    gsystem.printCities('population', 'F')
    print(delimiter)
    #### EXPERIMENT 2 ####
    # select all cities with latitudes between 40N and 50N
    # and longitudes between 85W and 130W.
    gsystem.selectCities('latitude',40,50)
    gsystem.selectCities('longitude',85,130)
    gsystem.printCities('name', 'F')
    gsystem.printEdges()
    gsystem.printPopulationDistr(20000)
    gsystem.selectAllCities()
    gsystem.selectCities('state', 'CA')
    gsystem.printCities('name', 'F')
    gsystem.printPopulatedStates()

if __name__ == '__main__':
    main()
