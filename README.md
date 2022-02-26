# MangoExtractor
A Python script to extract the messages and comments from a large XML file sent by MangoApps upon requesting message history.

## Requirements
- Python 3.10.2 or later (earlier versions not tested, other versions of ```Python3``` will likely work)
- Ability to use ```Python3``` from the command line

## Setup
- Clone/download the repository
- Copy the XML file from MangoApps into the MangoExtractor folder you just cloned/downloaded

## Usage
Using the command line inside the MangoExtractor directory, run ```mango_extractor.py``` using
```
python3 mango_extractor.py <file_name>
```
where ```<file_name>``` is the name of the XML file from MangoApps you copied into the folder.

This should have created a messages.json and a projectids.json inside the MangoExtractor folder, which can then be used in [MangoViewer](https://github.com/rojamdev/MangoViewer).
