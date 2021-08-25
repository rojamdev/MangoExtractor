import re

#Opens the xml file and stores it as a string, removing all newlines
with open("hub_network_data.xml", "r", encoding="utf8") as input_file:
    data = input_file.read().replace('\n', '')
    
#Finds all elements named <activity> in the string and stores it in an array
activities = re.findall("<activity>[\s\S]*?<\/activity>", data)

#Writes each <activity> element to a file
with open("output", "a+", encoding="utf8") as output_file:

    output_file.write("<root>\n")

    for i in range(0, len(activities) - 1):

        output_file.write(activities[i])
        output_file.write("\n")

    output_file.write("</root>")

    #<root> tags are placed at the bottom and top of the file
    #This is to make parsing as an xml work