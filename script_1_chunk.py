import PhotoScan
import math

doc = PhotoScan.app.document
path = PhotoScan.app.getSaveFileName()
doc.save(path)


chunk1 = doc.chunks[0]


### Photo Alignement ###
chunk1.matchPhotos(PhotoScan.HighAccuracy)
chunk1.alignCameras()

doc.save()

### DenseCloud ###
chunk1.buildDenseCloud(PhotoScan.MediumQuality, PhotoScan.AggressiveFiltering)

doc.save()

### Mesh ###
#chunk1.buildModel(PhotoScan.Arbitrary, face_count=PhotoScan.MediumFaceCount)

#doc.save()

### Texture ###
#chunk1.buildUV(PhotoScan.GenericMapping, 2)
#chunk1.buildTexture(PhotoScan.MosaicBlending, False, 8192, True)

#doc.save()

### DEM ###
#chunk1.buildDem(PhotoScan.DenseCloudData)

#doc.save()

### Orthomosaic ###
#chunk1.buildOrthomosaic(PhotoScan.ElevationData, PhotoScan.MosaicBlending)

#doc.save()

