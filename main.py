import os;  os.chdir("/home/amarin/Dropbox/Courses/MIT/1.2 LDA - Finding Themes in Project Description/MITprojects")
import os;  os.chdir("/home/kinkyboy/Dropbox/Courses/MIT/1.2 LDA - Finding Themes in Project Description/MITprojects")
#import gather
#abs_dict=gather.main(stop=2)
import json
with open('abs_dict.json') as abs_dict_file:    #import json from file
    abs_dict = json.load(abs_dict_file)

import scrape
scrape.main(abs_dict)
scrape.tokenize()


#TODO
#remove symbols from tokens


#Notes
#python onlinewikipedia.py 101; python printtopics.py dictnostops.txt lambda-100.dat
#python onlinewikipedia.py 2; python printtopics.py dictnostops.txt lambda-1.dat
#python printtopics.py dictnostops.txt lambda-10.dat
#https://wellecks.wordpress.com/2014/10/26/ldaoverflow-with-online-lda/

#str="ale @ is 0 2 (good) "
#re.findall(r'[^a-zA-Z0-9\s]',str)