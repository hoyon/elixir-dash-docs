from bs4 import BeautifulSoup
import glob

files = glob.glob('docs/*.html')


for file in files:
    with open(file, 'r+') as file:
        markup = file.read()
        soup = BeautifulSoup(markup, "html5lib")

        for tag in soup.select('.sidebar, .sidebar-button'):
            tag.decompose()

        head = soup.find("head")
        if head:
            style = soup.new_tag("style")
            style.string = ".content{padding-left: 0!important}.content-inner{max-width: auto}"
            head.append(style)

        file.seek(0)
        file.write(soup.prettify())
        file.truncate()
