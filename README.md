# MIT_projects
Python implementation of a case study in Module 1 in MITProfessionalX's course "Data Science: Data to insights". 

The case study is: "Module 1 - Making sense of unstructured data  Case Study". Case study is about doing our own analysis on MIT EECS
faculty data using stochastic variational inference on LDA. 

If you can access it, the description of the project is here:

[Self-Help Documentation](http://mitprofessionalx.mit.edu/asset-v1%3aMITProfessionalX+DSx+2017_T2+type@asset+block@Module1_CS2_LDA-analysis.pdf)

---

## Project description (copied from the Self-Help Documentation, section 1.)

Using BeautifulSoup (https://www.crummy.com/software/BeautifulSoup/), and by analyzing the structure of the source code of arXiv, we could scrape the name list of MIT EECS faculty members. Using this information, we could list the query we send to arXiv. A possible format for the arXiv search for papers by authors is the following:

arxiv.org/find/(subject)/1/au:+(lastname)_(initial)/0/1/0/all/0/1

You could therefore adapt the names you scraped, and query through all the relevant arXiv search
pages.

Within the arXiv source code, look for < class span=list-identifier >, which will give the identifier for the papers listed in your query results. Similarly look for the tag for the “Abstract” within each paper and scrape the abstract for each paper you find.

Note that you might want to scrape more information than you need and then do some local
processing with the text you have instead.

---

## Run the script
Clone the master branch and run it with e.g.:

`python scrape.py`

---

## Work in progress!

The script does the scraping and stores the abstract links for each faculty member in the MIT EECS faculty in the abs_dict dictionary.
