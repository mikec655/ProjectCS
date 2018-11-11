import json

file_path = ""

def setFilePath(path):
    # set het filepad naar het .json settings bestand.
    global file_path
    file_path = path
    
def readSettings():
    # hier wordt het .json bestand gelezen.
    with open(file_path, "r") as settings_file:
        settings = json.load(settings_file)
        return settings

def writeSettings(settings):
    # hier wordt er in het .json bestand geschreven.
    with open(file_path, "w") as settings_file:
        json.dump(settings, settings_file, indent=4)

setFilePath("Centrale/centrale/settings.json")
