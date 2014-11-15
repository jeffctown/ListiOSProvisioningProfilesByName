from os import listdir
import os

#Change this variable to the your user name in OSX
user = "jlett"

path = "/Users/" + user + "/Library/MobileDevice/Provisioning Profiles"

for thisPath in next(os.walk(path))[2]:
    fullPath = os.path.join(path,thisPath)
    baseCommand = "/usr/libexec/PlistBuddy -c 'Print :Name' /dev/stdin <<< $(security cms -D -i '"
    command = baseCommand + fullPath + "')"
    print thisPath + " - " + os.popen(command).read()
