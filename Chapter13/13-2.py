import re

data = """
[warning] 2015-07-05 13:52:14 asb.py[line:1] uid is not using up.
[info] 2015-07-30 15:54:03 asd.py[line:12] program start.
[debug] 2015-07-09 11:54:12 asd.py[line:12] generate uid 2354.
[warning] 2015-07-09 23:51:03 asd.py[line:12] uid is used up.
"""

splited = filter(lambda x: not x == '', re.split("\[warning\] ", data.replace('\n','')))
regex = '(?P<date>\d{4}(-\d{2}){2}) (?P<time>(\d{2}:?){3}) (?P<filename>[\w\.]*)\[line:(?P<line>\d*)\] (?P<info>[ \.\w]*)\[?'
r = re.compile(regex)
results = [r.search(part).groupdict() for part in splited]

with open("warning.txt",'w') as output:
    for result in results:
        output.write('Warning: "{4}"\n\tSender: {2}:{3}\n\tTime: {0} {1}\n\n'.format(result["date"], result["time"], result["filename"], result["line"], result["info"].rstrip('.')))
