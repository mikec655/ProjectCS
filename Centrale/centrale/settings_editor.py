import json

file_path = ""

def setFilePath(path):
    global file_path
    file_path = path
    
def readSettings():
    with open(file_path, "r") as settings_file:
        settings = json.load(settings_file)
        return settings

def writeSettings(settings):
    with open(file_path, "w") as settings_file:
        json.dump(settings, settings_file, indent=4)

def printSettings(settings): 
    for id in settings['aansturingen'].keys():
        print(settings['aansturingen'][id]['name'] + " met ID " + id + " heeft " + str(len(settings['aansturingen'][id]['sensor_value'])) + " sensoren:")
        for sensor_id in settings['aansturingen'][id]['sensor_value'].keys():
            print("\t- " + settings['sensor_name'][sensor_id] + " met ID " + sensor_id + " en grenswaarde " + str(settings['aansturingen'][id]['sensor_value'][sensor_id]) + ".")
            pass

setFilePath("Centrale/centrale/settings.json")
