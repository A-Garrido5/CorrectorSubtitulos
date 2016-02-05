import sys, os, string
import urllib.request
import zipfile
from subprocess import call
from optparse import OptionParser
from os import listdir
import os


apk_file=''
apk_folder=''
project_name=''
cwd=os.path.dirname(os.path.abspath(__file__))
home=os.path.dirname(os.path.realpath(sys.argv[0]))
outdir=os.path.dirname(os.path.realpath(sys.argv[1]))+"/"

def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        print("No existe")
    else:
    	print("Existe")

def main():

	usage = "usage: %prog action file [options]"
	parser = OptionParser(usage=usage)
	parser.add_option("-o", dest="outdir", default=cwd+"/")
	(options, args) = parser.parse_args()
      

	if len(args)==2:
		if args[0] == 'c':			

			project_name = os.path.splitext(os.path.basename(args[1]))[0]

			particion1 = os.path.splitext(os.path.abspath(args[1]))

			particion2 = os.path.split(os.path.abspath(particion1[0]))

			file_name = os.path.join(particion2[0],particion2[1]+'.srt')

			archivo=open(file_name,'r')

			lineas=archivo.readlines()

			reemplazo=open(file_name,'w')


			for line in lineas:

				if(line.find("<i>")!=-1):
					line=line.strip("<i>")

				if(line.find("</i>")!=-1):
					line=line.replace("</i>","")
				
				if(line.find("</b>")!=-1):
					line=line.replace("</b>","")

				if(line.find("<b>")!=-1):
					line=line.replace("<b>","")

				#print(line)
				reemplazo.write(line)
        
     
		print('Listo')




if __name__=="__main__":
  main()