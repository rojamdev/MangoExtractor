import xml.etree.ElementTree as etree

tree = etree.parse("some activities.xml")
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


for item in root.findall("activity"): #for every item named activity
    message = Activity(item) #create a new message object from that activity
    print("MESSAGE: " + message.contents["body"])
    
    for thing in item.findall("comments"):

        for i in thing.findall("comment"):
            comment = Activity(i)
            print("COMMENT: " + comment.contents["body"])