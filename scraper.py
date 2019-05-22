# pip install bs4
# pip install lxml
# pip install requests

from bs4 import BeautifulSoup
import requests

# Getting all html code using requests
all_html = requests.get("https://blog.acx.com/category/authors-publishers/").text


# Using BeautifulSoup with lxml parser
soup = BeautifulSoup(all_html, "lxml")

containers = soup.find_all("div", class_="status-publish")

all_title = []
all_posted = []
all_author = []
all_tags = []

for container in containers:
    title = container.h2.a.text
    title = title.replace(u'\xa0', u' ')
    posted = container.div.a.span.text
    posted = posted.replace(u'\xa0', u' ')
    author = container.find_all("span", class_="author vcard")[0].a.text
    author = author.replace(u'\xa0', u' ')

    try:
        all_links = container.find('p', class_="tag-links").find_all("a")
        helper = ""
        for link in all_links:
            helper = helper + " " + link.text
        all_tags.append(helper)
    except Exception:
        all_tags.append("Null")

    all_title.append(title)
    all_posted.append(posted)
    all_author.append(author)


# pip install xlwt
#Using Workbook function from xlwt to write lists of data into excel directly in one go!

from xlwt import Workbook
wb = Workbook()
sheet1 = wb.add_sheet("Sheet1")
sheet1.write(0,0, "Title")
sheet1.write(0,1,"Posted On")
sheet1.write(0,2,"Author")
sheet1.write(0,3,"Tags")

def writer(col, what_to_write):
    count = 1
    for i in what_to_write:
        sheet1.write(count, col, i)
        count += 1

writer(0, all_title)
writer(1, all_posted)
writer(2, all_author)
writer(3, all_tags)

wb.save("Blog Scraper.xls")


# Done ----> :)
