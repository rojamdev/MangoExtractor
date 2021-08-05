import xml.etree.ElementTree as etree
from tkinter import *

WIN = Tk()
WIN.geometry("800x500")

tree = etree.parse("example.xml")
root = tree.getroot()

class Activity:
    
    def __init__(self, element):

        self.contents = {
            "id": None, 
            "body": None, 
            "author-email-address": None, 
            "created-on": None,
            "updated-at": None
        }
        
        for subelem in element: #for every element in the tree
            #this loop checks each element's name against the list of tags and sets the corresponding variable to the data in the tag
            for key, value in self.contents.items(): #iterates list for the number of items in the self.tags list
                if subelem.tag == key: #if the tag matches one of the tags in the self.tags list
                    self.contents[key] = subelem.text #then set it to the respective variable

    def display(self):
        self.email_label = Label(WIN, text=self.contents["author-email-address"])
        self.body_label = Label(WIN, text=self.contents["body"])
        self.date_label = Label(WIN, text=self.contents["created-on"])

        labels = [self.email_label, self.body_label, self.date_label]

        for label in labels:
            label.pack()

# message = Activity(root)
# message.display()

# for key, value in message.contents.items():
#     try:
#         print(key + ": " + value)
#     except TypeError:
#         print("No value")

for item in root.findall("activity"): #for every item named activity
    message = Activity(item) #create a new message object from that activity
    message.display() #display the message object using tkinter

    for thing in item.findall("comments"):
        print(thing.tag)

        for i in thing.findall("comment"):
            print(i.tag)
            comment = Activity(i)
            comment.display()

WIN.mainloop()