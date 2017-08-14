import PhotoScan
import math

doc = PhotoScan.app.document
#path = PhotoScan.app.getSaveFileName()
#doc.save(path)


chunk1 = doc.chunks[0]

for i in range(3):
	chunk1.addMarker()

chunk1.loadReference("GCPs.csv", PhotoScan.ReferenceFormatCSV, delimiter=",")