import xml.etree.ElementTree as etree

tree = etree.parse("output")
root = tree.getroot()

class Activity:
    
    def __init__(self, element):

        self.contents = {
            "id": None, 
            "body": None,
            "project-id": "none",
            "author-email-address": None,
            "created-on": None,
            "updated-at": None
        }
        
        for subelem in element: #for every element in the tree
            #this loop checks each element's name against the list of tags and sets the corresponding variable to the data in the tag
            for key, value in self.contents.items(): #iterates list for the number of items in the self.tags list
                if subelem.tag == key: #if the tag matches one of the tags in the self.tags list
                    self.contents[key] = subelem.text #then set it to the respective variable


file = open("messages.csv", "a+", encoding="utf8")


for item in root.findall("activity"): #for every item named activity
    message = Activity(item) #create a new message object from that activity
    message_text = "[MESSAGE]" + "," + message.contents["author-email-address"] + "," + message.contents["created-on"] + "," + message.contents["project-id"] + "," + message.contents["body"]
    file.write(message_text)
    file.write("\n")
    
    for thing in item.findall("comments"):

        for i in thing.findall("comment"):
            comment = Activity(i)
            comment_text = "[COMMENT]" + "," + comment.contents["author-email-address"] + "," + comment.contents["created-on"] + "," + comment.contents["body"]
            file.write(comment_text)
            file.write("\n")

    file.write("\n")


file.close()