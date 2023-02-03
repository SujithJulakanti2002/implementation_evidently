import bs4 as bs4
import webbrowser
import app as app

# load the file
with open(app.name, "r", encoding="utf-8") as pre_edit:
    txt = pre_edit.read()
    soup = bs4.BeautifulSoup(txt, "html.parser")

# create new link
new_meta = soup.new_tag("meta")
new_meta["http-equiv"] = "refresh"
new_meta["content"] = "300"

# insert it into the document
soup.head.append(new_meta)

# save the file again
with open(app.name, "w", encoding="utf-8") as post_edit:
    post_edit.write(str(soup))

webbrowser.open(app.name)
