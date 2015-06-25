__author__ = 'rui'


import json
import subprocess
import sys
import os.path

try:
    import vobject
except ImportError as e:
    subprocess.call("sudo apt-get install python-vobject", shell = True)


requiredVC = ['businessName']

def genVCardFromJson(infile, outfile):
    outf = open(outfile,'w')
    with open(infile,'r') as inf:
        comps = json.load(inf)
        for comp in comps:
            v = vobject.vCard()
            v.add('n')
            v.n.value = vobject.vcard.Name(family = " ".join(comp['businessName']))
            v.add('fn')
            v.fn.value =" ".join(comp["businessName"])
            for c in comp:
                if c not in requiredVC:
                    lst = comp[c]
                    if type(lst)==type([]):
                        for i in range(len(lst)):

                            if i ==0:
                                t = v.add(c)
                            else:
                                t=v.add(c+str(i))
                            t.value = "".join(comp[c][i])
                    else:
                        t=v.add(c)
                        t.value = "".join(comp[c])
            outf.write(v.serialize())

if __name__=='__main__':
    print "You are about to start scraping www.yellowpages.com and your file will be saved as a json file"
    infile = 'yp_test.json'
    if os.path.isfile(infile):
        subprocess.call(["rm",infile])
    subprocess.call('scrapy crawl YP  -o %s'%infile, shell = True)
    print "scraping is finished! Result json file is saved as yp_test.json"
    genVCard=raw_input("Continue to convert your json file to VCard format(y/n)?")
    if genVCard=='y':
        outfile = infile[:infile.rfind('.')]+'.vcf'
        print('Json file %s is going to be converted to %s'%(infile, outfile))
        genVCardFromJson(infile,outfile)
    else:
        sys.exit()





