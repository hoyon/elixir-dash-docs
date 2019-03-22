from bs4 import BeautifulSoup
from pathlib import Path
import glob

files = glob.glob('docs/*.html')

for filename in files:
    with open(filename, 'r+') as file:
        markup = file.read()
        soup = BeautifulSoup(markup, "html5lib")

        # Remove sidebar and scripts
        for tag in soup.select('.sidebar, .sidebar-button, script'):
            tag.decompose()

        # Inject custom styling
        head = soup.find("head")
        if head:
            style = soup.new_tag("style")
            style.string = ".content{padding-left: 0!important}.content-inner{max-width: auto}"
            head.append(style)
        
        stem = Path(filename).stem
        # names for functions
        for tag in soup.select("#functions .detail"):
            tag["data-name"] = stem + "." + tag["id"]

        # names for callbacks
        for tag in soup.select("#callbacks .detail"):
            tag["data-name"] = stem + "." + tag["id"][2:]

        # names for callbacks
        for tag in soup.select("#types .detail"):
            tag["data-name"] = stem + "." + tag["id"][2:]

        # mark module type
        if soup.body.has_attr("data-type"):
            t = soup.body["data-type"]
            title = soup.find("title")
            title["class"] = t
            title["data-mod"] = stem

        file.seek(0)
        file.write(soup.prettify())
        file.truncate()
