Have you ever wanted to know what your grades are, only to be foiled by the glory that is Moodle? Does it annoy you that the statistics Moodle provides make about as much sense as an objdump of /dev/random? 

If so, then this might be the repo for you! This python script will parse the html of the Grades page, and then print the useful bits in a comma-seperated format that can be coppied and pasted into a spreadsheet.

# Installation
There's not much to install... Just download the python file and run it! The only dependency is the BeautifulSoup4 library, which can be installed with `pip install BeautifulSoup4`

# Usage
First, navigate to the 'Grades' page in Moodle for the class you want to read. Save the page as an html file, then (from a terminal) run the python script like this:

```python3 ./gradeCalc.py path/to/htmlFile.html```
If everything went well, then you should get a whole bunch of comma/carriage return seperated values printed to the console. It should be pretty trivial to just copy and paste that into a spread sheet program and have it format correctly.

NOTE: Any assignments whose grade is listed in moodle as `-` are output as a 0.