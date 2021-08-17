import re

with open("hub_network_data.xml", "r", encoding="utf8") as input_file:
    data = input_file.read().replace('\n', '')
    

activities = re.findall("<activity>[\s\S]*?<\/activity>", data)

with open("output", "a+", encoding="utf8") as output_file:

    for i in range(0, len(activities) - 1):

        output_file.write(activities[i])
        output_file.write("\n")