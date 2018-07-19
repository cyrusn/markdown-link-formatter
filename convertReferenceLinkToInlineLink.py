#!/usr/local/bin/python3
import sys
import re

query = sys.argv[1]


def convertReferenceLinkToInlineLink(content):
    ARCHORS_PATTERN = r"\n\[(.+)\]\: (.+)"
    links = re.finditer(ARCHORS_PATTERN, content, re.MULTILINE)

    for i, l in enumerate(links):
        referenceLinkPattern = '\[(.+)\]\[{}\]'.format(l.group(1))
        pattern = re.compile(referenceLinkPattern)

        def replacer(obj):
            return "[{}]({})".format(obj.group(1), l.group(2))

        content = re.sub(pattern, replacer, content)
        content = l.re.sub('', content)

    content = content.replace("\n<!-- reference links -->\n\n", "")
    return content

result = convertReferenceLinkToInlineLink(query)

print(result, end='')
