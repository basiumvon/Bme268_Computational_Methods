#Write a program to read through a file and print the contents of the file (line by line) all in upper case. Executing 
# the program will look as follows:

#python shout.py
#Enter a file name: mbox-short.txt
#FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008
#RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
#RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
#     BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
#     SAT, 05 JAN 2008 09:14:16 -0500

fout=open('ex.7.1.txt','w')
line1='python shout.py\n'
line2='Enter a file name: mbox-short.txt\n'
line3='FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008\n'
line4='RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>\n'
line5='RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])\n'
line6='     BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;\n'
line7='     SAT, 05 JAN 2008 09:14:16 -0500\n'
fout.write(line1.upper())
fout.write(line2.upper())
fout.write(line3.upper())
fout.write(line4.upper())
fout.write(line5.upper())
fout.write(line6.upper())
fout.write(line7.upper())

fout.close()