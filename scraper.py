# Auction scraper - looking for info from an auctions site to identify more into on govt sell offs of property to plug budget
# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
import scraperwiki
import lxml.html
#
# # Read in a page
html=scraperwiki.scrape("https://www.sdlauctions.co.uk/property-list/")
# Print the variable html containing the webpage
##commented out the print link so running the page doesn't take ages!
#print(html)
# # Find something on the page using css selectors
root=lxml.html.fromstring(html)
# inspecting the all the info in the <a tag within the <p> and <li> tags (P and LI are parents of A)
root.cssselect("li p a")
# then store the matched links in 'matchedlinks'
matchedlinks=root.cssselect("li p a")
##commented out the print link so running the page doesn't take ages!
# print(matchedlinks)
# create a dictionary called record
record = {}
# It's time to loop through the confusing codes from the page <Element a at 0x7f3fb1c536d8> calling each one li
# We're calling it li because it relates to the tag we've grabbed it from
for li in matchedlinks:
  #store the text elements of li in a new variable called 'listtext'
  listtext=li.text_content()
  # print that
  print(listtext)
  # store it in the 'record' dictionary under the key 'address'
  record["address"] = listtext
  # save the text that's been stored in the dictionary 'record' and save it to a table
  scraperwiki.sqlite.save(['address'],record)
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
