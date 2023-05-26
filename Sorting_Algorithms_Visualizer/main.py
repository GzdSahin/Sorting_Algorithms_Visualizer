import winsound
import time
from tkinter import *
from tkinter import ttk
import random
from sorting import Sortings
import matplotlib.pyplot as plt
from tkinter import messagebox

Sortings=Sortings()

root = Tk()
root.title('Sorting Algorithm Visualiser')
root.maxsize(900, 600)
root.config(bg='white')

#variables
selected_alg = StringVar()
data = []


#function
def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]),fill='purple')
    
    root.update_idletasks()


def Generate():
    global data

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal+1, maxVal+1))

    drawData(data, ['white' for x in range(len(data))]) #['red', 'red' ,....]

def StartAlgorithm():
    global data
    if not data: return

    if algMenu.get() == 'Quick Sort':
        timeTick = 0.1
        comparison_label = Label(root, text="Karşılaştırma Sayısı: 0")
        comparison_label.grid(row=1, column=0)
        comparison_count = Sortings.quick_sort(data, 0, len(data)-1, drawData , timeTick)
        comparison_label.config(text= "Karşılatırma Sayısı: {}".format(comparison_count))
    
    elif algMenu.get() == 'Bubble Sort':
        timeTick = 0.1
        comparison_label = Label(root, text="Karşılaştırma Sayısı: 0")
        comparison_label.grid(row=1, column=0)
        comparison_count = Sortings.bubble_sort(data, drawData , timeTick)
        comparison_label.config(text= "Karşılatırma Sayısı: {}".format(comparison_count))
        
    elif algMenu.get() == 'Selection Sort':
        timeTick = 0.1
        comparison_label = Label(root, text="Karşılaştırma Sayısı: 0")
        comparison_label.grid(row=1, column=0)
        comparison_count = Sortings.selection_sort(data, drawData , timeTick)
        comparison_label.config(text= "Karşılatırma Sayısı: {}".format(comparison_count))

    elif algMenu.get() == 'Merge Sort':
        timeTick = 0.1
        comparison_label = Label(root, text="Karşılaştırma Sayısı: 0")
        comparison_label.grid(row=1, column=0)
        comparison_count = Sortings.merge_sort(data, drawData , timeTick)
        comparison_label.config(text= "Karşılatırma Sayısı: {}".format(comparison_count))
    elif algMenu.get() == 'Insertion Sort':
        timeTick = 0.1
        comparison_label = Label(root, text="Karşılaştırma Sayısı: 0")
        comparison_label.grid(row=1, column=0)
        comparison_count = Sortings.insertion_sort(data, drawData , timeTick)
        comparison_label.config(text= "Karşılatırma Sayısı: {}".format(comparison_count))
    
    drawData(data, ['green' for x in range(len(data))])


#frame / base lauout
UI_frame = Frame(root, width= 700, height=300, bg='purple4')
UI_frame.grid(row=0, column=0, padx=0, pady=0)

canvas = Canvas(root, width=700, height=450, bg='white')
canvas.grid(row=0, column=1, padx=0, pady=0)

#User Interface Area
#Row[0] 

Label(UI_frame, text="Algorithm: ", bg='white',fg='white').grid(row=0, column=0, padx=5, pady=5, sticky=W) 

algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort','Selection Sort' ,'Quick Sort', 'Merge Sort', 'Insertion Sort']) 

algMenu.grid(row=0, column=0, padx=5, pady=5) 

algMenu.current(0) 

 
 

speedScale = Scale(UI_frame, from_=0.1, to=5.0, length=100, digits=2, resolution=0.2, orient=HORIZONTAL,bg='white', label="Select Speed [s]") 

speedScale.grid(row=1, column=0, padx=5, pady=5) 

Button(UI_frame, text="SÜTUN GRAFİĞİ", command=StartAlgorithm, bg='MediumPurple1').grid(row=6, column=0, padx=5, pady=5) 

 
 

#Row[1] 

sizeEntry = Scale(UI_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, bg='white',label="Data Size") 

sizeEntry.grid(row=2, column=0, padx=5, pady=5) 

 
 

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value",bg='white') 

minEntry.grid(row=3, column=0, padx=5, pady=5) 

 
 

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value",bg='white') 
maxEntry.grid(row=4, column=0, padx=5, pady=5) 


Button(UI_frame, text="Generate", command=Generate, bg='grey').grid(row=5, column=0, padx=5, pady=5) 

 

def bubble_sort_with_stem():

    global data
    n = len(data)
    colors = ['skyblue'] * n  # Tüm elemanlar başlangıçta skyblue renkli
    swapped = True

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title('Bubble Sort')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')

    while swapped:
        swapped = False

        for i in range(n - 1):
            colors[i] = 'yellow'  # Karşılaştırma başladığında elemanı yellow renge çevir

            # Grafiği güncelleyerek göster
            ax.clear()
            ax.stem(range(n), data, linefmt='skyblue', markerfmt='skyblue', basefmt='skyblue')
            ax.stem(i, data[i], linefmt='yellow', markerfmt='yellow', basefmt='yellow')
            ax.stem(i + 1, data[i + 1], linefmt='yellow', markerfmt='yellow', basefmt='yellow')
            plt.pause(2)

            # Karşılaştırmayı gerçekleştir
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True

                colors[i] = 'red'  # Swap yapıldığında elemanı red renge çevir

                # Grafiği güncelleyerek göster
                ax.clear()
                ax.stem(range(n), data, linefmt='skyblue', markerfmt='skyblue', basefmt='skyblue')
                ax.stem(i, data[i], linefmt='red', markerfmt='red', basefmt='red')
                ax.stem(i + 1, data[i + 1], linefmt='red', markerfmt='red', basefmt='red')
                plt.pause(2)

            colors[i] = 'skyblue'  # Karşılaştırma tamamlandığında elemanı tekrar skyblue renge çevir

    colors[:] = ['green'] * n  # Sıralama tamamlandığında elemanları green renge çevir

    # Grafiği son haliyle göster
    ax.clear()
    ax.stem(range(n), data, linefmt='skyblue', markerfmt='green', basefmt='green')
    plt.pause(2)  # Son hali için 2 saniye beklet

    plt.show()
def selection_sort_with_stem():

    global data
    n = len(data)
    colors = ['skyblue'] * n  # Tüm elemanlar başlangıçta skyblue renkli

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title('Selection Sort')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')

    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            colors[j] = 'orange'  # Karşılaştırma başladığında elemanı orange renge çevir

            # Grafiği güncelleyerek göster
            ax.clear()
            ax.stem(range(n), data, linefmt='skyblue', markerfmt='skyblue', basefmt='skyblue')
            ax.stem(i, data[i], linefmt='green', markerfmt='green', basefmt='green')
            ax.stem(j, data[j], linefmt='orange', markerfmt='orange', basefmt='orange')
            plt.pause(2)

            if data[j] < data[min_idx]:
                min_idx = j

            colors[j] = 'skyblue'  # Karşılaştırma tamamlandığında elemanı tekrar skyblue renge çevir

        data[i], data[min_idx] = data[min_idx], data[i]

        # Grafiği güncelleyerek göster
        ax.clear()
        ax.stem(range(n), data, linefmt='skyblue', markerfmt='skyblue', basefmt='skyblue')
        ax.stem(i, data[i], linefmt='red', markerfmt='red', basefmt='red')
        ax.stem(min_idx, data[min_idx], linefmt='red', markerfmt='red', basefmt='red')
        plt.pause(2)

    colors[:] = ['green'] * n  # Sıralama tamamlandığında elemanları green renge çevir

    # Grafiği son haliyle göster
    ax.clear()
    ax.stem(range(n), data, linefmt='skyblue', markerfmt='green', basefmt='green')
    plt.pause(2)  # Son hali için 2 saniye beklet

    plt.show()

def quicksort_stem():
    # Quick Sort algoritması
    global data
    def quicksort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            quicksort(arr, low, pivot_index - 1)
            quicksort(arr, pivot_index + 1, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    fig, ax = plt.subplots()
    plt.ion()  # Interaktif modu etkinleştir

    ax.stem(data)
    ax.set_title('Sıralanmamış Veri')
    ax.set_xlabel('Indeks')
    ax.set_ylabel('Değer')
    plt.show()

    sorted_data = data.copy()  # Sıralanmış veriyi güncellemek için kopyalayalım

    low = 0
    high = len(sorted_data) - 1
    quicksort(sorted_data, low, high)  # Veriyi Quick Sort ile sırala

    for i in range(low, high + 1):
        ax.stem(sorted_data, linefmt='gray', markerfmt=' ')
        ax.set_title(f'Karşılaştırma: {sorted_data[i]} ve {sorted_data[high]}')

        if sorted_data[i] > sorted_data[high]:
            sorted_data[i], sorted_data[high] = sorted_data[high], sorted_data[i]

        ax.stem(i, sorted_data[i], linefmt='r', markerfmt='ro')
        ax.stem(high, sorted_data[high], linefmt='r', markerfmt='ro')
        plt.pause(0.5)

    ax.clear()  # Grafik alanını temizle

    # Sıralanmış veriyi yeşil renkte göster
    ax.stem(sorted_data, linefmt='g', markerfmt='g')
    ax.set_title('Sıralanmış Veri')
    ax.set_xlabel('Indeks')
    ax.set_ylabel('Değer')
    plt.pause(1.5)  # Son durumu biraz daha uzun süre göstermek için bekle
    plt.ioff()  # Interaktif modu kapat
    plt.show()

def merge_sort_stem():
    # Merge Sort algoritması
    global data
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)

        return merge(left_half, right_half)

    def merge(left, right):
        merged = []
        left_index = right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        merged.extend(left[left_index:])
        merged.extend(right[right_index:])

        return merged

    fig, ax = plt.subplots()
    plt.ion()  # Interaktif modu etkinleştir

    ax.stem(data)
    ax.set_title('Sıralanmamış Veri')
    ax.set_xlabel('Indeks')
    ax.set_ylabel('Değer')
    plt.show()

    sorted_data = merge_sort(data)  # Veriyi Merge Sort ile sırala

    for i in range(len(sorted_data)):
        ax.stem(sorted_data, linefmt='gray', markerfmt=' ')
        ax.set_title(f'Karşılaştırma: {sorted_data[i]}')
        ax.stem(i, sorted_data[i], linefmt='r', markerfmt='ro')
        plt.pause(0.5)

    ax.clear()  # Grafik alanını temizle

    # Sıralanmış veriyi yeşil renkte göster
    ax.stem(sorted_data, linefmt='g', markerfmt='g')
    ax.set_title('Sıralanmış Veri')
    ax.set_xlabel('Indeks')
    ax.set_ylabel('Değer')
    plt.pause(1.5)  # Son durumu biraz daha uzun süre göstermek için bekle
    plt.ioff()  # Interaktif modu kapat
    plt.show()
def insertion_sort_stem():
    global data
    # Insertion Sort algoritması
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    fig, ax = plt.subplots()
    plt.ion()  # Interaktif modu etkinleştir

    ax.stem(data)
    ax.set_title('Sıralanmamış Veri')
    ax.set_xlabel('Indeks')
    ax.set_ylabel('Değer')
    plt.show()

    sorted_data = insertion_sort(data)  # Veriyi Insertion Sort ile sırala

    for i in range(len(sorted_data)):
        ax.stem(sorted_data, linefmt='gray', markerfmt=' ')
        ax.set_title(f'Ekleme: {sorted_data[i]}')
        ax.stem(i, sorted_data[i], linefmt='r', markerfmt='ro')
        plt.pause(0.5)

    ax.clear()  # Grafik alanını temizle

    # Sıralanmış veriyi yeşil renkte göster
    ax.stem(sorted_data, linefmt='g', markerfmt='g')
    ax.set_title('Sıralanmış Veri')
    ax.set_xlabel('Indeks')
    ax.set_ylabel('Değer')
    plt.pause(1.5)  # Son durumu biraz daha uzun süre göstermek için bekle
    plt.ioff()  # Interaktif modu kapat
    plt.show()

    
def bubble_sort_with_scatter():
    global data
    n = len(data)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title('Bubble Sort')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')

    for i in range(n-1):
        for j in range(n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

            # Tüm elemanları skyblue renkli olarak çiz
            ax.clear()
            ax.scatter(range(n), data, color='skyblue')

            # Karşılaştırılan elemanları kırmızı renkte çiz
            ax.scatter(j, data[j], color='red')
            ax.scatter(j+1, data[j+1], color='red')

            plt.pause(0.1)  # 0.1 saniye bekle

    # Tüm elemanları yeşil renkte çiz
    ax.clear()
    ax.scatter(range(n), data, color='green')
    plt.show()

def selection_sort_with_scatter():
    global data
    n = len(data)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title('Selection Sort')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')

    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if data[j] < data[min_index]:
                min_index = j

        data[i], data[min_index] = data[min_index], data[i]

        # Tüm elemanları pembe renkte çiz
        ax.clear()
        ax.scatter(range(n), data, color='pink')

        # Minimum elemanı ve yer değiştiren elemanı turuncu renkte çiz
        ax.scatter(i, data[i], color='orange')
        ax.scatter(min_index, data[min_index], color='orange')

        plt.pause(0.1)  # 0.1 saniye bekle

    # Tüm elemanları yeşil renkte çiz
    ax.clear()
    ax.scatter(range(n), data, color='green')
    plt.show()

def quicksort_scatter():
    global data
    # Quick Sort algoritması
    def quicksort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            quicksort(arr, low, pivot_index - 1)
            quicksort(arr, pivot_index + 1, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    fig, ax = plt.subplots()
    plt.ion()  # Interaktif modu etkinleştir

    x = list(range(len(data)))
    y = data

    ax.scatter(x, y, c='b')
    ax.set_title('Sıralanmamış Veri')
    ax.set_xlabel('Indeks')
    ax.set_ylabel('Değer')
    plt.show()

    sorted_data = data.copy()  # Sıralanmış veriyi güncellemek için kopyalayalım

    low = 0
    high = len(sorted_data) - 1
    quicksort(sorted_data, low, high)  # Veriyi Quick Sort ile sırala

    for i in range(low, high + 1):
        ax.clear()  # Grafik alanını temizle

        ax.scatter(x, sorted_data, c='b')
        ax.set_title(f'Karşılaştırma: {sorted_data[i]} ve {sorted_data[high]}')
        ax.scatter(i, sorted_data[i], c='r')
        ax.scatter(high, sorted_data[high], c='r')
        plt.pause(0.5)

        if sorted_data[i] > sorted_data[high]:
            sorted_data[i], sorted_data[high] = sorted_data[high], sorted_data[i]

    ax.clear()  # Grafik alanını temizle

    # Sıralanmış veriyi yeşil renkte göster
    ax.scatter(x, sorted_data, c='g')
    ax.set_title('Sıralanmış Veri')
    ax.set_xlabel('Indeks')
    ax.set_ylabel('Değer')
    plt.pause(1.5)  # Son durumu biraz daha uzun süre göstermek için bekle
    plt.ioff()  # Interaktif modu kapat
    plt.show()
def merge_sort_scatter():
    global data
    # Merge Sort algoritması
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)

        return merge(left_half, right_half)

    def merge(left, right):
        merged = []
        left_index = right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        merged.extend(left[left_index:])
        merged.extend(right[right_index:])

        return merged

    fig, ax = plt.subplots()
    plt.ion()  # Interaktif modu etkinleştir

    x = list(range(len(data)))
    y = data

    ax.scatter(x, y, c='b')
    ax.set_title('Sıralanmamış Veri')
    ax.set_xlabel('Indeks')
    ax.set_ylabel('Değer')
    plt.show()

    sorted_data = merge_sort(data.copy())  # Sıralanmış veriyi güncellemek için kopyalayalım

    colors = ['r', 'g', 'c', 'm', 'y']  # Renklerin listesi

    def merge_sort_visualize_helper(arr, start, end, depth):
        if start >= end:
            return

        mid = (start + end) // 2
        merge_sort_visualize_helper(arr, start, mid, depth + 1)
        merge_sort_visualize_helper(arr, mid + 1, end, depth + 1)

        merged = merge(arr[start:mid + 1], arr[mid + 1:end + 1])

        ax.clear()  # Grafik alanını temizle
        ax.scatter(x, arr, c='b')

        color_index = depth % len(colors)  # Renklerin döngüsünü sağlamak için indeksi hesapla

        # Karşılaştırma adımlarını göster
        for i in range(start, end + 1):
            if i <= mid:
                ax.scatter(i, arr[i], c=colors[color_index])
            else:
                ax.scatter(i, arr[i], c=colors[color_index + 1])

        ax.set_title(f'Karşılaştırma: {arr[start:mid + 1]} ve {arr[mid + 1:end + 1]}')
        plt.pause(0.5)

        arr[start:end + 1] = merged

    merge_sort_visualize_helper(sorted_data, 0, len(sorted_data) - 1, 0)

    ax.clear()  # Grafik alanını temizle

    # Sıralanmış veriyi yeşil renkte göster
    ax.scatter(x, sorted_data, c='g')
    ax.set_title('Sıralanmış Veri')
    ax.set_xlabel('Indeks')
    ax.set_ylabel('Değer')
    plt.pause(1.5)  # Son durumu biraz daha uz
def insertion_sort_scatter():
    global data
    # Insertion Sort algoritması
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    fig, ax = plt.subplots()
    plt.ion()  # Interaktif modu etkinleştir

    x = list(range(len(data)))
    y = data

    ax.scatter(x, y, c='b')
    ax.set_title('Sıralanmamış Veri')
    ax.set_xlabel('Indeks')
    ax.set_ylabel('Değer')
    plt.show()

    sorted_data = data.copy()  # Sıralanmış veriyi güncellemek için kopyalayalım

    for i in range(1, len(sorted_data)):
        key = sorted_data[i]
        j = i - 1

        ax.clear()  # Grafik alanını temizle
        ax.scatter(x, sorted_data, c='b')

        while j >= 0 and sorted_data[j] > key:
            sorted_data[j + 1] = sorted_data[j]

            # Karşılaştırma adımlarını göster
            ax.scatter(j, sorted_data[j], c='r')
            ax.scatter(j + 1, sorted_data[j + 1], c='g')
            plt.pause(0.5)

            j -= 1

        sorted_data[j + 1] = key

    ax.clear()  # Grafik alanını temizle

    # Sıralanmış veriyi yeşil renkte göster
    ax.scatter(x, sorted_data, c='g')
    ax.set_title('Sıralanmış Veri')
    ax.set_xlabel('Indeks')
    ax.set_ylabel('Değer')
    plt.pause(1.5)  # Son durumu biraz daha uzun süre göstermek için bekle
    plt.ioff()  # Interaktif modu kapat
    plt.show()

def StartAlgorithm2():



    global data
    if not data: return

    if algMenu.get() == 'Bubble Sort':
         bubble_sort_with_stem()
    elif algMenu.get() == 'Selection Sort':
        selection_sort_with_stem()
    elif algMenu.get() == 'Quick Sort':
        quicksort_stem()
    elif algMenu.get() == 'Merge Sort':
        merge_sort_stem()
    elif algMenu.get() == 'Insertion Sort': 
        insertion_sort_stem()   

    
        
def StartAlgorithm3():
    


    global data
    if not data: return

    if algMenu.get() == 'Bubble Sort':
         bubble_sort_with_scatter()
    elif algMenu.get() == 'Selection Sort':
        selection_sort_with_scatter()
    elif algMenu.get() == 'Quick Sort':
        quicksort_scatter()
    elif algMenu.get() == 'Merge Sort':
        merge_sort_scatter()
    elif algMenu.get() == 'Insertion Sort':
        insertion_sort_scatter()



Button(UI_frame, text="KÖK GRAFİĞİ", command=StartAlgorithm2, bg='MediumPurple1').grid(row=9, column=0, padx=5, pady=5) 

Button(UI_frame, text="KÖK GRAFİĞİ", command=StartAlgorithm2, bg='MediumPurple1').grid(row=9, column=0, padx=5, pady=5) 
Button(UI_frame, text="DAĞILIM GRAFİĞİ", comman=StartAlgorithm3, bg='MediumPurple1').grid(row=11, column=0, padx=8, pady=5) 







root.mainloop() 

 

