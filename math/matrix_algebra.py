# Matrix Algebra

##Define Matrices as listed in exercises using NumPy
import numpy

A=numpy.matrix([[1,2,3],[2,7,4]])
B=numpy.matrix([[1,-1],[0,1]])
C=numpy.matrix([[5,-1],[9,1],[6,0]])
D=numpy.matrix([[3,-2,-1],[1,2,3]])

u=numpy.array([6,2,-3,5])
v=numpy.array([3,5,-1,4])
w=numpy.matrix([[1],[8],[0],[5]])


##Part 1: Matrix Dimentions
print "Dimention of A:", A.shape #Dimention of A: (2,3)
print "Dimention of B:", B.shape #Dimention of B: (2,2)
print "Dimention of C:", C.shape #Dimention of C: (3,2)
print "Dimention of D:", D.shape #Dimention of D: (2,3)
print "Dimention of u:", u.shape #Dimention of u: (4,) (aka 1,4 if was written as matrix not array) :)
print "Dimention of w:", w.shape #Dimention of w: (4,1) :)


##Part 2: Vector Operations
print u+v #[9,7,-4,9]
print u-v #[3,-3,-2,1]
print 6*u #[36,12,-18,30]
print numpy.dot(u,v) #51
print numpy.linalg.norm(u)**2 #74 (so norm is sqrt(74))


##Part 3: Matrix Operations
print A+C #Not defined (ValueError: operands could not be broadcast together with shapes (2,3) (3,2))
print A-(numpy.matrix.transpose(C)) #[[-4 -7 -3], [ 3  6  4]]
print (numpy.matrix.transpose(C))+(3*D) #[[14  3  3], [ 2  7  9]]
print B*A #[[-1 -5 -1], [ 2  7  4]]
print B*(numpy.matrix.transpose(A)) #Not defined (ValueError: shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0))
print B*C #Not defined (ValueError: shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0))
print C*B #[[ 5 -6], [ 9 -8], [ 6 -6]]
print B**4 #[[ 1 -4], [ 0  1]]
print A*(numpy.matrix.transpose(A)) #[[14 28], [28 69]]
print (numpy.matrix.transpose(D))*D #[[10 -4  0], [-4  8  8], [ 0  8 10]]







