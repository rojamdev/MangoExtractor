import xml.etree.ElementTree as etree
import json

tree = etree.parse("output")
root = tree.getroot()

class Activity:
    
    def __init__(self, element, is_comment):

        self.contents = {
            "id": None,
            "author-email-address": None,
            "body": None,
            "created-on": None,
            "updated-at": None,
            "project-id": 0
        }
        
        for subelem in element: #for every element in the tree
            #this loop checks each element's name against the list of tags and sets the corresponding variable to the data in the tag
            for key, value in self.contents.items(): #iterates list for the number of items in the self.tags list
                
                if subelem.tag == key: #if the tag matches one of the tags in the self.tags list
                    
                    if subelem.text.isnumeric():
                        self.contents[key] = int(subelem.text)
                    
                    else:
                        self.contents[key] = subelem.text #then set it to the respective variable

        if is_comment:
            self.contents["is_comment"] = "true"
        else:
            self.contents["is_comment"] = "false"


def create_message_json(array, filename):

    output_file = open(filename, "a+", encoding="utf8")
    json.dump(array, output_file, indent = 4)
        

def create_activities_array(tree):
    
    activities = []

    for item in tree.findall("activity"): #for every item named activity
        message = Activity(item, False) #create a new message object from that activity
        activities.append(message.contents)

        for thing in item.findall("comments"):

            for i in thing.findall("comment"):
                comment = Activity(i, True)
                activities.append(comment.contents)

    return activities
    

def get_project_ids(tree):
    
    project_ids = []

    for item in tree.findall("activity"):
        message = Activity(item, False)
        
        if message.contents["project-id"] not in project_ids:
            project_ids.append(message.contents["project-id"])

    return project_ids


array = create_activities_array(root)

create_message_json(array, "messages.json")