import PhotoScan
import math

doc = PhotoScan.app.document
path = PhotoScan.app.getSaveFileName()
doc.save(path)


chunk1 = doc.chunks[0]
chunk2 = doc.chunks[1]

if chunk1.cameras[0].reference.location: #if geotagged photos are in chunk1
	chunk2.crs = chunk1.crs #same coordinate system for both chunks
	for i in range(len(chunk1.cameras)):
		chunk2.cameras[i].reference.location = chunk1.cameras[i].reference.location
		print(chunk1.cameras[i].reference.location, " ", chunk2.cameras[i].reference.location)

else: #if geotagged photos are in chunk2
	chunk1.crs = chunk2.crs
	for j in range(len(chunk1.cameras)):
		chunk1.cameras[j].reference.location = chunk2.cameras[j].reference.location
		print(chunk1.cameras[j].reference.location, " ", chunk2.cameras[j].reference.location)


doc.save()

"""

### Photo Alignement ###
for k in range(len(doc.chunks)):
	doc.chunks[k].matchPhotos(PhotoScan.HighAccuracy)
	doc.chunks[k].alignCameras()

doc.save()

### Merge Chunk ###
mergedchunk =

doc.save()

### DenseCloud ###
mergedchunk.buildDenseCloud(PhotoScan.MediumQuality, AggressiveFiltering)

doc.save()

### Mesh ###
mergedchunk.buildModel(PhotoScan.Arbitrary, face_count=PhotoScan.MediumFaceCount)

doc.save()

### Texture ###
mergedchunk.buildUV(PhotoScan.GenericMapping, 4)
mergedchunk.buildTexture(PhotoScan.MosaicBlending, False, 8192, True)

doc.save()

### DEM ###
mergedchunk.buildDem(PhotoScan.DenseCloudData)

doc.save()

### Orthomosaic ###
mergedchunk.buildOrthomosaic(PhotoScan.ElevationData, PhotoScan.MosaicBlending)

doc.save()

"""
