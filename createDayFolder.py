import sys
import getopt
import os
from datetime import datetime
from pathlib import Path
from string import Template


def main(argv):
    today = datetime.today()
    templatePath = Path("template")
    year = today.year
    day = today.day

    errorMsg = """
    createDayFolder.py [-h] [-y <year>] [-d <day>] [-t <template>]
    
    
    -h:     Display this help message
    -y:     The Year as number
    -d:     The day as number
    -t:     The template folder as path
    """
    opts = None
    try:
        opts = getopt.getopt(
            argv, "hy:d:t:", ["year=", "day=", "template="])[0]
    except getopt.GetoptError as err:
        print("An error has occured")
        print(errorMsg)
        sys.exit(2)
    try:
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print(errorMsg)
                sys.exit()
            elif opt in ("-y", "--year"):
                year = int(arg)
            elif opt in ("-d", "--day"):
                day = int(arg)
            elif opt in ("-t", "--template"):
                templatePath = Path(arg)
    except Exception as err:
        print(err)
        print(errorMsg)
        sys.exit(2)

    destPath = Path("{:d}/{:02d}".format(year, day))
    if(destPath.exists()):
        print("Path does alread exists. Maybe define a day and/or year with -d and/or -y")
        sys.exit(0)
    else:
        destPath.mkdir(parents=True)

    for f in templatePath.iterdir():
        if(f.is_file()):
            with f.open("r") as file:
                contents = Template(file.read()).safe_substitute(
                    {"day": str(day), "year": str(year)})

            dest = destPath.joinpath(f.name)
            with dest.open(mode="w") as file:
                file.write(contents)
            print(f.name + " copied!")


if(__name__ == "__main__"):
    main(sys.argv[1:])
