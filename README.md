# MangoExtractor
Two scripts to extract the messages from a large XML document, recieved from MangoApps after a company requested their message history.

## Requirements
- Python 3.9.5 or later (earlier versions not tested, other versions of Python 3 will likely work)

## Usage
- Clone the repository, or download the two python files and place them in a folder
- Place the XML file from MangoApps into the folder
- Run file-read.py
- Run mango-extractor.py

This should have created a messages.json and a projectids.json, which can then be used in MangoViewer.
