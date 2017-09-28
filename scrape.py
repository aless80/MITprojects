def main(abs_dict):
	"""
    scrape.main(abs_dict)
    Scrape abstracts stored in the dictionary output from gather.py: 
	   abs_dict=gather.main(stop=5)
    Store the abstracts in ./abstracts/	
	"""
	from bs4 import BeautifulSoup
	import urllib2
	import os
	scraped_path="./scraped"
	if not os.path.exists(scraped_path):
		os.makedirs(scraped_path)	   #mkdir if does not exist
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
				saveTextToFile(abstract, filename)
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
	import string
	#Create the output path
	pathout="./tokens/"
	if not os.path.exists(pathout):
		os.makedirs(pathout)	   #mkdir if does not exist
	#read the files
	filelist=os.listdir(path)
	for filename in filelist:
		f = open(path+filename, 'r')
		text = f.read()
		f.close()
		#Substitute punctuation, remove non-alpha chars
		replace_punctuation = string.maketrans(string.punctuation, ' '*len(string.punctuation))
		text = text.translate(replace_punctuation)
		#Count tokens in text
		tokens = nltk.word_tokenize(text)
		counter=Counter(tokens)
		filename_counter = filename.replace(".txt","") + "_counter.txt"
		#Save the tokens of each abstract to a new file
		saveCounterToFile(counter, pathout+filename_counter)
		
def saveTextToFile(text, filename):
	f=open(filename,"w")
	f.write(text)
	f.close()

def saveCounterToFile(counter, filename):
	f = open(filename, 'w')
	for tup in counter.items():
		f.write(tup[0]+','+str(tup[1])+'\n')
	f.close()

def clean(doc):
        stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
        punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
        #normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
        normalized = " ".join(pstemmer.stem(word) for word in punc_free.split())
        return normalized

def readAbstracts(path="./abstracts/"):
    """
    abs_list = scrape.readAbstracts()
    Read the abstracts from the default ./abstracts/ folder.
    return a list with the abstract text in each element
    """
    import os
    from nltk.corpus import stopwords 
    from nltk.stem.porter import PorterStemmer
    #from nltk.stem.wordnet import WordNetLemmatizer
    import string
    abs_list = []
    stop = set(stopwords.words('english'))
    exclude = set(string.punctuation) 
    #lemma = WordNetLemmatizer()
    pstemmer = PorterStemmer()
    #read the files
    filelist=os.listdir(path)
    for filename in filelist:
        f = open(path+filename, 'r')
        abstract = f.read()
        f.close()
        abs_list.append(abstract)
    return abs_list



def readCleanAbstracts(path="./abstracts/"):
	"""
    abs_list = scrape.readAbstracts()
    Read the abstracts from the default ./abstracts/ folder. 
    Clean the text (remove stopwords, etc)
	return a list with the abstract text in each element
	"""
	import os
	from nltk.corpus import stopwords 
	from nltk.stem.porter import PorterStemmer
	#from nltk.stem.wordnet import WordNetLemmatizer
	import string
	abs_list = []
	stop = set(stopwords.words('english'))
	exclude = set(string.punctuation) 
	#lemma = WordNetLemmatizer()
	pstemmer = PorterStemmer()
	#read the files
	filelist=os.listdir(path)
	for filename in filelist:
		f = open(path+filename, 'r')
		abstract = f.read()
		f.close()
		absclean_list.append(clean(abstract).split())
	return absclean
