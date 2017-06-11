def main(abs_dict):
    """scrape abstracts stored in the dictionary output from gather.py: 
    abs_dict=gather.main(stop=5)
    scrape.main(abs_dict)
    """
    from bs4 import BeautifulSoup
    import urllib2
    import os
    scraped_path="./scraped"
    if not os.path.exists(scraped_path):
        os.makedirs(scraped_path)       #mkdir if does not exist
    for prof, abs_list in abs_dict.items():
        if os.path.exists("./abstracts/"+prof+"_abs00.txt"):
            continue
        print("Processing %i abstracts for %s" % (len(abs_list), prof))
        for i,url in enumerate(abs_list):
            filename = "%s/%s_abs%02d.txt" % (scraped_path,prof,i)
            #Do not scrape abstracts again!
            if os.path.isfile(filename): continue
            #arxiv is blocking me, so you can try a different mirror like this:
            url=url.replace('https://arxiv.','http://es.arxiv.')
            try:
                h=urllib2.urlopen(url);
            except:
                print("  URL cannot be opened: %s" % url)
                break
            html_text=h.read();
            soup=BeautifulSoup(html_text, "html.parser");
            abstract=soup.find("blockquote", class_="abstract").text
            abstract=abstract.replace("Abstract: ","")
            title=soup.find("h1", class_="title").text
            try:
                f=open(filename,"w")
                #f.write(title)
                f.write(abstract)
                f.close()
                print("   stored in %s" % filename)
            except:
                print("   could not store in %s !" % filename)

def tokenize(path="./abstracts/",pathout="./tokens/"):
    """tokenize text from all files in path.
    return a counter of the tokens
    cnt=tokenize(path="./abstracts/")
    """
    from collections import Counter
    import nltk
    import os
    pathout="./tokens/"
    if not os.path.exists(pathout):
        os.makedirs(pathout)       #mkdir if does not exist
    filelist=os.listdir(path)
    for filename in filelist:
        f = open(path+filename, 'r')
        text = f.read()
        f.close()
        tokens = nltk.word_tokenize(text)
        counter=Counter(tokens)
        filename_counter = filename.replace(".txt","") + "_counter.txt"
        
        f = open(pathout+filename_counter, 'w')
        for el in counter.items():
            f.write('\n'+el[0]+'\t'+str(el[1]))
        f.close()

    

def saveCounterToFile(cnt):
    return