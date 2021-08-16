import re

with open("testing.xml", "r") as file:
    data = file.read().replace('\n', '')

#print(data)

start = re.escape("<activity>")
end = re.escape("</activity>")

activity = re.search('%s(.*)%s' % (start, end), data).group(0)

print(activity)