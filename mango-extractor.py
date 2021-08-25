import xml.etree.ElementTree as etree
import json

tree = etree.parse("output") #parses the xml created from the file reader script
root = tree.getroot() #gets the most outward element in which all other elements are inside


class Activity:

    def __init__(self, element, is_comment):
    """Takes an activity xml element and creates a dictionary based off of it."""
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
                    #then set it to the respective variable

                    if subelem.text.isnumeric() and subelem.tag != "body":
                        #converts the element to an int data type if it's a number (unless it's the body element)
                        self.contents[key] = int(subelem.text) 
                    else: 
                        self.contents[key] = subelem.text 


def create_message_json(array, filename):
    """Dumps the list of message objects into a JSON file."""
    output_file = open(filename, "a+", encoding="utf8")
    json.dump(array, output_file, indent = 4)
    output_file.close()
        

def create_activities_array(tree):
    """Creates an array of activity (or message/comment) objects."""
    activities = [] #creates an array to store all the message objects

    for item in tree.findall("activity"): #for every element named activity
        message = Activity(item, False) #create a new message object from that activity

        for comment_list in item.findall("comments"): #finds the comments element
            comments = [] #creates an array to store the comment objects in belonging to the message

            for i in comment_list.findall("comment"): #finds the individual comment elements inside <comments>
                comment = Activity(i, True) 
                comments.append(comment.contents)

        message.contents["comments"] = comments #adds the comments as an item in the message object
        activities.append(message.contents) #appends the whole message to the message objects list

    return activities
    

def get_project_ids(tree):
    """Compiles a list of all the project-id elements in each message from the xml."""
    project_ids = []

    for item in tree.findall("activity"):
        message = Activity(item, False)
        
        if message.contents["project-id"] not in project_ids:
            project_ids.append(message.contents["project-id"])

    return project_ids


def create_ids_json(array, filename):
    """Creates a JSON file of all the project IDs against generic names that can be edited later."""
    project_id_dict = {} 

    for i in range(0, len(array)-1):
        project_id_dict["key" + str(i)] = array[i]

    output_file = open(filename, "a+", encoding="utf8")
    json.dump(project_id_dict, output_file, indent = 4)
    output_file.close()


message_array = create_activities_array(root)
create_message_json(message_array, "messages.json")

project_id_array = get_project_ids(root)
create_ids_json(project_id_array, "projectids.json")