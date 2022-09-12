from functools import lru_cache
import csv

@lru_cache
def read(path):
   newFile = []
   with open(path) as file:
      filecsv = csv.DictReader(file)
      for data in filecsv:
         newFile.append(data)
   return newFile 
