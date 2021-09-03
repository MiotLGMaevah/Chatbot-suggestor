#finalproject  #suggestionbasedonweather 
#get * form tkinter
from tkinter import *
box= Tk()
#tk color to green
box.configure(background='green')

#welcome

print("Welcome to Event suggestor!")

#userinput
e=Entry(box, width=100)

#send loop 
def send():
    send="User: "+e.get()
    txt.insert(END,"\n"+send)
#hello with list
    if (e.get()=='hello'):
       txt.insert(END,"\n"+"SUG: What's the weather like today? (Sunny, Cloudy,Rainy,Snowy,Windy) ")
       e.delete(0,END)
#sugestions start
    if (e.get()=='sunny'):
       txt.insert(END,"\n"+"SUG: Let's go to the Beach! Don't forget your bathing suit,sunscreen and to  hydrate.")
       e.delete(0,END)
    elif (e.get()=='rainy'):
        txt.insert(END,"\n"+"SUG: You should... Spend time inside watching a movie and relaxing!")
        e.delete(0,END)
    elif (e.get()=='windy'):
        txt.insert(END,"\n"+"SUG: You should... Make and fly a kite!")
        e.delete(0,END)  
    elif (e.get()=='snowy'):
        txt.insert(END,"\n"+"SUG: You should... Go sledding and make a snowman!")
        e.delete(0,END)  
    elif (e.get()=='cloudy'):
        txt.insert(END,"\n"+"SUG: You should... Have a Picnic at the park!")
        e.delete(0,END)  
     
      
#Tkinter box 
txt= Text(box)
txt.grid(row=0,column=0)
#send button for user
SB= Button(box,text="Send", command=send)
SB.grid(row=1,column=1)
e.grid(row=1,column=0)
#title of box
box.title("Day Planner")
#end
box.mainloop()



