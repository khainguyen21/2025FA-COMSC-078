from abc import ABC, abstractmethod


class Rational:
    """Class to represent rational numbers"""
    
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        
        # Compute GCD to simplify the rational number
        def gcd(a, b):
            a, b = abs(a), abs(b)
            while b:
                a, b = b, a % b
            return a
        
        g = gcd(numerator, denominator)
        
        # Handle sign: keep negative sign in numerator
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        
        self.numerator = numerator // g
        self.denominator = denominator // g
    
    def __add__(self, other):
        """Add two rational numbers"""
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Rational(num, den)
    
    def __mul__(self, other):
        """Multiply two rational numbers"""
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Rational(num, den)
    
    def __str__(self):
        """String representation of rational number"""
        return f"{self.numerator}/{self.denominator}"
    
    def __repr__(self):
        return self.__str__()


class GenericMatrix(ABC):
    """Abstract class that operates on matrices with the same types of numbers"""
    
    def __init__(self, matrix):
        """Initialize with a matrix (list of lists)"""
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if matrix else 0
    
    @abstractmethod
    def add(self, element1, element2):
        """Adds two elements drawn from matrices"""
        pass
    
    @abstractmethod
    def multiply(self, element1, element2):
        """For multiplying two elements drawn from matrices"""
        pass
    
    @abstractmethod
    def zero(self):
        """Abstract method for defining the zero element for the type of matrix"""
        pass
    
    def addMatrix(self, other):
        """Adds two matrices with the same types of elements and returns the resulting matrix"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition")
        
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.add(self.matrix[i][j], other.matrix[i][j]))
            result.append(row)
        
        return self.__class__(result)
    
    def multiplyMatrix(self, other):
        """Multiplies two matrices with the same types of elements and returns the resulting matrix"""
        if self.cols != other.rows:
            raise ValueError("Number of columns in first matrix must equal number of rows in second matrix")
        
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                # Compute the element at position (i, j)
                element = self.zero()
                for k in range(self.cols):
                    product = self.multiply(self.matrix[i][k], other.matrix[k][j])
                    element = self.add(element, product)
                row.append(element)
            result.append(row)
        
        return self.__class__(result)
    
    def __str__(self):
        """Returns the string representation of the matrix"""
        result = ""
        for row in self.matrix:
            result += "  ".join(str(element) for element in row) + "\n"
        return result.strip()


class IntegerMatrix(GenericMatrix):
    """Allows you to add and multiply the elements in an IntegerMatrix"""
    
    def __init__(self, matrix):
        """Initialize integer matrix"""
        super().__init__(matrix)
    
    def add(self, element1, element2):
        """Adds two integers and return the sum"""
        return element1 + element2
    
    def multiply(self, element1, element2):
        """Multiplies two integers and returns the product"""
        return element1 * element2
    
    def zero(self):
        """Returns 0 as an integer"""
        return 0


class RationalMatrix(GenericMatrix):
    """Allows you to add and multiply two elements in a RationalMatrix"""
    
    def __init__(self, matrix):
        """Initialize rational matrix"""
        super().__init__(matrix)
    
    def add(self, element1, element2):
        """Add and return the sum of two rational numbers"""
        return element1 + element2
    
    def multiply(self, element1, element2):
        """Multiply and return the product of two rational numbers"""
        return element1 * element2
    
    def zero(self):
        """Returns the zero for rational numbers (0/1)"""
        return Rational(0, 1)


def main():
    """Main program to test integer and rational matrices"""
    
    print("=" * 60)
    print("Testing Integer Matrices")
    print("=" * 60)
    
    # Create two integer matrices
    m1 = IntegerMatrix([[1, 2, 3],
                        [4, 5, 6],
                        [1, 1, 1]])
    
    m2 = IntegerMatrix([[1, 1, 1],
                        [2, 2, 2],
                        [0, 0, 0]])
    
    print("\nm1 is:")
    print(m1)
    
    print("\nm2 is:")
    print(m2)
    
    # Add matrices
    print("\nm1 + m2 is:")
    m3 = m1.addMatrix(m2)
    print(m3)
    
    # Multiply matrices
    print("\nm1 * m2 is:")
    m4 = m1.multiplyMatrix(m2)
    print(m4)
    
    print("\n" + "=" * 60)
    print("Testing Rational Matrices")
    print("=" * 60)
    
    # Create two rational matrices
    r1 = RationalMatrix([[Rational(1, 5), Rational(1, 6), Rational(1, 7)],
                         [Rational(2, 5), Rational(1, 3), Rational(2, 7)],
                         [Rational(3, 5), Rational(1, 2), Rational(3, 7)]])
    
    r2 = RationalMatrix([[Rational(1, 6), Rational(1, 7), Rational(1, 8)],
                         [Rational(1, 3), Rational(2, 7), Rational(1, 4)],
                         [Rational(1, 2), Rational(3, 7), Rational(3, 8)]])
    
    print("\nr1 is:")
    print(r1)
    
    print("\nr2 is:")
    print(r2)
    
    # Add rational matrices
    print("\nr1 + r2 is:")
    r3 = r1.addMatrix(r2)
    print(r3)
    
    # Multiply rational matrices
    print("\nr1 * r2 is:")
    r4 = r1.multiplyMatrix(r2)
    print(r4)
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()