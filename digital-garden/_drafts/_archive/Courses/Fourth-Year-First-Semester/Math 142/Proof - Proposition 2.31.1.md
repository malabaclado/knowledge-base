# Proposition 2.31.1
Let $f: (S, \rho) \to (T, \tau)$ be a function from the metric space $(S, \rho)$ to the metric space $(T, \tau)$.


The function $f$ is continuous at $p\in S$ if for every open set $\mathcal{U} \in T$, the pre-image $f^{-1}(\mathcal{U})$ contains a subset $\mathcal{O}$ such that $p \in \mathcal{O}$

---
# Proof
Assume that for all open set $\mathcal{U} \subset T$ such that $f(p) \in T$, there exists an open set $\mathcal{O} \subset f^{-1}(\mathcal{U})$ such that $p \in \mathcal{O}$.


Since $\mathcal{U}$ is open, then there exists an open ball $B(f(p), \epsilon) \subset \mathcal{U}$.

Fix $\epsilon >0$. By hypothesis, there exists an open set $\mathcal{O} \subset f^{-1}(B(f(p), \epsilon))$.

Choose an open set $\mathcal{O}$ such that $p \in \mathcal{O} \subset f^{-1}(B(f(p), \epsilon))$.

Choose $\delta_\epsilon>0$ such that $B(p, \delta_\epsilon) \subset \mathcal{O}$

> Here, $\delta_\epsilon$ depends on the value of $\epsilon$, hence the notation.

Let $q \in S$ such that $\rho(q,p) < \delta_\epsilon$. Then $q \in B(p, \delta_\epsilon)$ which implies $q \in \mathcal{O}$. It follows that $f(q) \in B(f(p)), \epsilon$. Thus, $\tau(f(q), f(p)) < \epsilon$. 

*End of proof.*