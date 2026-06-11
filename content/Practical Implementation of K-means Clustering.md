Assumptions of K-means algorithm
1. The data is symmetrically distributed / not skewed.
2. The variables have the same average values
3. The variables have the same variance

Remark: Basically, the variables have to be normally distributed.

- To handle skewness: use logarithmic transformation
- To handle varying average: centering 
- To handle varying variance: scaling

Remark: centering and scaling are both automatically handled in scikit-learn's `StandardScaler`.

Recommended sequence for data pre-processing
1. Unskew the data (via log transformation)
2. Standardize to have the same average values
3. Scale to have the same standard deviation/variance
4. Store as a separate array to be used for clustering model.

# Key steps in implementing k-means
1. Data pre-processing (see recommended steps above)
2. Choose a number of clusters
	1. Methods to define the number of clusters
		1. visual method - via elbow criterion
		2. mathematical method - via silhouette coefficient
		3. experimentation/interpretation (industry knowledge)
3. Running k-means clustering on pre-processed data
4. Analysis and interpretation