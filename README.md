# MITprojects

Python implementation of a case study in Module 1 of the MITProfessionalX course "Data Science: Data to insights". 

The case study is: "Module 1 Case Study - Making sense of unstructured data". This case study is about doing our own analysis on MIT EECS faculty data using stochastic variational inference on LDA. 

If you can access it, the description of the project is here:

[Self-Help Documentation](http://mitprofessionalx.mit.edu/asset-v1%3aMITProfessionalX+DSx+2017_T2+type@asset+block@Module1_CS2_LDA-analysis.pdf)

---

## Project description (copied from the Self-Help Documentation, section 1.)

Using BeautifulSoup (https://www.crummy.com/software/BeautifulSoup/), and by analyzing the structure of the source code of arXiv, we could scrape the name list of MIT EECS faculty members. Using this information, we could list the query we send to arXiv. A possible format for the arXiv search for papers by authors is the following:

arxiv.org/find/(subject)/1/au:+(lastname)_(initial)/0/1/0/all/0/1

You could therefore adapt the names you scraped, and query through all the relevant arXiv search pages.

Within the arXiv source code, look for < class span=list-identifier >, which will give the identifier for the papers listed in your query results. Similarly look for the tag for the “Abstract” within each paper and scrape the abstract for each paper you find.

Note that you might want to scrape more information than you need and then do some local processing with the text you have instead.

---

## Run the script
Clone the master branch and run it in a python shell as:

```python
import gather
import scrape
abs_dict=gather.main()
scrape.main(abs_dict)
scrape.tokenize()
```

This is an example of the printed output for gather.main(), which stores the faculty members and the links of their abstracts in arXiv in a python dictionary. 

```python
import gather
abs_dict=gather.main()

0 Hal Abelson has 0 abstract(s)

1 Elfar Adalsteinsson has 2 abstract(s)

2 Anant Agarwal has 0 abstract(s)

3 Akintunde Akinwande has 0 abstract(s)

4 Mohammad Alizadeh has 5 abstract(s)

5 Saman Amarasinghe has 1 abstract(s)

6 Dimitri Antoniadis has 1 abstract(s)

...


30 Fernando Corbató cannot form a search string. Do accents work in search engine?

...

162 Lizhong Zheng has 19 abstract(s)

163 Victor Zue has 0 abstract(s)

```

I stored this dictionary in json format in the file abs_dict.json, which you can load directly as

```python
import json
with open('abs_dict.json') as abs_dict_file:    #import json from file
    abs_dict = json.load(abs_dict_file)

```

After that `scrape.main(abs_dict)` is called, which creates an `abstracts` directory with each scraped abstracts. Finally, `scrape.tokenize()` reads the locally stored abstracts and creates the `tokens` folder containing the tokens and their count. The `abstracts` and `tokens` folder are inclouded in this repo. 


---

## Work in progress! 
Topic Analysis using LDA can be found in the notebook: [https://github.com/aless80/MITprojects/blob/master/LDA.ipynb](LDA.ipynb)

---

## TODO
More plots