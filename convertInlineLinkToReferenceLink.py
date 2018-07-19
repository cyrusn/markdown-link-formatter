#!/usr/local/bin/python3

import sys
import re
from math import log, floor

query = sys.argv[1]

# query = """
# - [Riverbank | Software | PyQt | What is PyQt?](https://riverbankcomputing.com/software/pyqt/intro)
# - [![image](https://www.riverbankcomputing.com/@@/resources/logo.png)](https://riverbankcomputing.com/software/pyqt/intro)
# """


def convertInlineLinkToReferenceLink(content):

    MARKDOWN_LINK_PATTERN = r"\[\!\[([^\[]+?)\]\(([^\#].+?)\)\]\(([^\#].+?)\)|\[([^\[]+?)\]\(([^\#].+?)\)"

    archors = []

    index = 0

    mdlinks = re.finditer(MARKDOWN_LINK_PATTERN, content)
    lst = list(mdlinks)
    size = len(lst)

    for i, link in enumerate(lst):
        index += 1
        pad = int(floor(log(max(size, 1), 10))) + 1

        if link.group(1):
            formattedArchorImageString = "[@{:0{pad}d}-img]: {}".format(
                index, link.group(2), pad=pad)
            formattedArchorLinkString = "[@{:0{pad}d}-url]: {}".format(
                index, link.group(3), pad=pad)

            archors.append(formattedArchorImageString)
            archors.append(formattedArchorLinkString)

            formattedString = "[![{}][@{:0{pad}d}-img]][@{:0{pad}d}-url]".format(
                link.group(1), index, index, pad=pad)

        else:
            formattedArchorString = "[@{:0{pad}d}]: {}".format(
                index, link.group(5), pad=pad)
            archors.append(formattedArchorString)

            formattedString = "[{}][@{:0{pad}d}]".format(
                link.group(4), index, pad=pad)

        content = content.replace(link.group(0), formattedString)

    content += "\n<!-- reference links -->\n\n"
    for a in archors:
        content += a + "\n"

    return content

result = convertInlineLinkToReferenceLink(query)

print(result, end='')
