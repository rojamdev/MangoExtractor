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
            "project-id": 0
        }
        
        for subelem in element: #for every element in the tree
            #this loop checks each element's name against the list of tags and sets the corresponding variable to the data in the tag
            for key, value in self.contents.items(): #iterates list for the number of items in the self.tags list
                
                if subelem.tag == key: #if the tag matches one of the tags in the self.tags list
                    
                    if subelem.text.isnumeric() and subelem.tag != "body":
                        self.contents[key] = int(subelem.text)
                    
                    else:
                        self.contents[key] = subelem.text #then set it to the respective variable


def create_message_json(array, filename):

    output_file = open(filename, "a+", encoding="utf8")
    json.dump(array, output_file, indent = 4)
    output_file.close()
        

def create_activities_array(tree):
    
    activities = []

    for item in tree.findall("activity"): #for every item named activity
        message = Activity(item, False) #create a new message object from that activity

        for thing in item.findall("comments"):
            comments = []

            for i in thing.findall("comment"):
                comment = Activity(i, True)
                comments.append(comment.contents)
                #activities.append(comment.contents)

        message.contents["comments"] = comments
        activities.append(message.contents)    

    return activities
    

def get_project_ids(tree):
    
    project_ids = []

    for item in tree.findall("activity"):
        message = Activity(item, False)
        
        if message.contents["project-id"] not in project_ids:
            project_ids.append(message.contents["project-id"])

    return project_ids


def create_ids_json(array, filename):
    project_id_dict = {}

    for i in range(0, len(array)-1):
        project_id_dict["key" + str(i)] = array[i]

    output_file = open(filename, "a+", encoding="utf8")
    json.dump(project_id_dict, output_file, indent = 4)
    output_file.close()


#message_array = create_activities_array(root)
#create_message_json(message_array, "messages.json")

project_id_array = get_project_ids(root)
create_ids_json(project_id_array, "projectids.json")