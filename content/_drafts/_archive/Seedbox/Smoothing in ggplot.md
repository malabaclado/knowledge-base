In this reading, you will learn about smoothing in ggplot2 and how it can be used to make your data visualizations in R clearer and easier to follow. Sometimes it can be hard to understand trends in your data from scatter plots alone. **Smoothing** enables the detection of a data trend even when you can't easily notice a trend from the plotted data points. Ggplot2’s smoothing functionality is helpful because it adds a **smoothing line** as another layer to a plot; the smoothing line helps the data to make sense to a casual observer.

|**Example code**|
|---|
|ggplot(data, aes(x=distance, y= dep_delay)) + geom_point() + geom_smooth()|

The example code creates a plot with a trend line similar to the blue line below.

![Screenshot of a scatterplot. There are points on the plot with a blue smoothing line indicating the upward trend of the poi](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/XbKKHOhhSEKyihzoYchC-A_368afc47eb8a4edcbb089c2684ce088f_e0a48bb6-bfad-4eda-96bf-c292a3beac48.png?expiry=1689120000000&hmac=hIr9atQpPTKfr-_yxSmBpnmd5Q-ZTT2jn3LKKg80f6U)

# Two types of smoothing

![Image of person painting over a rough, textured wall](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/iyRvuCCCSlKkb7gggtpSYw_d486c74c6d6d4f07bd189c920a9f7fbb_Screen-Shot-2021-03-10-at-10.48.47-PM.png?expiry=1689120000000&hmac=7cm9jxojDpzqKp4urrCm5R4vxZ-99rBOxrchuDYCJQY)

|**Type of smoothing**|**Description**|**Example code**|
|---|---|---|
|**Loess smoothing**|The loess smoothing process is best for smoothing plots with less than 1000 points.|ggplot(data, aes(x=, y=))+  geom_point() +       geom_smooth(method="loess")|
|**Gam smoothing**|Gam smoothing, or generalized additive model smoothing, is useful for smoothing plots with a large number of points.|ggplot(data, aes(x=, y=)) + geom_point() +         geom_smooth(method="gam", formula = y ~s(x))|

The smoothing functionality in ggplot2 helps make data plots more readable, so you are better able to recognize data trends and make key insights. The first plot below is the data before smoothing, and the second plot below is the same data after smoothing.

![screenshot of ggplot2 scatterplot. the x axis is weight from 2-5. The y axis is miles per gallon from 10-35.](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/wPPc24hXSWuz3NuIV0lrnQ_912eda8141a1490597aa1f78a57921c5_b6a22f66-9ecc-4452-aa73-79e0673d26f5.png?expiry=1689120000000&hmac=6qmhpr9pKXF6RqUsjvx6x8IOqx3S7zoIjj2QQJrSc9o)

![screenshot of ggplot2 scatterplot with smooth line. x axis is weight from 2-5. The y axis is miles per gallon from 10-35](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/f1AMePxESHyQDHj8RPh8OQ_100fd672112445729c7b0d534ec2ab82_755509aa-c74b-4eb0-a1ec-ff884e86b97f.png?expiry=1689120000000&hmac=nyJQvxwHqXI-At1I4_y0wyuxwX9MBad8LZgIcRSc58o)

## Additional resource

For more information about smoothing, refer to the Smoothing section in the [**Stats Education’s Introduction to R**](http://statseducation.com/Introduction-to-R/modules/graphics/smoothing/ "This link takes you to the Smoothing section in Stats Education's Introduction to R course.") course. It includes detailed descriptions and examples of how to use the different types of smoothing in ggplot2. It also includes links to other lessons about ggplot2. You can explore these to get more familiar with plotting data in R.