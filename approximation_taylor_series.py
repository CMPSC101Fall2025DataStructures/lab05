#!/usr/bin/env python3

# Name: Add Your Name Here
# Date: Add Today's Date Here


"""
Taylor Series Demonstration for Exponential and Natural Logarithm Functions

This module demonstrates how Taylor series can be used to approximate mathematical
functions like e^x and ln(1+x). The Taylor series provides a way to represent
functions as infinite sums of terms calculated from the function's derivatives.

Taylor Series Formulas:
- e^x = 1 + x + x²/2! + x³/3! + x⁴/4! + ... = Σ(x^n/n!) for n=0 to ∞
- ln(1+x) = x - x²/2 + x³/3 - x⁴/4 + ... = Σ((-1)^(n-1) * x^n/n) for n=1 to ∞

"""

# TODO #1: We're missing some important imports! Run your code, check the error messages to see what's needed.
# HINT: We need math, numpy, matplotlib, and typing modules
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple


def factorial(n: int) -> int:
    """Calculate factorial of n using iteration for efficiency."""
    if n <= 1:
        return 1
    result = 1
    # TODO #2: Same bug as in the simple version - check the range!
    for i in range(2, n):  # BUG: Should be range(2, n + 1)
        result *= i
    return result


def taylor_exp(x: float, n_terms: int = 10) -> float:
    """
    Calculate e^x using Taylor series expansion.
    
    Taylor series for e^x:
    e^x = 1 + x + x²/2! + x³/3! + x⁴/4! + ... = Σ(x^n/n!) for n=0 to ∞
    
    Args:
        x: Input value
        n_terms: Number of terms to include in the series
        
    Returns:
        Approximation of e^x
    """
    result = 0.0
    # TODO #10: There is a subtle bug with large x values! The factorial function becomes very slow.
    # HINT: For large factorials, try calculating x=10 with many terms. What happens to performance?
    # HINT: Consider a more efficient way to calculate terms without calling factorial() every time.
    for n in range(n_terms):
        term = (x ** n) / factorial(n)
        result += term
    return result


def taylor_ln(x: float, n_terms: int = 100) -> float:
    """
    Calculate ln(1+x) using Taylor series expansion.
    
    Taylor series for ln(1+x):
    ln(1+x) = x - x²/2 + x³/3 - x⁴/4 + ... = Σ((-1)^(n-1) * x^n/n) for n=1 to ∞
    
    Note: This series converges for -1 < x ≤ 1
    
    Args:
        x: Input value (must be > -1 for convergence)
        n_terms: Number of terms to include in the series
        
    Returns:
        Approximation of ln(1+x)
    """
    # TODO #11: The input validation is incomplete! What about the upper bound?
    # HINT: The series only converges for -1 < x ≤ 1. What happens if x > 1?
    # HINT: Try running the program with x = 2 and see what happens to accuracy.
    if x <= -1:
        raise ValueError("x must be greater than -1 for ln(1+x) to be defined")
    
    result = 0.0
    # TODO #3: The same sign error from the simple version - fix the alternating pattern!
    for n in range(1, n_terms + 1):
        term = ((-1) ** n) * (x ** n) / n  # BUG: Should be (-1)**(n-1)
        result += term
    return result


def compare_accuracy(x: float, n_terms_list: List[int]) -> None:
    """
    Compare Taylor series approximations with actual function values.
    
    Args:
        x: Input value to test
        n_terms_list: List of term counts to test
    """
    print(f"\nAccuracy comparison for x = {x}")
    print("=" * 60)
    
    # Test exponential function
    # TODO #4: Missing math import will cause this to fail
    actual_exp = math.exp(x)  # NameError without import math
    print(f"Actual e^{x} = {actual_exp:.10f}")
    print("\nTaylor series approximations for e^x:")
    print("Terms\tApproximation\t\tError\t\t% Error")
    print("-" * 60)
    
    for n in n_terms_list:
        approx = taylor_exp(x, n)
        error = abs(actual_exp - approx)
        # TODO #12: There is a potential division by zero error here! What if actual_exp is 0?
        # HINT: Although e^x is never actually 0, what if the approximation is very poor?
        # HINT: Add a check to prevent division by zero and handle the edge case properly.
        percent_error = (error / actual_exp) * 100
        print(f"{n}\t{approx:.10f}\t{error:.2e}\t{percent_error:.6f}%")
    
    # Test natural logarithm function (only for valid range)
    if x > -1:
        # TODO #5: Another place where missing math import causes problems
        actual_ln = math.log(1 + x)  # NameError without import math
        print(f"\nActual ln(1+{x}) = {actual_ln:.10f}")
        print("\nTaylor series approximations for ln(1+x):")
        print("Terms\tApproximation\t\tError\t\t% Error")
        print("-" * 60)
        
        for n in n_terms_list:
            try:
                approx = taylor_ln(x, n)
                error = abs(actual_ln - approx)
                percent_error = (error / abs(actual_ln)) * 100 if actual_ln != 0 else 0
                print(f"{n}\t{approx:.10f}\t{error:.2e}\t{percent_error:.6f}%")
            except ValueError as e:
                print(f"{n}\tError: {e}")


def plot_convergence() -> None:
    """
    Create plots showing how Taylor series approximations converge to actual functions.
    """
    # Set up the plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Plot 1: Exponential function
    x_exp = np.linspace(-2, 2, 1000)
    y_actual_exp = np.exp(x_exp)  # This works with numpy
    
    ax1.plot(x_exp, y_actual_exp, 'k-', linewidth=2, label='Actual e^x')
    
    colors = ['red', 'blue', 'green', 'orange', 'purple']
    term_counts = [1, 3, 5, 10, 15]
    
    # TODO #13: There is a list index error waiting to happen! What if we add more term_counts?
    # HINT: What happens if term_counts has more elements than colors?
    # HINT: Try adding [20, 25] to term_counts and see what error you get.
    for i, n_terms in enumerate(term_counts):
        y_taylor_exp = [taylor_exp(x, n_terms) for x in x_exp]
        ax1.plot(x_exp, y_taylor_exp, '--', color=colors[i], 
                label=f'Taylor (n={n_terms})', alpha=0.7)
    
    ax1.set_xlabel('x')
    ax1.set_ylabel('e^x')
    ax1.set_title('Taylor Series Approximation of e^x')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(0, 15)
    
    # Plot 2: Natural logarithm function
    x_ln = np.linspace(-0.9, 1, 1000)
    y_actual_ln = np.log(1 + x_ln)  # This works with numpy
    
    ax2.plot(x_ln, y_actual_ln, 'k-', linewidth=2, label='Actual ln(1+x)')
    
    for i, n_terms in enumerate(term_counts):
        y_taylor_ln = []
        for x in x_ln:
            try:
                y_taylor_ln.append(taylor_ln(x, n_terms))
            except ValueError:
                y_taylor_ln.append(float('nan'))
        
        ax2.plot(x_ln, y_taylor_ln, '--', color=colors[i], 
                label=f'Taylor (n={n_terms})', alpha=0.7)
    
    ax2.set_xlabel('x')
    ax2.set_ylabel('ln(1+x)')
    ax2.set_title('Taylor Series Approximation of ln(1+x)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    # TODO #6: Adjust this path for your system or use a simple filename
    plt.savefig('taylor_convergence.png', dpi=300, bbox_inches='tight')
    plt.show()


def interactive_demo() -> None:
    """
    Interactive demonstration of Taylor series approximations.
    """
    print("Taylor Series Demonstration")
    print("=" * 50)
    print("This program demonstrates Taylor series approximations for:")
    print("1. e^x (exponential function)")
    print("2. ln(1+x) (natural logarithm function)")
    print()
    
    while True:
        try:
            print("\nChoose a function to approximate:")
            print("1. e^x")
            print("2. ln(1+x)")
            print("3. Compare both functions")
            print("4. Show convergence plots")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '5':
                print("Thank you for using the Taylor Series demonstration!")
                break
            elif choice == '4':
                print("Generating convergence plots...")
                plot_convergence()
                continue
            elif choice == '3':
                x = float(input("Enter a value for x: "))
                n_terms_list = [5, 10, 20, 50]
                compare_accuracy(x, n_terms_list)
                continue
            
            x = float(input("Enter a value for x: "))
            # TODO #14: There is an input validation bug here! What if the user enters a negative number of terms?
            # HINT: What happens if someone enters -5 for number of terms? Should that be allowed?
            # HINT: Add validation to ensure n_terms is positive and reasonable (e.g., between 1 and 100).
            n_terms = int(input("Enter number of terms to use (default 10): ") or "10")
            
            if choice == '1':
                # Exponential function
                # TODO #7: More missing math import issues here
                actual = math.exp(x)  # NameError without import math
                approx = taylor_exp(x, n_terms)
                error = abs(actual - approx)
                
                print(f"\nResults for e^{x}:")
                print(f"Actual value: {actual:.10f}")
                print(f"Taylor approximation ({n_terms} terms): {approx:.10f}")
                print(f"Absolute error: {error:.2e}")
                print(f"Relative error: {(error/actual)*100:.6f}%")
                
            elif choice == '2':
                # Natural logarithm function
                if x <= -1:
                    print("Error: x must be greater than -1 for ln(1+x)")
                    continue
                    
                # TODO #8: And another math import issue
                actual = math.log(1 + x)  # NameError without import math
                approx = taylor_ln(x, n_terms)
                error = abs(actual - approx)
                
                print(f"\nResults for ln(1+{x}):")
                print(f"Actual value: {actual:.10f}")
                print(f"Taylor approximation ({n_terms} terms): {approx:.10f}")
                print(f"Absolute error: {error:.2e}")
                if actual != 0:
                    print(f"Relative error: {(error/abs(actual))*100:.6f}%")
            
        except ValueError as e:
            print(f"Invalid input: {e}")
        except KeyboardInterrupt:
            print("\nExiting...")
            break


if __name__ == "__main__":
    # TODO #9: Fix all the bugs above before running this!
    # Remember: import math, fix factorial range, fix taylor_ln sign
    interactive_demo()