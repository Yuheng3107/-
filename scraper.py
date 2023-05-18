import requests
from bs4 import BeautifulSoup

# Check that source does not end with html
# When it doesn't end with html, we have reached the end
def write_chapter_to_file(title, content):
    with open(name, "a") as f:
        f.write(title.text+"\n")
        for line in content:
            f.write(line.text+"\n")
base = "https://www.uukanshu.com"
source = "https://www.uukanshu.com/b/191026/130962.html"
name = "全民领主：我的亡灵会裂变"

while (source.endswith(".html")):
    response = requests.get(source)
    html_text = response.text
    soup = BeautifulSoup(html_text, "lxml")
    # Get title of chapter
    title = soup.find(id="timu")
    # Get content of chapter
    content = soup.find("div", id="contentbox").find_all("p")
    # Get link to next chapter
    source = base+soup.find(id="next")["href"]
    # Write contents of chapter to file
    write_chapter_to_file(title, content)
    