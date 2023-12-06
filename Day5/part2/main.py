import os
import sys
import time
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE_PATH = os.path.join(FILE_PATH, "../data/input.txt")
TEST_FILE_PATH = os.path.join(FILE_PATH, "../data/test.txt")

class Seed:
    def __init__(self, number, soil=-1, fertilizer=-1, water=-1, light=-1, temperature=-1, humidity=-1, location=-1):
        self.number = int(number)
        self.soil = int(soil)
        self.fertilizer = int(fertilizer)
        self.water = int(water)
        self.light = int(light)
        self.temperature = int(temperature)
        self.humidity = int(humidity)
        self.location = int(location)
    
    def __str__(self):
        return f"Seed {self.number}, soil {self.soil}, fertilizer {self.fertilizer}, water {self.water}, light {self.light}, temperature {self.temperature}, humidity {self.humidity}, location {self.location}"

class Map:
    def __init__(self, source, destination, lrange):
        self.source = int(source)
        self.destination = int(destination)
        self.lrange = int(lrange)
        self.delta = int(destination)-int(source)

seeds = []
seedtosoil = []
soiltofertilizer = []
fertilizertowater = []
watertolight = []
lighttotemperature = []
temperaturetohumidity = []
humiditytolocation = []

start = time.perf_counter()


def processseeds(seed):
    for element in seedtosoil:
        if seed.number >= element.source and seed.number < element.source+element.lrange:
            seed.soil = seed.number + element.delta
    if seed.soil == -1:
        seed.soil = seed.number

    for element in soiltofertilizer:
        if seed.soil >= element.source and seed.soil < element.source+element.lrange:
            seed.fertilizer = seed.soil + element.delta
    if seed.fertilizer == -1:
        seed.fertilizer = seed.soil

    for element in fertilizertowater:
        if seed.fertilizer >= element.source and seed.fertilizer < element.source+element.lrange:
            seed.water = seed.fertilizer + element.delta
    if seed.water == -1:
        seed.water = seed.fertilizer

    for element in watertolight:
        if seed.water >= element.source and seed.water < element.source+element.lrange:
            seed.light = seed.water + element.delta
    if seed.light == -1:
        seed.light = seed.water

    for element in lighttotemperature:
        if seed.light >= element.source and seed.light < element.source+element.lrange:
            seed.temperature = seed.light + element.delta
    if seed.temperature == -1:
        seed.temperature = seed.light

    for element in temperaturetohumidity:
        if seed.temperature >= element.source and seed.temperature < element.source+element.lrange:
            seed.humidity = seed.temperature + element.delta
    if seed.humidity == -1:
        seed.humidity = seed.temperature

    for element in humiditytolocation:
        if seed.humidity >= element.source and seed.humidity < element.source+element.lrange:
            seed.location = seed.humidity + element.delta
    if seed.location == -1:
        seed.location = seed.humidity

    return seed.location

def processmap(line,map):
    map.append(Map(line[1],line[0],line[2]))

def preprocessseeds(line):
    finallocation = sys.maxsize
    for i in range(0,int(len(line)/2)):
        for j in range(int(line[i*2]),int(line[i*2])+int(line[i*2+1])):
            loc = processseeds(Seed(j))
            if loc < finallocation:
                finallocation = loc
        temp = time.perf_counter()
        print(f"Processed range#: {i}, it took {temp-start: 0.2f} seconds")
    return finallocation

def readseeds(line):
    for element in line:
        seeds.append(int(element))

def main():
    # with open(TEST_FILE_PATH,"r") as file:
    with open(INPUT_FILE_PATH,"r") as file:
        lines = file.readlines()

    isseedtosoil = False
    issoiltofertilizer = False
    isfertilizertowater = False
    iswatertolight = False
    islighttotemperature = False
    istemperaturetohumidity = False
    ishumiditytolocation = False

    for line in lines:
        if line.find("seeds") != -1:
            readseeds(line.strip().replace("seeds: ","").split(" "))

        if line.find("seed-to-soil") != -1:
            isseedtosoil = True
            issoiltofertilizer = False
            isfertilizertowater = False
            iswatertolight = False
            islighttotemperature = False
            istemperaturetohumidity = False
            ishumiditytolocation = False
            continue
        elif line.find("soil-to-fertilizer") != -1:
            isseedtosoil = False
            issoiltofertilizer = True
            isfertilizertowater = False
            iswatertolight = False
            islighttotemperature = False
            istemperaturetohumidity = False
            ishumiditytolocation = False
            continue
        elif line.find("fertilizer-to-water") != -1:
            isseedtosoil = False
            issoiltofertilizer = False
            isfertilizertowater = True
            iswatertolight = False
            islighttotemperature = False
            istemperaturetohumidity = False
            ishumiditytolocation = False
            continue
        elif line.find("water-to-light") != -1:
            isseedtosoil = False
            issoiltofertilizer = False
            isfertilizertowater = False
            iswatertolight = True
            islighttotemperature = False
            istemperaturetohumidity = False
            ishumiditytolocation = False
            continue
        elif line.find("light-to-temperature") != -1:
            isseedtosoil = False
            issoiltofertilizer = False
            isfertilizertowater = False
            iswatertolight = False
            islighttotemperature = True
            istemperaturetohumidity = False
            ishumiditytolocation = False
            continue
        elif line.find("temperature-to-humidity") != -1:
            isseedtosoil = False
            issoiltofertilizer = False
            isfertilizertowater = False
            iswatertolight = False
            islighttotemperature = False
            istemperaturetohumidity = True
            ishumiditytolocation = False
            continue
        elif line.find("humidity-to-location") != -1:
            isseedtosoil = False
            issoiltofertilizer = False
            isfertilizertowater = False
            iswatertolight = False
            islighttotemperature = False
            istemperaturetohumidity = False
            ishumiditytolocation = True
            continue

        if(isseedtosoil and line.strip() != ""):
            processmap(line.strip().split(" "),seedtosoil)
        elif(issoiltofertilizer and line.strip() != ""):
            processmap(line.strip().split(" "),soiltofertilizer)
        elif(isfertilizertowater and line.strip() != ""):
            processmap(line.strip().split(" "),fertilizertowater)
        elif(iswatertolight and line.strip() != ""):
            processmap(line.strip().split(" "),watertolight)
        elif(islighttotemperature and line.strip() != ""):
            processmap(line.strip().split(" "),lighttotemperature)
        elif(istemperaturetohumidity and line.strip() != ""):
            processmap(line.strip().split(" "),temperaturetohumidity)
        elif(ishumiditytolocation and line.strip() != ""):
            processmap(line.strip().split(" "),humiditytolocation)

    print(preprocessseeds(seeds))
    end = time.perf_counter()
    print(f"Solution took {end-start: 0.2f} seconds")
    


if __name__ == '__main__':
    main()