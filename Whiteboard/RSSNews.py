import requests
import xml.etree.ElementTree as ET
import csv

def loadRSS():
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    url = 'https://www.hindustantimes.com/feeds/rss/top-news/rssfeed.xml'

    resp = requests.get(url, headers=headers)

    #resp = requests.get(url)

    with open('topnewsfeed.xml', 'wb') as f:
        f.write(resp.content)

def parseXML(xmlfile):

    tree = ET.parse(xmlfile)

    root = tree.getroot()

    newsitems = []

    for item in root.findall('./channel/item'):
        news = {}

        for child in item:

            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')

        newsitems.append(news)

    return newsitems

def savetoCSV(newsitems, filename):

    fields = ['guid','title', 'pubDate', 'description','link','media']

    with open(filename, 'w') as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames = fields)

        writer.writeheader()

        writer.writerows(newsitems)

def main():
    loadRSS()

    newsitems = parseXML('topnewsfeed.xml')

    savetoCSV(newsitems, 'topnews.csv')

if __name__ == '__main__':
    main()