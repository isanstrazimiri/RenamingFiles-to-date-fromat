import re,os,shutil

#Create a regex that matches the files with the American date format
datePattern = re.compile(r"""^(.*?)
    ((0|1)>?\d)-      #one or two digits for the month
    ((0|1|2|3)?\d)-    #one or two digits for the day
    ((19|20)\d\d)       #4 digits for the year
    (.*?)$              #all text after the date
""",re.VERBOSE)

#Todo: Loop over files in the working directory

for amerFilename in os.listdir('C:\\Users\\ISAN\\PycharmProjects\RenamingFiles-to-Europ-Style-Date'):
    mo = datePattern.search(amerFilename)

    #Skip files without a date.
    if mo == None:
        continue

    #Get the different parts of the filename
    beforePart=mo.group(1)
    monthPart=mo.group(2)
    dayPart=mo.group(4)
    yearPart=mo.group(6)
    afterPart=mo.group(8)



#Todo: Form the European-style filename

euroFilename= beforePart +  dayPart + '-' + monthPart + '-' + yearPart + afterPart

#Todo: Get the full, absolute file paths

absWorkingDir = os.path.abspath('.')
amerFilename = os.path.join(absWorkingDir,amerFilename)
euroFilename = os.path.join(absWorkingDir,euroFilename)

#Todo: Rename the files
print('Renaming "%s" to "%s"...' %(amerFilename,euroFilename))
shutil.move(amerFilename,euroFilename)