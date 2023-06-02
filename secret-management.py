from sys import argv
import re
import yaml

default_rules = ["url","password","secret","usr","base64"]

def define_rules(rule):
    keyPattern, valuePattern = "", ""
    if rule == "url":
        keyPattern = "^.*(Endpoint|host|Host|Registry).*$"
        valuePattern = "^[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\+.~#?&//=]*)$"
    if rule == "password":
        keyPattern = "^\S*(pass(words?|wd|phrase)?|pwd)_?(hash)?[0-9]*$"
        valuePattern = ".*"
    if rule == "apikey":
        keyPattern = ".*[A-Za-z0-9\-\_]+(key|token)$"
        valuePattern = "^(?!.*[ ])"
    if rule == "usr":
        keyPattern = "^.*(Name|name|id|Id).*$"
        valuePattern = "\w+$"
    if rule == "base64":
        keyPattern = ""
        valuePattern = "^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$"
    return keyPattern, valuePattern

def detect_secrets(lineChecked, location):
    # key, value = dict(lineChecked).keys()[0], dict(lineChecked).values()[0]
    # if value.startswith("#"):
    #     value = ""
    print(str(lineChecked).index(":"))
    # secret_check = False
    # for rule in default_rules:
    #     keyPattern, valuePattern = define_rules(rule=rule)
    #     regexKey, regexValue = re.compile(keyPattern), re.compile(valuePattern)
    #     if value == "":
    #         if regexKey.match(key):
    #             secret_check = True
    #             print("Found the secret in location {location}".format(location=location))
    #         else:
    #             secret_check = False
                
    # return secret_check
    # print("Found the secret in location {location}".format(location=location))
        

def __main__():
    # try:
    #     try:
            with open(argv[1], "r") as stream:
                count = 1
                for line in stream.readlines():
                    if line.replace(" ", "").startswith("#"):
                        pass
                    elif line == "\n":
                        pass
                    else:
                        detect_secrets(lineChecked=line.replace(" ", "").replace("\n",""), location=count)
                    count = count + 1
                    
    #     except FileNotFoundError:
    #         print("Something wrong on your file, It doesn't exist or wrong path. Try Again !!!")
    #         exit(1)
    # except IndexError:
    #     print("Missing a path for the log file, pass in and try again !!!")
    #     exit(1)
        
if __name__ == "__main__":
    __main__()
