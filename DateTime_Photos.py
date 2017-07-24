import PhotoScan
import math

doc = PhotoScan.app.document
chunk1 = doc.chunks[0]
#chunk2 = doc.chunks[1]


#for i in range(len(chunk1.cameras)):
#    print(chunk1.cameras[i], " ", chunk1.cameras[i].photo.meta["Exif/DateTime"], " ", chunk2.cameras[i].photo.meta["Exif/DateTime"])


#for j in range(5):
#    print(" ")


for k in range(len(chunk1.cameras)):
    print(chunk1.cameras[k], "  Alt :", chunk1.cameras[k].reference.location[2])
