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
        Sortings.quick_sort(data, 0, len(data)-1, drawData, speedScale.get())
    
    elif algMenu.get() == 'Bubble Sort':
        Sortings.bubble_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Selection Sort':
        Sortings.selection_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Merge Sort':
        Sortings.merge_sort(data, drawData, speedScale.get())
    
    drawData(data, ['green' for x in range(len(data))])


#frame / base lauout
UI_frame = Frame(root, width= 700, height=300, bg='purple4')
UI_frame.grid(row=0, column=0, padx=0, pady=0)

canvas = Canvas(root, width=700, height=450, bg='white')
canvas.grid(row=0, column=1, padx=0, pady=0)

#User Interface Area
#Row[0] 

Label(UI_frame, text="Algorithm: ", bg='white',fg='white').grid(row=0, column=0, padx=5, pady=5, sticky=W) 

algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort','Selection Sort' ,'Quick Sort', 'Merge Sort']) 

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



def StartAlgorithm2():



    global data
    if not data: return

    if algMenu.get() == 'Bubble Sort':
         bubble_sort_with_stem()
    elif algMenu.get() == 'Selection Sort':
        selection_sort_with_stem()
    
        
def StartAlgorithm3():
    


    global data
    if not data: return

    if algMenu.get() == 'Bubble Sort':
         bubble_sort_with_scatter()
    elif algMenu.get() == 'Selection Sort':
        selection_sort_with_scatter()
Button(UI_frame, text="KÖK GRAFİĞİ", command=StartAlgorithm2, bg='MediumPurple1').grid(row=9, column=0, padx=5, pady=5) 

Button(UI_frame, text="DAĞILIM GRAFİĞİ", comman=StartAlgorithm3, bg='MediumPurple1').grid(row=11, column=0, padx=8, pady=5) 







 

root.mainloop() 

 

