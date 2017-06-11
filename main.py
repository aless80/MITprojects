import os;  os.chdir("/home/amarin/Dropbox/Courses/MIT/1.2 LDA - Finding Themes in Project Description/MITprojects")
import gather
import scrape
abs_dict=gather.main(stop=3)
scrape.main(abs_dict)
#cnt=
