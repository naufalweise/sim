from random import random


def get_jumlah_pelanggan():
    random_num = random()
    if random_num < 0.35:
        return 8
    if random_num < 0.65:
        return 10
    if random_num < 0.9:
        return 12
    else:
        return 14

def get_jumlah_donut():
    random_num = random()
    if random_num < 0.4:
        return 1
    if random_num < 0.7:
        return 2
    if random_num < 0.9:
        return 3
    return 4


P = 20 # jumlah donut yang diproduksi
# mensimulasikan jual/beli toko roti dalam sehari
def simulate_day(day_num):
    D = 0 # total jumlah donut yang dibeli
    n_pelanggan = get_jumlah_pelanggan() # jumlah pelanggan
    for i in range(n_pelanggan):
        donut_beli = get_jumlah_donut() # jumlah donut yg dibeli
        D += donut_beli
    S = max(P - D, 0)
    B = min(P, D)
    keuntungan = calc_keuntungan(B, S)
    return DailySales(day_num, n_pelanggan, D, P, S, keuntungan)

from functools import reduce
# simulasi dalam 5 hari
def simulate_week():
    sales_list = []
    for day in range(5):
        sales_info = simulate_day(day)
        sales_list.append(sales_info)
    
    return sales_list
    
    
N_simulation=10000
def simulate_multiple():
    print()
    print("="*60)
    print()
    print("Hasil Simulasi Berkali-kali")
    profit_all = 0
    for i in range(N_simulation):
        sales_in_week = simulate_week()
        profit_all += reduce(lambda acc, sales: acc + sales.keuntungan, sales_in_week, 0)
    print("Total simulation: ", N_simulation)
    print("Avg Weekly Profit:", profit_all / float( N_simulation))

# print daily sales table
def print_sales(sales_list):
    print(f"{'Day':<5} {'Customers':<10} {'Demand':<8} {'Produced':<10} {'Leftover':<10} {'Profit':<10}")
    print("-" * 60)
    profit = 0
    for sales in sales_list:
        profit += sales.keuntungan
        print(f"{sales.day_num:<5} {sales.n_pelanggan:<10} {sales.D:<8} {sales.P:<10} {sales.S:<10} {sales.keuntungan:<10}")
    print("Total Profit:", profit)


# mengkalkulasikan keuntungan, harga jual - harga produksi
def calc_keuntungan(B, S):
    return 25000 * B - 15000 * S


from dataclasses import dataclass
@dataclass
class DailySales:
   """kelas untuk menyimpan informasi hasil simulasi toko dalam sehari"""
   day_num : int
   n_pelanggan: int
   D: int # demand donut
   P: int # produksi donut
   S: int # sisa donut
   keuntungan: int 

print("Hasil simulasi 1x")
print()
print_sales(simulate_week())
simulate_multiple()