# gsheets is a small wrapper around the Google Sheets API (v4) to provide more convenient access to Google Sheets from Python scripts.

Turn on the API, download an OAuth client ID as JSON file, and create a Sheets object from it. Use its index access (__getitem__) to retrieve SpreadSheet objects by their id, or use .get() with a sheet URL. Iterate over the Sheets object for all spreadsheets, or fetch spreadsheets by title with the .find() and .findall() methods.

SpreadSheet objects are collections of WorkSheets, which provide access to the cell values via spreadsheet coordinates/slices (e.g. ws['A1']) and zero-based cell position (e.g. ws.at(0, 1)).

Save WorkSheets (or all from a SpreadSheet) as CSV files with the .to_csv()-method. Create pandas.DataFrames from worksheet with the .to_frame()-method.
Links
GitHub: https://github.com/xflr6/gsheets
PyPI: https://pypi.org/project/gsheets/
Documentation: https://gsheets.readthedocs.io
Changelog: https://gsheets.readthedocs.io/en/latest/changelog.html
Issue Tracker: https://github.com/xflr6/gsheets/issues
Download: https://pypi.org/project/gsheets/#files

Installation
This package runs under Python 2.7, and 3.6+, use pip_ to install:

.. code:: bash

$ pip install exceldrive2py
This will also install google-api-python-client_ and its dependencies, notably httplib2_ and oauth2client_, as required dependencies.

Quickstart
Log into the Google Developers Console_ with the Google account whose spreadsheets you want to access. Create (or select) a project and enable the Drive API and Sheets API (under Google Apps APIs).

Go to the Credentials for your project and create New credentials > OAuth client ID > of type Other. In the list of your OAuth 2.0 client IDs click Download JSON for the Client ID you just created. Save the file as client_secrets.json in your home directory (user directory).

import the library and load the data by passing the filename and json file downloaded from console it will return a dataframe and print top 5 rows of your data:

.. code:: python

>>> import exceldrive2py as rf

>>> dataframe = rf.load_data(filename_of_your_sheet,json_path)
For plotting the data you have to pass the dataframe you just loaded and pass the name X axis columns name and Y axis column name it will plot the data for you:

.. code:: python

for plotting
>>> rf.plot_data(dataframe,"x-axis-column","y-axis-column")
