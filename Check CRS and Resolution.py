# Check CRS and Resolution
for layer in QgsProject.instance().mapLayers().values():
    if layer.type() == QgsMapLayer.RasterLayer:
       print("\nLayer:", layer.name())
       print("CRS:", layer.crs().authid())
       print("Width:", layer.width())
       print("Height:", layer.height())
       print("Pixel size X:", layer.rasterUnitsPerPixelX())
       print("Pixel size Y:", layer.rasterUnitsPerPixelY())