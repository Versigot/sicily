import numpy as np
import random



print('Welcome to the game! Please choose a car!')
print('')
print('1. Lancia D24')
print('2. Maserati A6GCS')
print('3. Ferrari 500 Mondial')
print('4. Fiat 8V Zagato')
print('')
car = input()
print('')

D24Specs = np.array([26, 26, 3.2, 260, 25])
A6Specs = np.array([34, 34, 2, 170, 17])
FerrariSpecs = np.array([26, 26, 2, 170, 10])
FiatSpecs = np.array([49, 49, 2, 127, 5])

if car == '1':
    CarSpecs = np.array([26, 26, 3.2, 260, 0])
if car == '2':
    CarSpecs = np.array([34, 34, 2, 170, 17])
if car == '3':
    CarSpecs = np.array([26, 26, 2, 170, 10])
if car == '4':
    CarSpecs = np.array([49, 49, 2, 127, 5])

## Fuel Reference, Fuel Tank, Fuel Usage, Horsepower, Chance of Breaking Down



class City:
	def __init__(self, connect1, connect2, connect3, connect4, connect5, connect6, connect7, connect8, distance1, distance2, distance3, distance4, distance5, distance6, distance7, distance8, fuel):
		self.connect1 = connect1
		self.connect2 = connect2
		self.connect3 = connect3
		self.connect4 = connect4
		self.connect5 = connect5
		self.connect6 = connect6
		self.connect7 = connect7
		self.connect8 = connect8
		self.distance1 = distance1
		self.distance2 = distance2
		self.distance3 = distance3
		self.distance4 = distance4
		self.distance5 = distance5
		self.distance6 = distance6
		self.distance7 = distance7
		self.distance8 = distance8
		self.fuel = fuel

RAG = City("MDR", "MOD", "COM", "GIA", "nan", "nan", "nan", "nan", 33, 11, 8, 17, "nan", "nan", "nan", "nan", 1)

COM = City("RAG", "VIT", "nan", "nan", "nan", "nan", "nan", "nan", 8, 8, "nan", "nan", "nan", "nan", "nan", "nan", 0)

VIT = City("COM", "GLA", "nan", "nan", "nan", "nan", "nan", "nan", 8, 15, "nan", "nan", "nan", "nan", "nan", "nan", 0)

MDR = City("RAG", "POZ", "nan", "nan", "nan", "nan", "nan", "nan", 33, 31, "nan", "nan", "nan", "nan", "nan", "nan", 0)

POZ = City("MDR", "MOD", "NTO", "CAP", "nan", "nan", "nan", "nan", 31, 30, 41, 40, "nan", "nan", "nan", "nan", 0)

MOD = City("RAG", "POZ", "NTO", "CAP", "nan", "nan", "nan", "nan", 11, 30, 41, 40, "nan", "nan", "nan", "nan", 0)

CAP = City("POZ", "NTO", "MOD", "nan", "nan", "nan", "nan", "nan", 40, 36, 40, "nan", "nan", "nan", "nan", "nan", 0)

NTO = City("SIR", "CAP", "MOD", "POZ", "nan", "nan", "nan", "nan", 31, 36, 41, 41, "nan", "nan", "nan", "nan", 0)

SIR = City("NTO", "FLO", "AUG", "nan", "nan", "nan", "nan", "nan", 31, 14, 21, "nan", "nan", "nan", "nan", "nan", 1)

AUG = City("SIR", "LEN", "nan", "nan", "nan", "nan", "nan", "nan", 21, 24, "nan", "nan", "nan", "nan", "nan", "nan", 0)

LEN = City("CAT", "AUG", "nan", "nan", "nan", "nan", "nan", "nan", 31, 24, "nan", "nan", "nan", "nan", "nan", "nan", 0)

FLO = City("SIR", "PAL", "nan", "nan", "nan", "nan", "nan", "nan", 14, 18, "nan", "nan", "nan", "nan", "nan", "nan", 0)

PAL = City("GIA", "FLO", "CAL", "nan", "nan", "nan", "nan", "nan", 12, 18, 48, "nan", "nan", "nan", "nan", "nan", 0)

GIA = City("RAG", "PAL", "nan", "nan", "nan", "nan", "nan", "nan", 17, 12, "nan", "nan", "nan", "nan", "nan", "nan", 0)

def converter(cCode):
	cityCodes = ["RAG", "COM", "VIT", "MDR", "POZ", "MOD", "CAP", "NTO", "SIR", "AUG", "LEN", "FLO", "PAL", "GIA"]
	cityNames = ["Ragusa", "Comiso", "Vittoria", "Marina di Ragusa", "Pozzallo", "Modica", "Capo Passero", "Noto Marioa", "Siracusa", "Augusta", "Lentini", "Floridia", "Palazzolo Acreide", "Giarratana"]

	i = 0

	while(cCode != cityCodes[i]):
		i += 1

	return cityNames[i]


print("Welcome to " + converter(RAG.connect1) + "!")




