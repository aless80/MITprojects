import os;  os.chdir("/home/amarin/Dropbox/Courses/MIT/1.2 LDA - Finding Themes in Project Description/MITprojects")
import os;  os.chdir("/home/kinkyboy/Dropbox/Courses/MIT/1.2 LDA - Finding Themes in Project Description/MITprojects")
#import gather
#abs_dict=gather.main(stop=2)
import json
with open('abs_dict.json') as abs_dict_file:    #import json from file
    abs_dict = json.load(abs_dict_file)

import scrape
scrape.main(abs_dict)

#I deleted last files from Isaac Chuang

"""
cannot pickle:
	if attr == 'string':
	RuntimeError: maximum recursion depth exceeded in cmp

mirror='https://arxiv.org:443' #'http://es.arXiv.org:443' 	#
search_str = mirror+'/find/all/1/au:+'+"Adalsteinsson"+'_'+"Elfar"+'/0/1/0/all/0/1'
h=urllib2.urlopen(search_str);
papers_text=h.read()
soup_papers=BeautifulSoup(papers_text, "html.parser");
#Use the arXiv code to go to the abstract, for example: https://arxiv.org/abs/1705.09655
spans = soup_papers.find_all("span", class_="list-identifier")
print(" has " + str(len(spans)) + " abstract(s)")
abs_url_list=list()
#for span in spans:
span=spans[0]
print('https://arxiv.org/'+span.a["href"])
span.a["href"]
span.a["href"].string
abs_url='https://arxiv.org/'+span.a["href"].string
"""


#for prof, abs_list in abs_dict.items():
prof, abs_list = abs_dict.items()[-1]:
if os.path.exists("./scraped/"+prof+"_abs00.txt"):
    continue
print("Processing %i abstracts for %s" % (len(abs_list), prof))
all_abstracts=unicode()
#for i,url in enumerate(abs_list):
url = abs_list[0]
i=0

url=url.replace('https://arxiv.','http://es.arxiv.')

"""try:
    h=urllib2.urlopen(url);
except:
    print("  URL cannot be opened: %s" % url)
    break
html_text=h.read();
soup=BeautifulSoup(html_text, "html.parser");
abstract=soup.find("blockquote", class_="abstract").text
abstract=abstract.replace("Abstract: ","")
title=soup.find("h1", class_="title").text"""
scraped_path="./scraped"
filename = "%s/%s_abs%02d.txt" % (scraped_path,prof,i)
#Do not scrape files again!
if os.path.isfile(filename): continue
try:
    f=open(filename,"w")
    #f.write(title)
    #f.write(abstract)
    f.write("testAle")
    f.close()
    print("   stored in %s" % filename)
except:
    print("   could not store in %s !" % filename)
print(filename)
return