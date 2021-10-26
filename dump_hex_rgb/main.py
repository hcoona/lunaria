#!/usr/bin/env python3

import json

def to_css_hex(rgb):
    return "#{0:02X}{1:02X}{2:02X}".format(
        *[ round(x * 255.) for x in rgb ]
    )

def camel_to_dashes(camel):
    dashes = list()
    for c in camel:
        if c.isupper():
            dashes.append("-")
            dashes.append(c.lower())
        else:
            dashes.append(c)
    return ''.join(dashes)

for (themename, themefile) in [("light", "../lunaria-light.json"), ("dark", "../lunaria-dark.json"), ("eclipse", "../lunaria-eclipse.json")]:
    theme = json.load(open(themefile))
    print("[" + themename + "]")
    for (k,v) in sorted(theme.items()):
        if k[0] == "_":
            continue
        print("{}={}".format(camel_to_dashes(k), to_css_hex(v)))
    print()
