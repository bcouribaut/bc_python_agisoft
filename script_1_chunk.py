import PhotoScan
import math

doc = PhotoScan.app.document
path = PhotoScan.app.getSaveFileName()
doc.save(path)


chunk1 = doc.chunks[0]


### Photo Alignement ###
chunk1.matchPhotos(accuracy = PhotoScan.MediumAccuracy, generic_preselection=True, reference_preselection=True, filter_mask=False, keypoint_limit=40000, tiepoint_limit=4000)
chunk1.alignCameras()

doc.save()

### DenseCloud ###
chunk1.buildDenseCloud(quality=PhotoScan.MediumQuality, filter=PhotoScan.AggressiveFiltering)

doc.save()

### Mesh ###
#chunk1.buildModel(surface=PhotoScan.Arbitrary, source=PhotoScan.DenseCloudData, face_count=PhotoScan.MediumFaceCount, interpolation=PhotoScan.EnabledInterpolation)
chunk1.buildModel(surface=PhotoScan.HeightField, source=PhotoScan.DenseCloudData, face_count=PhotoScan.MediumFaceCount, interpolation=PhotoScan.EnabledInterpolation)

#doc.save()

### Texture ###
#chunk1.buildUV(mapping=PhotoScan.GenericMapping, count=2)
#chunk1.buildTexture(blending=PhotoScan.MosaicBlending, color_correction=False, size=8192, fill_holes=True)

#doc.save()

### DEM ###
#chunk1.buildDem(source=PhotoScan.DenseCloudData, interpolation=PhotoScan.EnabledInterpolation)
chunk1.buildDem(source=PhotoScan.ModelData, interpolation=PhotoScan.EnabledInterpolation)

#doc.save()

### Orthomosaic ###
#chunk1.buildOrthomosaic(surface=PhotoScan.ElevationData, blending=PhotoScan.MosaicBlending, color_correction=False, fill_holes=True)

#doc.save()
