from bs4 import BeautifulSoup

import errno
import glob
import json
import re


def normalizeWhitespace(rawString):
    return re.sub(' +', ' ', rawString.replace('\n', ' ').strip())


def getMethodName(dom):
    methodNameResults = dom.find_all(class_="methodname")
    if len(methodNameResults) >= 1:
        rawMethodName = methodNameResults[0].text
        methodName = normalizeWhitespace(rawMethodName)
        return methodName
    return None


def getSynopsis(dom):
    synopsisResults = dom.find_all(class_="rdfs-comment")
    if len(synopsisResults) >= 1:
        rawSynopsis = synopsisResults[0].text
        synopsis = normalizeWhitespace(rawSynopsis)
        return synopsis
    return None


def getUsage(dom):
    usageResults = dom.find_all(class_="methodsynopsis")
    if len(usageResults) >= 1:
        rawUsage = usageResults[0].text
        usage = normalizeWhitespace(rawUsage)
        return usage


path = './php-chunked-xhtml/*.html'
files = glob.glob(path)

manEntries = []
resultsFile = open("man.json", "w")

for name in files:
    try:
        file = open(name)
        fileContents = file.read()
        if 'methodsynopsis' in fileContents:
            soup = BeautifulSoup(fileContents, "lxml")
            methodName = getMethodName(soup)
            synopsis = getSynopsis(soup)
            usage = getUsage(soup)
            manEntries.append({
                'name': methodName,
                'synopsis': synopsis,
                'usage': usage
            })

    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise


json.dump(manEntries, resultsFile)

resultsFile.close()
