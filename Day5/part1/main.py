import os
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE_PATH = os.path.join(FILE_PATH, "../data/input.txt")
TEST_FILE_PATH = os.path.join(FILE_PATH, "../data/test.txt")

seeds = []
seedtosoil = []
soiltofertilizer = []
fertilizertowater = []
watertolight = []
lighttotemperature = []
temperaturetohumidity = []
humiditytolocation = []

def processseeds():
    for seed in seeds:
        for element in seedtosoil:
            if seed.seed >= element.sourcestart and seed < element.sourcestart+element.range:
                seed.soil = seed.seed + element.delta

        

def processmap(line,map):
    map.append({
        "sourcestart" : line[1],
        "destinationstart" : line[0],
        "range" : line[2],
        "delta" : int(line[0]) - int(line[1])
    })

def readseeds(line):
    for seed in line:
        seeds.append({
            "seed" : seed,
            "soil" : -1,
            "fertilizer" : -1,
            "water" : -1,
            "light": -1,
            "temperature": -1,
            "humidity": -1,
            "location": -1
        })

def main():
    with open(TEST_FILE_PATH,"r") as file:
    # with open(INPUT_FILE_PATH,"r") as file:
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
    
    print("Read")
    


if __name__ == '__main__':
    main()