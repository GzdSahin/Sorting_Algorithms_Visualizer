import winsound
import time
from tkinter import *
from tkinter import ttk
import random
from sorting import Sortings

Sortings=Sortings()

root = Tk()
<<<<<<< HEAD
=======
root.title('Sorting Algorithm')
>>>>>>> 4dd5d722bafdeb76961297217c7c249a0d279ca4
root.maxsize(900, 600)
root.config(bg='white')

#variables
selected_alg = StringVar()
data = []
#function
def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 300
    c_width = 300
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
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]),fill='white')
    
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
    
    elif algMenu.get() == 'Insertion Sort':
        Sortings.insertion_sort(data, drawData, speedScale.get())
    

    drawData(data, ['green' for x in range(len(data))])


#frame / base lauout
UI_frame = Frame(root, width= 700, height=300, bg='white')
UI_frame.grid(row=0, column=0, padx=0, pady=0)

canvas = Canvas(root, width=700, height=380, bg='white')
canvas.grid(row=0, column=1, padx=0, pady=0)

#User Interface Area
#Row[0]
Label(UI_frame, text="Algorithm: ", bg='white',fg='white').grid(row=0, column=0, padx=5, pady=5, sticky=W)
<<<<<<< HEAD
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort','Selection Sort' ,'Quick Sort', 'Merge Sort', 'Insertion Sort'])
=======
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort','Selection Sort' ,'Quick Sort', 'Merge Sort'])
>>>>>>> 4dd5d722bafdeb76961297217c7c249a0d279ca4
algMenu.grid(row=0, column=0, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.1, to=5.0, length=100, digits=2, resolution=0.2, orient=HORIZONTAL,bg='white', label="Select Speed [s]")
speedScale.grid(row=1, column=0, padx=5, pady=5)
Button(UI_frame, text="Start", command=StartAlgorithm, bg='green').grid(row=6, column=0, padx=5, pady=5)

#Row[1]
sizeEntry = Scale(UI_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, bg='white',label="Data Size")
sizeEntry.grid(row=2, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value",bg='white')
minEntry.grid(row=3, column=0, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value",bg='white')
maxEntry.grid(row=4, column=0, padx=5, pady=5)

Button(UI_frame, text="Generate", command=Generate, bg='grey').grid(row=5, column=0, padx=5, pady=5)

root.mainloop()

