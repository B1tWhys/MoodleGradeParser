from sys import argv
from bs4 import BeautifulSoup as bs
import re
from statistics import mean

def parseGrade(gradeStr):
    if (gradeStr == '-'):
        return 0.
    m = re.search(r"\d{1,3}\.\d{2}", gradeStr.strip())
    return float(m.group())

def parseRange(rangeStr):
    return float(rangeStr.strip().replace('–', '-').split('-')[1])

f = open(argv[1], 'r')
html = f.read()
f.close()

table = bs(html, "html.parser").find("table", class_=re.compile("user-grade"))
grades = table.find_all("td", headers=re.compile("grade"))
grades = [grade for grade in grades if 'total' not in grade.parent.text]

titles = [grade.find_previous_sibling("th").text for grade in grades]
grades = [parseGrade(grade.string) for grade in grades if 'total' not in grade.parent.text]

# print(titles)

ranges = table.find_all("td", headers=re.compile("range"))
maxScores = [parseRange(range_.string) for range_ in ranges if 'total' not in range_.parent.text] # range is a reserved word, hence range_


assert(len(grades) == len(maxScores))
weighted = [grade * maxScore for grade, maxScore in zip(grades, maxScores)]

mean = sum(grades)/sum(maxScores)
print(f"""avg: {mean}""")

# print(str([(title, g, m, g/m) for title, g, m in zip(titles, grades, maxScores)]).replace('), (', '\n')[2:-2])
# print({t: (g, m, g/m) for t, g, m in zip(titles, grades, maxScores)})
data = [(t, g, m, g/m) for t, g, m in zip(titles, grades, maxScores)]
print(str(data).replace("), (", "\n").replace("'", "")[2:-2])

