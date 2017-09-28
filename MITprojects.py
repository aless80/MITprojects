import os;  os.chdir(os.getenv("HOME")+"/Dropbox/Courses/MIT/1.2 LDA - Finding Themes in Project Description/MITprojects")
#import gather
#abs_dict=gather.main(stop=2)
import json
with open('abs_dict.json') as abs_dict_file:    #import json from file
    abs_dict = json.load(abs_dict_file)

import scrape
scrape.main(abs_dict)
scrape.tokenize()

#Now run lda. in onlineMIT I coded path to ../MITprojects/ etc
#This creates some .txt files
#os.chdir(os.getenv("HOME")+"/Dropbox/Courses/MIT/1.2 LDA - Finding Themes in Project Description/onlineldavb")
cd "/home/kinkyboy/Dropbox/Courses/MIT/1.2 LDA - Finding Themes in Project Description/onlineldavb"
python onlineMIT.py 101

python printtopics.py dictnostops.txt lambda-100.dat  #NaN


#TODO
#remove symbols from tokens
#check wikirandom for regular expressions: saxon genitives should be removed: "an agent's" in 'Leslie Kaelbling_abs20.txt'

#Notes
#python onlinewikipedia.py 101; python printtopics.py dictnostops.txt lambda-100.dat
#python printtopics.py dictnostops.txt lambda-10.dat
#https://wellecks.wordpress.com/2014/10/26/ldaoverflow-with-online-lda/

#(wordids, wordcts) = onlineldavb.parse_doc_list(docset, olda._vocab)
#printed output is in the return of do_e_step_docs  (gamma, sstats) = self.do_e_step_docs(docs)
#batchsize=64, docset is ['token token','token token',.. 64], articlenames=[..'Eddie_Noack', 64]. documentstoanalyze=51562

#python onlineMIT.py 101 
#python printtopics.py dictnostops.txt lambda-100.dat
import os;  os.chdir(os.getenv("HOME")+"/Dropbox/Courses/MIT/1.2 LDA - Finding Themes in Project Description/onlineldavb_101")
dictnostops.txt lambda-100.dat

Help on Case Study 1.2 - Finding Themes in Project Description
Hello,
Case study 1.2 - Finding Themes in Project Description: I did the scraping, I downloaded onlineldavb and modified the script so that it processes the abstracts of professors at MIT. 
My version now seems to run but I am not sure it is correct and most of all i do not know how to priint the results.
*) https://github.com/blei-lab/onlineldavb says that running



