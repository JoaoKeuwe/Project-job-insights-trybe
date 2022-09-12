from functools import lru_cache
import csv


@lru_cache
def read(path):

    with open(path) as file:
        filecsv = csv.DictReader(file, delimiter=",", quotechar='"')
        newFile = []
        for data in filecsv:
            newFile.append(data)
    return newFile
