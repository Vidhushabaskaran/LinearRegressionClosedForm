# Linear regression closed-form

The closed-form solution for linear regression is a mathematical approach that determines the best coefficients (slope and intercept) of a linear model directly. By identifying the values that reduce the sum of squared residuals, it reduces the discrepancy between actual and anticipated values. Due to matrix inversion, this method can be computationally expensive for bigger datasets even if it is effective for small to moderate-sized datasets.

![Alt Text](/asset.gif)

### Input dataset

Assume a dataset with $M$ data points
$\mathcal{X} = \{(x_i, y_i), \forall i \in 1...M\}$


### Model definition
Assume a linear model with independent variable $x$ and dependent variable $y$

$$ y = mx + c + \epsilon $$

where, $m,c$ are model parameters and $\epsilon$ in the error term.

### Equation derivation

Complete dataset can be represented in the homogeneous form as follows,


$$\begin{bmatrix}
y_1 \\ 
y_2 \\ 
\vdots \\
 y_M
 \end{bmatrix}^\text{T} = \begin{bmatrix}
 m & c
 \end{bmatrix} \begin{bmatrix}
 x_1 & 1 \\ 
 x_2 & 1 \\ 
 \vdots & \vdots \\
x_M & 1
\end{bmatrix}^\text{T}+\epsilon$$

rewritten,

$$ \mathbf{y} = \mathbf{\phi}^\text{T}\mathbf{X} + \epsilon$$

Squared residuals (or) loss term is defined as 

$$\mathcal{L} = \|\mathbf{y} - \hat{\mathbf{y}}\|^2_2$$

$$\mathcal{L} = \|\mathbf{y} - \mathbf{\phi}^\text{T}\mathbf{X} + \epsilon\|^2_2$$


where, $\hat{\mathbf{y}}$ denotes predicted values using the considered model.
Best model is the one which produces least error

$$\frac{d\mathcal{L}}{d\mathbf{\phi}} = 0$$

Upon simplification,

$$\mathbf{\phi} = (\mathbf{X}^\text{T}\mathbf{X})^{-1}\mathbf{X}^\text{T}\mathbf{y}$$


### Usage

run 
```
python3 line_fitting_closed_form_solution.py
```

Interactively add points to the plot using mouse! and see the updated best linear fit.
