import wsiprocess as wp

slidename="/mnt/beegfs/work/H2020DeciderFicarra/gbontempo/datasets/camelyon16/training/tumor/test_004.tif"
annotationname="/mnt/beegfs/work/H2020DeciderFicarra/gbontempo/datasets/camelyon16/testing/test_004.xml"


slide = wp.slide(slidename)
annotation = wp.annotation(annotationname)
annotation.make_masks(slide)
annotation.export_mask("CMU-1/masks", "Tumor")