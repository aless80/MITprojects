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