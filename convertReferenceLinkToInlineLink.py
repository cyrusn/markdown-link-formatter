#!/usr/local/bin/python3
import re
from math import log, floor


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


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Markdown Link converter')
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-r', '--reference',
        help='convert reference link to inline link',
        action="store_true"
    )
    group.add_argument(
        '-i', '--inline',
        help='convert inline link to reference link',
        action='store_true'
    )
    parser.add_argument('content', help="Markdown content")
    args = parser.parse_args()

    if args.reference:
        result = convertReferenceLinkToInlineLink(args.content)
    elif args.inline:
        result = convertInlineLinkToReferenceLink(args.content)
    print(result, end='')
