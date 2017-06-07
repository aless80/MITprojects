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

This is the printed output: 

`
0 Hal Abelson has 0 abstract(s) 

1 Elfar Adalsteinsson has 2 abstract(s) 

2 Anant Agarwal has 0 abstract(s) 

3 Akintunde Akinwande has 0 abstract(s) 

4 Mohammad Alizadeh has 5 abstract(s) 

5 Saman Amarasinghe has 1 abstract(s) 

6 Dimitri Antoniadis has 1 abstract(s)

8 Arthur Baggeroer has 0 abstract(s)

9 Hari Balakrishnan has 4 abstract(s)

10 Marc A. Baldo has 1 abstract(s)

11 Regina Barzilay has 20 abstract(s)

12 Bonnie A. Berger has 0 abstract(s)

13 Karl Berggren has 25 abstract(s)

14 Tim Berners-Lee has 1 abstract(s)

15 Dimitri Bertsekas has 11 abstract(s)

16 Robert Berwick has 1 abstract(s)

17 Sangeeta Bhatia has 2 abstract(s)

18 Duane Boning has 1 abstract(s)

19 Louis Braida has 0 abstract(s)

20 Guy Bresler has 16 abstract(s)

21 Tamara Broderick has 25 abstract(s)

22 Rodney Brooks has 0 abstract(s)

23 Vladimir Bulovic has 2 abstract(s)

24 Michael Carbin has 1 abstract(s)

25 Vincent Chan has 2 abstract(s)

26 Anantha Chandrakasan has 2 abstract(s)

27 Adam Chlipala has 3 abstract(s)

28 Isaac Chuang has 25 abstract(s)

29 David Clark has 14 abstract(s)

30 Fernando Corbató cannot form a search string. Do accents work in search engine?

31 Munther Dahleh has 25 abstract(s)

32 Luca Daniel has 10 abstract(s)

33 Konstantinos Daskalakis has 4 abstract(s)

34 Randall Davis has 2 abstract(s)

35 Jesús del Alamo cannot form a search string. Do accents work in search engine?

36 Erik Demaine has 25 abstract(s)

37 Jack Dennis has 0 abstract(s)

38 Srini Devadas has 0 abstract(s)

39 Fredo Durand has 4 abstract(s)

40 Joel Emer has 3 abstract(s)

41 Tony Eng has 0 abstract(s)

42 Dirk R. Englund has 15 abstract(s)

43 Clifton Fonstad has 0 abstract(s)

44 David Forney has 0 abstract(s)

45 William Freeman has 25 abstract(s)

46 Dennis Freeman has 0 abstract(s)

47 James Fujimoto has 1 abstract(s)

48 Robert Gallager has 1 abstract(s)

49 David Gifford has 1 abstract(s)

50 Shafrira Goldwasser has 0 abstract(s)

51 Polina Golland has 5 abstract(s)

52 Martha Gray has 0 abstract(s)

53 Paul Gray has 0 abstract(s)

54 W. Eric L. Grimson has 0 abstract(s)

55 Alan Grodzinsky has 0 abstract(s)

56 John Guttag has 4 abstract(s)

57 Peter Hagelstein has 10 abstract(s)

58 Jongyoon Han has 0 abstract(s)

59 Ruonan Han has 0 abstract(s)

60 Thomas Heldt has 0 abstract(s)

61 Frederick Hennie III has 0 abstract(s)

62 Berthold Horn has 1 abstract(s)

63 Judy Hoyt has 2 abstract(s)

64 Qing Hu has 13 abstract(s)

65 Piotr Indyk has 24 abstract(s)

66 Erich Ippen has 1 abstract(s)

67 Tommi Jaakkola has 25 abstract(s)

68 Daniel Jackson has 3 abstract(s)

69 Patrick Jaillet has 25 abstract(s)

70 Stefanie Jegelka has 25 abstract(s)

71 M. Frans Kaashoek has 1 abstract(s)

72 Leslie Kaelbling has 23 abstract(s)

73 David Karger has 16 abstract(s)

74 John Kassakian has 0 abstract(s)

75 Dina Katabi has 4 abstract(s)

76 Manolis Kellis has 5 abstract(s)

77 James Kirtley, Jr. has 0 abstract(s)

78 Leslie Kolodziejski has 0 abstract(s)

79 Jing Kong has 25 abstract(s)

80 Butler Lampson has 1 abstract(s)

81 Jeffrey Lang has 1 abstract(s)

82 Hae-Seung Lee has 0 abstract(s)

83 Steven Leeb has 0 abstract(s)

84 Charles Leiserson has 1 abstract(s)

85 Jae Lim has 2 abstract(s)

86 Barbara Liskov has 0 abstract(s)

87 Luqiao Liu has 11 abstract(s)

88 Andrew Lo has 5 abstract(s)

89 Tomás Lozano-Pérez cannot form a search string. Do accents work in search engine?

90 Timothy Lu has 0 abstract(s)

91 Nancy Lynch has 20 abstract(s)

92 Samuel Madden has 18 abstract(s)

93 Aleksander Madry has 15 abstract(s)

94 Thomas Magnanti has 2 abstract(s)

95 Roger Mark has 0 abstract(s)

96 Wojciech Matusik has 3 abstract(s)

30 Muriel Médard cannot form a search string. Do accents work in search engine?

98 Alexandre Megretski has 17 abstract(s)

99 Albert Meyer has 0 abstract(s)

100 Silvio Micali has 8 abstract(s)

101 Rob Miller has 5 abstract(s)

102 Sanjoy Mitter has 19 abstract(s)

103 Robert Morris has 25 abstract(s)

104 Joel Moses has 0 abstract(s)

105 Stefanie Mueller has 0 abstract(s)

106 Alan Oppenheim has 3 abstract(s)

107 Terry Orlando has 12 abstract(s)

108 Asuman Ozdaglar has 25 abstract(s)

109 Tomás Palacios cannot form a search string. Do accents work in search engine?

110 Pablo Parrilo has 25 abstract(s)

111 William Peake has 0 abstract(s)

112 Li-Shiuan Peh has 0 abstract(s)

113 Paul Penfield, Jr. has 0 abstract(s)

114 David Perreault has 1 abstract(s)

115 Yury Polyanskiy has 25 abstract(s)

116 Rajeev Ram has 7 abstract(s)

117 L. Rafael Reif has 0 abstract(s)

118 Martin Rinard has 14 abstract(s)

119 Ronald Rivest has 9 abstract(s)

120 Ronitt Rubinfeld has 19 abstract(s)

121 Daniela Rus has 23 abstract(s)

122 Daniel Sanchez has 25 abstract(s)

123 Joel Schindall has 0 abstract(s)

124 Martin A. Schmidt has 1 abstract(s)

125 Devavrat Shah has 25 abstract(s)

126 Jeffrey Shapiro has 25 abstract(s)

127 Nir Shavit has 12 abstract(s)

128 Max Shulaker has 1 abstract(s)

129 Henry Smith has 1 abstract(s)

130 Charles Sodini has 0 abstract(s)

131 Armando Solar-Lezama has 16 abstract(s)

132 Justin Solomon has 6 abstract(s)

133 David Sontag has 25 abstract(s)

134 Michael Stonebraker has 5 abstract(s)

135 Collin Stultz has 1 abstract(s)

136 Gerald Sussman has 1 abstract(s)

137 Vivienne Sze has 6 abstract(s)

138 Peter Szolovits has 10 abstract(s)

139 Russell Tedrake has 0 abstract(s)

140 Christopher Terman has 0 abstract(s)

141 Bruce Tidor has 0 abstract(s)

142 Antonio Torralba has 25 abstract(s)

143 John Tsitsiklis has 25 abstract(s)

144 Caroline Uhler has 25 abstract(s)

145 Vinod Vaikuntanathan has 1 abstract(s)

146 George Verghese has 4 abstract(s)

147 Joel Voldman has 0 abstract(s)

148 Stephen Ward has 1 abstract(s)

149 Cardinal Warde has 0 abstract(s)

150 Michael Watts has 2 abstract(s)

151 Thomas F. Weiss has 1 abstract(s)

152 Ron Weiss has 7 abstract(s)

153 Jacob White has 24 abstract(s)

154 Virginia Williams has 19 abstract(s)

155 Ryan Williams has 20 abstract(s)

156 Alan Willsky has 25 abstract(s)

157 Gerald Wilson has 0 abstract(s)

158 Patrick Winston has 0 abstract(s)

159 Gregory Wornell has 25 abstract(s)

160 Markus Zahn has 0 abstract(s)

161 Nickolai Zeldovich has 1 abstract(s)

162 Lizhong Zheng has 19 abstract(s)

163 Victor Zue has 0 abstract(s)`


---

## Work in progress!

The script does the scraping and stores the abstract links for each faculty member in the MIT EECS faculty in the abs_dict dictionary.
