#!/usr/bin/env python3
import json
import re

import pathlib
path = pathlib.Path(__file__).parent.resolve()

# replace special characters in dialogue such as ^n
def repl(s: str) -> str:
    global replacements
    for r in replacements:
        s = re.sub(r[0], r[1], s)
    return s

# check if key matches any of the patterns to exclude from the deck
def is_excluded(k: str) -> bool:
    global exclude
    for e in exclude:
        if re.match(e, k):
            return True
    return False

# register special characters
replacements = []
with open(path / 'special.txt') as escapes:
    for line in escapes.readlines():
        things = line.strip('\n').split('|')
        if len(things) == 1:
            replacements.append((things[0], ''))
        else:
            replacements.append((things[0], things[1]))

# register excluded patterns
exclude = []
with open(path / 'exclude.txt') as excludes:
    for line in excludes.readlines():
        exclude.append(line.strip('\n'))

# already seen lines
seen = []

# sort_id counter
counter = 0

# convert, filter, and output cards
for line in json.load(open(path / 'lines.json')):
    key = line['key']
    en, jp = line['en'], line['jp']

    if is_excluded(key):
        continue

    enr, jpr = repl(en), repl(jp)
    enrs, jprs = enr.strip(), jpr.strip()

    if enrs == '' or jprs == '' or enrs == re.sub('＊', '*', jprs):
        continue

    enrss, jprss = re.sub('\s', '', enrs), re.sub('\s', '', jprs)

    if (enrss, jprss) in seen:
        continue

    seen.append((enrss, jprss))

    def respace(match: re.Match) -> str:
        return '&nbsp;' * (match.end() - match.start())

    enrsn = re.sub('  +', respace, enrs)

    jprsns, enrsns = '<span>'+jprs+'</span>', '<span>'+enrsn+'</span>'

    print(key, jprsns, enrsns, counter, sep='\t')
    counter += 1
