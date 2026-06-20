
Convex functions are **real valued functions** which visually can be understood as functions which satisfy the fact that the line segment joining any two points on the graph of the function lie above that of the function.^[[Convex Functions | Brilliant](https://brilliant.org/wiki/convex-functions/)]


![512px-ConvexFunction.svg.png (512×266) (wikimedia.org)|400](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/ConvexFunction.svg/512px-ConvexFunction.svg.png)



> [!NOTE]- Examples
> Common examples include $f(x)=x^2$ and $f(x)=e^x$. 

Any value of $x$ in the interval from $x=a$ to $x=b$ can be written in the form $$\lambda a + (1-\lambda)b$$ where $0\leq \lambda \leq 1$.

The corresponsing point on the chord is given by $$\lambda f(a) + (1-\lambda) f(b)$$ and the corresponding value of the function is $$f(\lambda a + (1-\lambda)b)$$

Convexity implies $$f(\lambda a + (1-\lambda)b) \leq \lambda f(a) + (1-\lambda) f(b)$$

---
 A function is *strictly convex* if the equality is satisfied only for $\lambda=0$ and $\lambda=1$.

# Definition 
We start by defining what a convex set is. 

> [!Note] Convex Set
> A set $E \subseteq \mathbb{R}$ is said to be convex if given $x,y \in E$ such that $x<y$ then $[x,y] \subseteq E$.

> [!NOTE] Convex Function
> Let $E$ be a convex set and $f: E \to \mathbb{R}$ be a function. Then $f$ is said to be convex if the following condition holds:
> $$f(\lambda x + (1-\lambda)y) \leq \lambda f(x)+ (1-\lambda) f(y) \qquad \forall \lambda \in (0,1); x,y \in E$$


