import bs4 as bs4

def add_refresh(html_path):
# load the file
    with open(html_path, "r", encoding="utf-8") as pre_edit:
        txt = pre_edit.read()
        soup = bs4.BeautifulSoup(txt, "html.parser")

    # create new link
    new_meta = soup.new_tag("meta")
    new_meta["http-equiv"] = "refresh"
    new_meta["content"] = "5"

    # insert it into the document
    soup.head.append(new_meta)

    # save the file again
    with open(html_path, "w", encoding="utf-8") as post_edit:
        post_edit.write(str(soup))

