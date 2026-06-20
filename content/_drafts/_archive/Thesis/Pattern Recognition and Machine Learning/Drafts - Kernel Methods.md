#type/draft

**memory-based method** ➡methods that involve storing the entire training set in order to make predictions for future data points.


- these methods require a *metric* that measures the similarity of any two vectors in the input space
- generally fast to "train" but slow at making predictions

dual-representation ➡ representation where the predictions are based on linear combinations of a *kernel function*.

---
For a nonlinear *feautre space* mapping $\phi(\text{x})$, the **kernel function is given by the relation:** $$k(\text{x}, \text{x}') = \phi(\text{x}^{T}) \phi(\text{x}')$$

***Note:*** The kernel is a *symmetric* function of its argument

---
