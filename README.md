# gsheets 
is a small wrapper around the Google Sheets API (v4) to provide more convenient access to Google Sheets from Python scripts.

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


