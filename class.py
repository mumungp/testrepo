# class
class employee():
    
    def __init__(self, input_name,input_nik):
        self.name = input_name
        self.nik  = input_nik

    def status(self,kondisi):
        print(self.name,', id :',self.nik, kondisi)

# main program
danish = employee('danish faeyza',12345)
print(danish.name)
print(danish.nik)
danish.status('active')



import pandas as pd
import csv

df = pd.read_csv("D:\personal\DATA SCIENCE\IBM\data_car.csv")
df.head(5)




 