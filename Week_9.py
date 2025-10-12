import numpy as np
# Take own 2 vectors and 2 3x3 matrices and perfrom all operations - Addition,Subtraction,Scalar Multiplication, Dot Product, Cross product, Magnitude, Unit vector, Transpose, Determinant, Inverse, Rank, Trace, Eigenvalues and vectors, Identity, Zeros and Ones and Diagonal
# A company tracks the number of products sold each month, help the manager to analyze the sale trend.
# A website tracks the number of visitors everyday for 30 days, the website manager wants to analyze the traffic patterns, help him with your program

# Given sales = [120,135,150,160,170,180,200,210,250,300,320,500]
# Visitors = np.array([120,135,150,160,170,180,200,210,250,300,320,500,480,460,450,430,420,410,400,390,380,370,360,350,340,330,320,310,300,290])

def one():
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])

    m1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

    print("Vector Addition:", v1 + v2)
    print("Vector Subtraction:", v1 - v2)
    print("Scalar Multiplication (v1 * 2):", v1 * 2)
    print("Dot Product:", np.dot(v1, v2))
    print("Cross Product:", np.cross(v1, v2))
    print("Magnitude of v1:", np.linalg.norm(v1))
    print("Unit Vector of v1:", v1 / np.linalg.norm(v1))

    print("\nMatrix Addition:\n", m1 + m2)
    print("Transpose of m1:\n", m1.T)
    print("Determinant of m1:", np.linalg.det(m1))
    print("Trace of m1:", np.trace(m1))
    print("Rank of m1:", np.linalg.matrix_rank(m1))
    print("Eigenvalues and Eigenvectors of m1:\n", np.linalg.eig(m1))
    print("Identity Matrix:\n", np.eye(3))
    print("Zeros Matrix:\n", np.zeros((3, 3)))
    print("Ones Matrix:\n", np.ones((3, 3)))
    print("Diagonal of m1:", np.diag(m1))

def two_sales():
    sales = [120,135,150,160,170,180,200,210,250,300,320,500]
    sales_array = np.array(sales)
    print("Sales Data Analysis")
    print("Total Sales:", np.sum(sales_array))
    print("Average Sales:", np.mean(sales_array))
    print("Median Sales:", np.median(sales_array))
    print("Maximum Sales:", np.max(sales_array))
    print("Minimum Sales:", np.min(sales_array))
    print("Sales Standard Deviation:", np.std(sales_array))
    print("Monthly Sales Growth:", np.diff(sales_array))
    print("Months in year with sales above average:", np.where(sales_array > np.mean(sales_array))[0] + 1)

def three_visitors():
    visitors = np.array([120,135,150,160,170,180,200,210,250,300,320,500,480,460,450,430,420,410,400,390,380,370,360,350,340,330,320,310,300,290])
    print("Website Visitors Analysis")
    print("Total Visitors in 30 days:", np.sum(visitors))
    print("Average Daily Visitors:", np.mean(visitors))
    print("Median Daily Visitors:", np.median(visitors))
    print("Maximum Daily Visitors:", np.max(visitors))
    print("Minimum Daily Visitors:", np.min(visitors))
    print("Visitors Standard Deviation:", np.std(visitors))
    print("Daily Visitor Change:", np.diff(visitors))
    print("Days of month with visitors above average:", np.where(visitors > np.mean(visitors))[0] + 1)

                                                         

one()
two_sales()
three_visitors()