import random, os, sys, tkinter as tk


def main():
    if( not os.path.exists("m-94wheels.txt")):
        print("please install m-94wheels.txt")
        sys.exit()

    t = ""

    with open('m-94wheels.txt', "r") as m:
        t = m.read()
    
    t = t.split()

    #Start Gui
    labels = []


    def plus(data):
        name = data[0]
        number = data[1]
        cipher = data[2]

        i = cipher.index(name["text"])
        i += 1
        if(i > 25):
            i = 0
        name["text"] = cipher[i]
        
        
    
    def minus(data):
        name = data[0]
        number = data[1]
        cipher = data[2]

        i = cipher.index(name["text"])
        i -= 1
        if(i < 0):
            i = 25
        name["text"] = cipher[i]
    
    def addAll():
        for i in labels:
            plus(i)

    def minusAll():
        for i in labels:
            minus(i)


    window = tk.Tk()
    

    window.rowconfigure([0,1,2], minsize=25, weight=1)
    window.columnconfigure([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24, 25], minsize=25, weight=1)

    Addallbtn = tk.Button(master=window, text="add all" , command=addAll, height=1,)
    Addallbtn.grid(row=2, column=26, sticky="nsew")

    Minusallbtn = tk.Button(master=window, text="Minus all" , command=minusAll, height=1,)
    Minusallbtn.grid(row=1, column=26, sticky="nsew")

    for i in range(25):
        locals()['f%dbtnMinus' , (i)] = tk.Button(master=window, text="-" ,command=lambda: minus(labels[i]), height=1)
        locals()['f%dbtnMinus' , (i)].grid(row=0, column=i, sticky="nsew")

        locals()['f%dlbl' , (i)] = tk.Label(master= window, text= t[i][0], height=1, background= "red")
        locals()['f%dlbl' , (i)].grid(row=1, column=i, sticky="nsew")
        labels.append(([locals()['f%dlbl' , (i)], i, t[i]]))

        locals()['f%dplus' , (i)] = tk.Button(master=window, text="+" , command=lambda: plus(labels[i]), height=1)
        locals()['f%dplus' , (i)].grid(row=2, column=i, sticky="nsew")

    

    

    

    window.mainloop()
    

if (__name__ == "__main__"):
    main()
