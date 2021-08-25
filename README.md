# MangoExtractor
Two scripts to extract the messages from a large XML document, recieved by a company from MangoApps after requesting their message history.

## Requirements
- Python 3.9.5 or later

## Usage
- Clone the repository, or download the two python files and place them in a folder
- Place the XML file named hub_network_data.xml into the folder
- Run file-read.py
- Run mango-extractor.py

This should have created a messages.json and a projectids.json, which can then be used in MangoViewer.
