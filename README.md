# doc-tracking-payload

### Tracking Document Payloads
This is a really basic PoC for tracking whether a unique user has opened an email attachment. Arguably, you cannot really be 100% the correct user has accessed the attachment vs. another user or potentially a sandbox with this method. If there are more novel ways of doing this without macros, I'd be excited to hear them.

This currently functions by embedding a tracking pixel in the header of an Office document which points at an external resource. User correlation is possible because each time a document is generated, a new RID is assigned to it. There's nothing inherently malicious about the blank template so hopefully it won't be flagged by AV.

### Example Operation
```
./doc-tracking.py --lhost 192.168.1.9 --lport 1337 --cleanup
Host: 192.168.1.9
Port: 1337
RID: e2be995d43034f3f89a34a9433071f3c
Outputfile: Doc1-e2be995d43034f3f89a34a9433071f3c.docx
Waiting for file operations to finish...
./tmp-extract/ has been cleaned up
```
