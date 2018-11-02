Sometimes we want to send documents to users and track if they actually open them without dropping malware.

I scripted up this tool to generate blank documents that can sent via Gmail, GoPhish, etc.

It works by "randomly" generating an unique ID for the document and storing it in a tracking pixel in the header of the docx file



Example Use:

First setup a webserver (I use pythom -m SimpleHTTPServer 1337 or whatever)

./doc-tracking.py --lhost 192.168.1.9 --lport 1337 --cleanup
Host: 192.168.1.9
Port: 1337
RID: e2be995d43034f3f89a34a9433071f3c
Outputfile: Doc1-e2be995d43034f3f89a34a9433071f3c.docx
Waiting for file operations to finish...
./tmp-extract/ has been cleaned up

>> The files are stored in the "output" directory.

Then you just need to facilitate delivery to a target and check your logs to see if the file was accessed.


::NOTES::
 You could create your own document by following these directions:
===> https://www.blackhillsinfosec.com/bugging-docx-files-using-microsoft-word-part-1/
--> Following the scheme I used, you should be able to get additional working templates that will be functional with the script.
--> Just use a URL like http://$LHOST:$LPORT/rid=$RID or something like that
There is also some room to use this to track the downloads of malicious docx files as well with the right template.
