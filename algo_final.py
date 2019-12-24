#import library
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from sklearn.preprocessing import LabelEncoder

#Sorting
def partition(nums, low, high):
	pivot = nums[(low+high)//2]
	i = low-1
	j = high+1
	while True:
		i+=1
		while nums[i] < pivot:
			i+=1
		j-=1
		while nums[j] > pivot:
			j-=1
		if i >= j:
			return j
		nums[i],nums[j] = nums[j],nums[i]

def quick_sort(nums):
	def _quick_sort(items,low,high):
		if low < high:
			split_index = partition(items,low,high)
			_quick_sort(items,low,split_index)
			_quick_sort(items,split_index+1,high)

	_quick_sort(nums,0,len(nums)-1)
	return nums

#menu
def menu(pilihan):
	if pilihan==1:
		print()
		urutkan()
	elif pilihan==2:
		print()
		ekpor_csv()
		print('file berhasil diexport')
	else:
		print("Terima Kasih")
		exit()

#sub-menu
def urutkan():
	pilihan = int(input("urutkan berdasarkan:\n 1. Tahun\n 2. Negara Bagian\n 3. Bulan\n 4. Jumlah kebakaran\n pilihan anda:"))
	if pilihan == 1:
		quick_sort(df['year'])
		print(df)
	elif pilihan == 2: 
		quick_sort(df['state'])
		print(df)
	elif pilihan ==3: 
		quick_sort(df['month'])
		print(df)
	elif pilihan == 4:
		quick_sort(df['number'])
		print(df)

def ekpor_csv():
	pilihan = int(input("eksport berdasarkan:\n 1. Tahun\n 2. Negara Bagian\n 3. Bulan\n 4. Jumlah kebakaran\n pilihan anda:"))
	if pilihan == 1:
		quick_sort(df['year'])
		df.to_csv('sorted_by_year.csv',index=False, encoding='latin1')
	elif pilihan == 2:
		quick_sort(df['state'])
		df.to_csv('sorted_by_state.csv',index=False, encoding='latin1')
	elif pilihan == 3:
		quick_sort(df['month'])
		df.to_csv('sorted_by_month.csv',index=False, encoding='latin1')
	elif pilihan == 4:
		quick_sort(df['number'])
		df.to_csv('sorted_by_number.csv', index=False, encoding='latin1')

#MAIN PROGRAM
if __name__ == '__main__':

	#import data
	df = pd.read_csv('brazil-forest.csv',encoding='latin1')

	while True:
		print("\n\tTugas akhir Algoritma dan Struktur Data")
		print(" Menu\n 1. Urutkan\n 2. Eksport ke csv\n 3. Keluar")

		pilihan = int(input("pilihan anda: "))
		menu(pilihan)