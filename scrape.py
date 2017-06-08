def main():
    #Scrape those profs
    url_MITEECSfaculty = "https://www.eecs.mit.edu/people/faculty-advisors"
    from bs4 import *
    import urllib2
    handle=urllib2.urlopen(url_MITEECSfaculty);
    html_text=handle.read();
    soup=BeautifulSoup(html_text);
    people_div=soup.find_all("div", class_="people-list")[0];
    #Print all the names
    divs=people_div.find_all("div", class_="views-field views-field-title")
    names=list()
    for div in divs:
        nameholder = div.span.a
        if nameholder is None: #for example, Tony Eng does not have a link
            nameholder = div.span
        names.append(nameholder.contents[0])

    #Search papers in arXiv for each person in arxiv.org/find/all/1/au:+(lastname)_(initial)/0/1/0/all/0/1
    abs_dict=dict()
    for i,name in enumerate(names):
        split = name.rsplit(None,1)
        if len(split) == 0:
            print("Cannot find the first and last name for " + name)
            continue
        elif len(split) == 1:
            #Weird that one guy is just called "Arvind". 
            #He has a couple of papers but how to get them with the search string?
            lastname = split[0]
            firstname = ""
            continue
        else:        
            lastname = split[1].replace("-","_") #for Tim Berners-Lee
            firstname = split[0].replace("-","_")
        search_str = 'https://arxiv.org:443/find/all/1/au:+'+lastname+'_'+firstname+'/0/1/0/all/0/1'
        try:
            papers_text=urllib2.urlopen(search_str).read();
        except:
            print(str(i) + ' ' + name + ' cannot form a search string. Do accents work in search engine?')
            continue    
        soup_papers=BeautifulSoup(papers_text);
        #Use the arXiv code to go to the abstract, for example: https://arxiv.org/abs/1705.09655
        spans = soup_papers.find_all("span", class_="list-identifier")
        print(str(i) + " " + name + " has " + str(len(spans)) + " abstract(s)")
        abs_url_list=list()
        for span in spans:
            abs_url='https://arxiv.org/'+span.a["href"]        
            abs_url_list.append(abs_url)
            #You can continue by looking in each abstract with e.g.:
            #abs_text=urllib2.urlopen(search_str).read();
            #soup_abs=BeautifulSoup(abs_text);
            #or maybe save abstracts to disk
        #Here I just store the abstract url in a dictionary
        abs_dict[name]=abs_url_list

if __name__ == '__main__':
    main()
