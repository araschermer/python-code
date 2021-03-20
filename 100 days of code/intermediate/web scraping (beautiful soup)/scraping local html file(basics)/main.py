from bs4 import BeautifulSoup

with open("Cristiano Ronaldo - Wikipedia.html", encoding = "utf-8")as cr7:
    content = cr7.read()
# #
soup = BeautifulSoup(content, "html.parser")
# to obtain the text only
print(soup.text)
# to write the text into a file:
with open("article_content.txt", "w", encoding = "utf-8") as f:
    f.write(soup.text)
# to find how many time the name "cristiano ronaldo" appears in the text:
with open("article_content.txt", "r", encoding = "utf-8") as f:
    text_content = f.read()
#
Cristiano_Ronaldo = text_content.count("Cristiano Ronaldo")
# to find how many time each word appears:
words = text_content.split()
word_counts = {word: 0 for word in words}
#
for w in words:
    word_counts[w] += 1
print(word_counts)
# ranking the 10 most appearing words in the text
sorted_rankings = sorted(word_counts.items(), key = lambda item: item[1], reverse = True)[:10]
print(sorted_rankings)

# to get the html file content with indentation
print(soup.prettify())  # printing file content with indentation
# to get the article's title
# Look in the children of this PageElement and find the first pageElement that matches the given criteria
headings = soup.find("title")
print(headings)

# to get all the anchor_tags in the article
anchor_tags = soup.find_all(name = "a")
print(anchor_tags)

# to get the text that is attached to links

for tag in anchor_tags:
    print(tag.getText())
# getting only the links
for tag in anchor_tags:
    print(tag.get("href"))
# to save each link with the text attached to it in a  .txt file
with open("links.txt", 'w', encoding = "utf-8") as file:
    for tag in anchor_tags:
        file.write(f"{tag.getText()}: {tag.get('href')}\n")
# to select an element inside another element:
url = soup.select_one(selector = "p a")  # gets the first url insider a paragraph
print(url)
