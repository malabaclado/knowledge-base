---
tags: type/concept
alias: null
creation-date: Monday 1st August 2022
last-modified-date: Monday 1st August 2022 11:47:50
---

# Methods for Image Segmentation
![[Image Segmentation#^45d297]]

**Methods for image segmentation:** (See [Image segmentation - Wikipedia](https://en.wikipedia.org/wiki/Image_segmentation))

1. Thresholding
2. Clustering methods 
3. Motion and interactive segmentation 
4. Compression-based methods 
	- Compression based methods postulate that the optimal segmentation is the one that minimizes, over all possible segmentations, the coding length of the data.The connection between these two concepts is that segmentation tries to find patterns in an image and any regularity in the image can be used to compress it. The method describes each segment by its texture and boundary shape.
5. Histogram-based methods 
	- In this technique, a histogram is computed from all of the pixels in the image, and the peaks and valleys in the histogram are used to locate the clusters in the image. Color or intensity can be used as the measure.
	- A refinement of this technique is to recursively apply the histogram-seeking method to clusters in the image in order to divide them into smaller clusters. This operation is repeated with smaller and smaller clusters until no more clusters are formed.
6. Dual-clustering methods 
7. Region-growing methods 
8. Partial differential equation-based methods 
9. Variational methods
10. Graph-partitioning methods 