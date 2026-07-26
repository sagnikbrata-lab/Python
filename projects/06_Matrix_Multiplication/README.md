# Matrix Multiplication

A Python implementation of general matrix multiplication for matrices of arbitrary dimensions.

## Description

This program multiplies two matrices of dimensions **n × m** and **m × p** using the standard three-loop algorithm taught in introductory linear algebra.

The program:

- verifies whether multiplication is defined,
- computes the matrix product,
- returns the resulting matrix, and
- reports when multiplication is not possible.

## Concepts Practised

- Functions
- Nested loops
- Two-dimensional lists
- Matrix indexing
- Dimension validation
- Algorithm implementation

## Mathematical Background

For matrices

- A of size **n × m**
- B of size **m × p**

their product

**C = AB**

is an **n × p** matrix where

```
            m-1
C[i][j] =   Σ   A[i][k] × B[k][j]
           k=0
```

## Example

```
A × B

[94, 100]
[229, 244]
[364, 388]
[499, 532]
```

## Future Improvements

- Accept matrix input from the user
- Validate empty or irregular matrices
- Improve output formatting
- Compare performance with NumPy
- Measure execution time for large matrices

---

Created while learning matrix multiplication in my first-year B.Sc. Physics course. This project implements the standard three-loop algorithm as a programming exercise to reinforce the underlying mathematics.