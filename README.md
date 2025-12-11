## 🧪 Error Propagation Calculator (Python/SymPy)

This Python script uses the `sympy` library to calculate the **best value** and the **propagation of error** for a given mathematical expression, based on the measured values and associated errors of the independent variables.

It implements the general formula for the propagation of uncertainty (error), which is:

$$\delta f = \sqrt{\sum_{i} \left( \frac{\partial f}{\partial x_i} \delta x_i \right)^2}$$

Where:
* $f$ is the calculated expression.
* $x_i$ are the independent variables.
* $\frac{\partial f}{\partial x_i}$ is the partial derivative of the expression $f$ with respect to the variable $x_i$.
* $\delta x_i$ is the error (uncertainty) in the variable $x_i$.
* $\delta f$ is the calculated error in the result $f$.

### 🚀 Usage

1.  **Dependencies:** Ensure you have the `sympy` library installed.
    ```bash
    pip install sympy
    ```

2.  **Run the script:** Execute the Python file.

3.  **Input Variables:**
    * The program will first prompt you to enter the **variables**, their **true values**, and their associated **errors**.
    * **Format:** `variable true_value error` (separated by spaces).
    * **Example Input:**
        ```
        x 3 0.1
        y 5 0.2
        Type "done" if finished
        Enter your variables, true value and error: done
        ```

4.  **Input Expression:**
    * Next, you will be prompted to enter the mathematical expression.
    * **Use Python/SymPy Syntax:** Utilize standard Python operators and SymPy functions.
    * **Example Input:**
        ```
        Enter your expression: x**2 + sin(y)
        ```

### 💡 Key Features and Notes

* **Syntax:** Use standard Python syntax for operations (e.g., `*` for multiplication, `**` for exponentiation).
* **Functions:** Supports standard trigonometric and exponential functions from SymPy, such as `sin()`, `cos()`, `tan()`, `exp()`, `log()`, etc.
* **Angles:** All trigonometric function inputs (angles) **must be in radians**. Use `pi` or `sympy.pi` for the mathematical constant $\pi$.
* **Output:** The final result is displayed as:
    * The **Best Value** of the expression.
    * The **Error** (uncertainty) of the expression.
    * The result in **scientific notation** in the format `Best Value ± Error`.

### ⚠️ Important Guidelines for Input

* **Delimeter:** Use **space** to separate the variable, true value, and error when defining variables.
* **Constants:** All constant values must be entered **explicitly** (e.g., use `2*x` instead of `2x`).
* **Keywords:** **Avoid** using Python/SymPy keywords (e.g., `for`, `if`, `pi`, `I`) as variable names.

### 📜 Code Walkthrough

1.  **Initialization:** Dictionaries `variables` (stores value and error) and `vars` (stores only the value for substitution) are initialized.
2.  **Variable Input Loop:** Reads variable data until the user types `"done"`. It converts variable names into symbolic expressions using `symbols()`.
3.  **Expression Input:** Reads the mathematical expression from the user.
4.  **Error Propagation Calculation:**
    * It iterates through each variable (`key` in `variables`).
    * `diff(expression, key)`: Calculates the partial derivative $\frac{\partial f}{\partial x_i}$.
    * `partial.subs(vars)`: Substitutes the true values of all variables into the partial derivative to get a numerical value.
    * The result is multiplied by the variable's error ($\delta x_i$).
    * The terms $(\frac{\partial f}{\partial x_i} \delta x_i)^2$ are summed up.
    * The final error is calculated as the square root of the sum (`summ**0.5`).
5.  **Best Value Calculation:**
    * `simplify(expression).subs(vars)`: Substitutes the true values into the original expression to find the **best value**.
6.  **Output Formatting:**