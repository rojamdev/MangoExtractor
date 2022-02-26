import xml.etree.ElementTree as etree
import json, argparse, re, os

class Activity:
    """Used for holding activity elements as Python objects from the XML tree, which are either messages
    or the comments within the messages."""
    def __init__(self, element, is_comment):

        self.contents = {
            "id": None,
            "author-email-address": None,
            "body": None,
            "created-on": None,
            "project-id": 0
        }

        # This loop checks each element's name against the list of tags and sets the corresponding variable
        # to the data in the tag
        for subelem in element:  # For every element in the tree
            for key, value in self.contents.items():  # Iterates list for the number of items in the self.tags list

                if subelem.tag == key:  # If the tag matches one of the tags in the self.tags list

                    if subelem.text.isnumeric() and subelem.tag != "body":
                        self.contents[key] = int(subelem.text)

                    else:
                        self.contents[key] = subelem.text  # then set it to the respective variable
            
            # Creates a new element in the dictionary for the activity object
            # to define whether it is a comment or not
            if is_comment: 
                self.contents["is_comment"] = True
            else:
                self.contents["is_comment"] = False


def file_read(input_file, output_file):
    """Reads the raw XML file and outputs a far cleaner copy
    with only the necessary information."""

    # Opens the xml file and stores it as a string, removing all newlines
    with open(input_file, "r", encoding="utf8") as input_file:
        data = input_file.read().replace('\n', '')

    # Finds all elements named <activity> in the string and stores it in an array
    activities = re.findall("<activity>[\s\S]*?<\/activity>", data)

    # Writes each <activity> element to a file
    with open(output_file, "w", encoding="utf8") as output_file:
        output_file.write("<root>\n")

        for i in range(0, len(activities) - 1):
            output_file.write(activities[i])
            output_file.write("\n")

        output_file.write("</root>")

        # <root> tags are placed at the bottom and top of the file
        # This is to make parsing as an xml work


def create_activities_array(tree):
    """Creates an array of activity objects with a sub-array of 
    activities within each message for the comments."""
    activities = []

    for item in tree.findall("activity"):  # for every item named activity
        message = Activity(item, False)  # create a new message object from that activity

        comments = []
        for thing in item.findall("comments"):

            for i in thing.findall("comment"): # do the same for comments within that activity
                comment = Activity(i, True)
                comments.append(comment.contents)

        message.contents["comments"] = comments
        activities.append(message.contents)

    return activities


def get_project_ids(tree):
    """Searches for every 'project-id' element in the provided XML 
    tree and adds it to a list if not already in the list."""
    project_ids = []

    for item in tree.findall("activity"):
        message = Activity(item, False)

        if message.contents["project-id"] not in project_ids:
            project_ids.append(message.contents["project-id"])

    return project_ids


def create_message_json(array, filename):
    """Dumps the array of message objects into a JSON file."""
    output_file = open(filename, "w", encoding="utf8")
    json.dump(array, output_file, indent=4)
    output_file.close()


def create_ids_json(array, filename):
    """Dumps the array of 'project-id' values into a JSON file."""
    project_id_dict = {}

    for i in range(0, len(array) - 1):
        project_id_dict["key" + str(i)] = array[i]

    output_file = open(filename, "w", encoding="utf8")
    json.dump(project_id_dict, output_file, indent=4)
    output_file.close()


if __name__ == "__main__":
    # File names
    OUTPUT_XML_NAME = "output.xml"
    MSG_JSON_NAME =  "messages.json"
    IDS_JSON_NAME = "projectids.json"
    
    # Parses the filename argument from running this file
    # in command line
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "filename",
        type=str,
        help="the name of the .xml file containing the messages"
        )

    args = parser.parse_args()
    input_xml = args.filename

    # Taking the raw XML file and converting it into another
    # much cleaner XML file
    try:
        file_read(input_xml, OUTPUT_XML_NAME)
    except FileNotFoundError:
        print("File '" + str(input_xml) + "' not found.")
        exit()

    xml_tree = etree.parse(OUTPUT_XML_NAME)
    root = xml_tree.getroot()

    # Creates the arrays of message objects and 'project-id' values
    message_array = create_activities_array(root)
    project_id_array = get_project_ids(root)

    # Dumps the message array and 'project-id' array into two separate JSON files
    create_message_json(message_array, MSG_JSON_NAME)
    create_ids_json(project_id_array, IDS_JSON_NAME)
