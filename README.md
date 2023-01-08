# XML to CSV Parser
The XML to CSV Parser is a Python class that allows you to parse an XML file and write its data to a CSV file.

## Overview
The XML to CSV Parser consists of a single class, xmlParser, which contains the following methods:

- `__init__`: Initializes an instance of the xmlParser class and parses the XML file specified in the constructor.
- `createExcelFile`: Writes the data from the parsed XML file to a CSV file.
- `__readXML`: A private method for parsing the XML file.
- `sanitizeField`: A static method for cleaning up a string by removing leading and trailing white space and converting multiline string into single line.

## Usage
Import the `xmlParser` class in your Python code using the following statement:
```py
from xmltocsv import xmlParser
```

After importing, create an instance of the `xmlParser` class by calling it with the name of the XML file you want to parse and the name of the CSV file you want to write the results to

```py
parser = xmlParser("compiler.xml", "compiler.csv")
```

This will parse the `compiler.xml` file and write the results to the `compiler.csv` file.

The data in the CSV file will be organized with one row per book element in the XML file, and the columns will contain the values of specific elements or attributes within the book element.

## Explanation
### Class: `xmlParser`

#### Method: `__init__`

Initializes an instance of the `xmlParser` class and parses the XML file specified in the constructor.

##### Parameters

- `xmlFileName`: The name of the XML file to parse.
- `excelFileName`: The name of the CSV file to write the results to.

#### Method: `createExcelFile`

Writes the data from the parsed XML file to a CSV file.

##### Parameters

- `excelFileName`: The name of the CSV file to write the results to.

#### Method: `__readXML`

Private method for parsing the XML file.

#### Method: `sanitizeField`

Static method for cleaning up a string by removing leading and trailing white space and converting multiline string to single line.

##### Parameters

- `string`: The string to clean up.

##### Returns

A sanitized version of the input string.
