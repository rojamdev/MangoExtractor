import xml.etree.ElementTree as etree

tree = etree.parse("output")
root = tree.getroot()

class Activity:
    
    def __init__(self, element):

        self.contents = {
            "id": None, 
            "body": None,
            "project-id": 0,
            "author-email-address": None,
            "created-on": None,
            "updated-at": None
        }
        
        for subelem in element: #for every element in the tree
            #this loop checks each element's name against the list of tags and sets the corresponding variable to the data in the tag
            for key, value in self.contents.items(): #iterates list for the number of items in the self.tags list
                if subelem.tag == key: #if the tag matches one of the tags in the self.tags list
                    self.contents[key] = subelem.text #then set it to the respective variable


def create_message_file(tree, filename):

    output_file = open(filename, "a+", encoding="utf8")


def create_activities_array(tree):
    
    activities = []

    for item in tree.findall("activity"): #for every item named activity
        message = Activity(item) #create a new message object from that activity
        message_contents = ["[MESSAGE]", message.contents["author-email-address"], message.contents["created-on"], message.contents["body"]]
        
        activities.append(message_contents)

        for thing in item.findall("comments"):

            for i in thing.findall("comment"):
                comment = Activity(i)
                comment_contents = ["[COMMENT]", comment.contents["author-email-address"], comment.contents["created-on"], comment.contents["body"]]

                activities.append(comment_contents)

    return activities
    

def get_project_ids(tree):
    
    project_ids = []

    for item in tree.findall("activity"):
        message = Activity(item)
        
        if message.contents["project-id"] not in project_ids:
            project_ids.append(message.contents["project-id"])

    return project_ids


print(get_project_ids(root))

array = create_activities_array(root)

for item in array:
    print(item)
    print()