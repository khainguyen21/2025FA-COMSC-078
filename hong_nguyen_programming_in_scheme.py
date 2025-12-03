"""
Programming Assignment: Higher-Order Procedures in Scheme
Author: Hong Nguyen
Description: This file contains Scheme procedures that demonstrate higher-order functions,
including sum-integers, sum-cubes, and pi-sum implementations.
"""

# ==========================================
# Scheme Code (to be run in a Scheme interpreter)
# ==========================================

scheme_code = '''
; Helper procedure: cube
; Returns the cube of an integer argument
(define (cube n)
  (* n n n))

; Helper procedure: identity
; Returns its parameter unchanged
(define (identity n)
  n)

; Helper procedure: pi-term
; Returns the value 8 / ((4 * n - 3) * (4 * n - 1))
(define (pi-term n)
  (/ 8 (* (- (* 4 n) 3) (- (* 4 n) 1))))

; Higher-order procedure: summation
; Accepts a procedure, lower bound, and upper bound
; Sums the values of applying the procedure to each integer from lower to upper
(define (summation proc lower upper)
  (if (> lower upper)
      0
      (+ (proc lower)
         (summation proc (+ lower 1) upper))))

; Alternative iterative version of summation (more efficient)
(define (summation-iter proc lower upper)
  (define (iter current total)
    (if (> current upper)
        total
        (iter (+ current 1) (+ total (proc current)))))
  (iter lower 0))

; 1) sum-integers: computes the sum of consecutive integers from a through b
(define (sum-integers a b)
  (summation identity a b))

; 2) sum-cubes: computes the sum of cubes of integers from a to b
(define (sum-cubes a b)
  (summation cube a b))

; 3) pi-sum: computes the sum of terms in the series that converges to pi
(define (pi-sum n)
  (summation pi-term 1 n))

; ==========================================
; Test cases and examples
; ==========================================

; Test sum-integers
; Example: (sum-integers 1 10) should return 55
; 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55

; Test sum-cubes
; Example: (sum-cubes 1 3) should return 36
; 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36

; Test pi-sum
; Example: (pi-sum 1000) should approximate pi (around 3.14...)
; The more terms, the closer to pi

; To test these procedures, run them in a Scheme interpreter:
(sum-integers 1 10) 
(sum-cubes 1 3)     
(sum-cubes 1 10)    
(pi-sum 100)        
(pi-sum 1000)       
(pi-sum 10000)      
'''

# Print the Scheme code for reference
print(scheme_code)


# ==========================================
# Python equivalents for verification
# ==========================================

def cube(n):
    """Returns the cube of n"""
    return n * n * n


def identity(n):
    """Returns n unchanged"""
    return n


def pi_term(n):
    """Returns the pi series term: 8 / ((4n - 3) * (4n - 1))"""
    return 8 / ((4 * n - 3) * (4 * n - 1))


def summation(proc, lower, upper):
    """Higher-order function that sums proc(i) for i from lower to upper"""
    total = 0
    for i in range(lower, upper + 1):
        total += proc(i)
    return total


def sum_integers(a, b):
    """Computes the sum of consecutive integers from a through b"""
    return summation(identity, a, b)


def sum_cubes(a, b):
    """Computes the sum of cubes of integers from a to b"""
    return summation(cube, a, b)


def pi_sum(n):
    """Computes the sum of terms in the series that converges to pi"""
    return summation(pi_term, 1, n)


# ==========================================
# Test and verify calculations
# ==========================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("Python Verification of Calculations")
    print("=" * 60)

    # Test sum-integers
    result1 = sum_integers(1, 10)
    print(f"\nsum_integers(1, 10) = {result1}")
    print(f"Expected: 55 (1+2+3+4+5+6+7+8+9+10)")
    print(f"Correct: {result1 == 55}")

    # Test sum-cubes
    result2 = sum_cubes(1, 3)
    print(f"\nsum_cubes(1, 3) = {result2}")
    print(f"Expected: 36 (1³ + 2³ + 3³ = 1 + 8 + 27)")
    print(f"Correct: {result2 == 36}")

    result3 = sum_cubes(1, 10)
    print(f"\nsum_cubes(1, 10) = {result3}")
    print(f"Expected: 3025")
    print(f"Correct: {result3 == 3025}")

    # Test pi-sum
    result4 = pi_sum(100)
    print(f"\npi_sum(100) = {result4:.6f}")
    print(f"Error from π: {abs(result4 - 3.141592653589793):.6f}")

    result5 = pi_sum(1000)
    print(f"\npi_sum(1000) = {result5:.6f}")
    print(f"Error from π: {abs(result5 - 3.141592653589793):.6f}")

    result6 = pi_sum(10000)
    print(f"\npi_sum(10000) = {result6:.6f}")
    print(f"Error from π: {abs(result6 - 3.141592653589793):.6f}")

    print("\n" + "=" * 60)
    print("Copy the Scheme code above to test in a Scheme interpreter")
    print("=" * 60)