# Python Learning Journey

Welcome to my Python Learning repository! This is a personal project where I explore the fundamentals of Python programming through hands-on coding exercises and mini-projects. Each file in this repository represents a step forward in my journey to mastering Python.

---

## 📂 Repository Contents

### **Day 1**
#### 1. [`hello.py`](https://github.com/Ayush-Bitla/Python/blob/main/Day1/hello.py)
- A simple introductory script to print "Hello, World!" using Python.
- Demonstrates the basics of variable assignment and the `print()` function.

#### 2. [`data_types.py`](https://github.com/Ayush-Bitla/Python/blob/main/Day1/data_types.py)
- Explores Python data types, including:
  - **Strings**: Assignment, concatenation, multiline strings, escaping characters, and string methods.
  - **Numbers**: Integer, float, complex types, and operations like rounding, casting, and absolute value.
  - **Booleans**: Boolean values and type-checking.
- Includes a practical example of formatting a menu with string manipulation.

#### 3. [`meaning.py`](https://github.com/Ayush-Bitla/Python/blob/main/Day1/meaning.py)
- Implements a ternary operator to evaluate a condition and provide output.
- A minimalistic script to reinforce conditional statements.

#### 4. [`rps.py`](https://github.com/Ayush-Bitla/Python/blob/main/Day1/rps.py) (Rock-Paper-Scissors Game)
- A Python implementation of the classic "Rock-Paper-Scissors" game:
  - Utilizes `random` and `enum` modules for computer choice and better code readability.
  - Includes input validation and user interaction.
  - Simple logic for determining the winner.

#### 5. [`welcome.py`](https://github.com/Ayush-Bitla/Python/blob/main/Day1/welcome.py)
- A script to display a simple welcome message using formatted strings.
- Introduces header/footer design and code reusability.

---
### **Day 2**
#### 1. [`dictionaries.py`](https://github.com/Ayush-Bitla/Python/blob/main/Day2/dictionaries.py)
- Explores Python dictionaries and their key-value operations:
  - **Creating Dictionaries**: Using curly braces and the `dict()` constructor.
  - **Accessing and Modifying Data**: Using keys, `.get()`, and `.update()`.
  - **Nested Dictionaries**: Storing complex data structures.

#### 2. [`sets.py`](https://github.com/Ayush-Bitla/Python/blob/main/Day2/sets.py)
- Introduces Python sets and their unique characteristics:
  - **Creating Sets**: Using curly braces or the `set()` constructor.
  - **Set Operations**: Union, intersection, difference, and symmetric difference.
  - **Updating Sets**: Using `.add()` and `.update()` methods.

#### 3. [`lists.py`](https://github.com/Ayush-Bitla/Python/blob/main/Day2/lists.py)
- Delves into Python lists and their operations:
  - **Adding Elements**: Using `.append()` and `.extend()`.
  - **Slicing and Sorting**: Utilizing slicing to modify lists and `.sort()` to arrange elements.
  - **Multi-type Lists**: Handling lists with mixed data types.

#### 4. [`tuples.py`](https://github.com/Ayush-Bitla/Python/blob/main/Day2/tuples.py)
- Explains tuples and their immutability:
  - **Creating Tuples**: Using parentheses or the `tuple()` constructor.
  - **Unpacking Tuples**: Using unpacking techniques for assigning values.

---

### **Day 3**

#### 1. [`functions.py`](https://github.com/Ayush-Bitla/Python/blob/main/Day3/functions.py)
- Introduces Python functions with examples:
  - Basic function definition and calling.
  - Default arguments for functions.
  - Usage of `*args` for handling multiple positional arguments.
  - Usage of `**kwargs` for handling named arguments.
- Provides examples for adding numbers and handling multiple items as arguments.

#### 2. [`loops.py`](https://github.com/Ayush-Bitla/Python/blob/main/Day3/loops.py)
- Demonstrates Python loops:
  - `while` loops with conditions, and handling special cases like `break` and `continue`.
  - `for` loops iterating over lists and ranges.
  - Nested loops to combine two or more loops for different actions.
  - The use of `else` with loops.
- Includes examples of printing a range of numbers and names with corresponding actions using nested loops.

#### 3. [`rock_paper_scissors_2.py`](https://github.com/Ayush-Bitla/Python/blob/main/Day3/rps2.py)
- An enhanced version of the classic Rock-Paper-Scissors game:
  - Uses Python's `enum` module to define possible moves (Rock, Paper, Scissors).
  - Generates a random choice for the computer.
  - Includes input validation for user input.
  - Provides options to replay the game and handles input for playing again or quitting.
  - Displays the result of the game based on user choice and computer choice.

---

### **Day 4**

#### 1. [`example.py`](https://github.com/Ayush-Bitla/Python/blob/main/Day4/example.py)
- Demonstrates the use of `while` loops and `break` and `continue` statements.
  - The loop continues until a certain condition is met, with `count` being incremented each time.
  - Includes a conditional check to break the loop at a specific count.

#### 2. [`recursion.py`](https://github.com/Ayush-Bitla/Python/blob/main/Day4/recursion.py)
- Introduces recursion by defining a function `add_one()`:
  - Recursively adds 1 to a number until a base condition is met.
  - Demonstrates the importance of base cases to prevent infinite recursion.
  - Shows how recursion can be used to perform repeated actions.

#### 3. [`rps3.py`](https://github.com/Ayush-Bitla/Python/blob/main/Day4/rps3.py) (Rock-Paper-Scissors Game)
- An implementation of the classic "Rock-Paper-Scissors" game:
  - Uses recursion for replaying the game.
  - Implements a `while` loop to validate user input for game choices.
  - The game continues until the player chooses to quit.

#### 4. [`rps4.py`](https://github.com/Ayush-Bitla/Python/blob/main/Day4/rps4.py) (Rock-Paper-Scissors Game with Game Count)
- Enhances the "Rock-Paper-Scissors" game by adding a game counter:
  - Tracks the number of games played.
  - The `decide_winner()` function is separated to handle the logic of determining the winner.
  - Displays the total number of games played at the end of each round.

#### 5. [`scope.py`](https://github.com/Ayush-Bitla/Python/blob/main/Day4/scope.py)
- Demonstrates the concepts of variable scope in Python:
  - Uses the `global` keyword to modify a global variable.
  - Uses the `nonlocal` keyword to modify a variable in the nearest enclosing scope.
  - Shows how different scopes interact with variables in nested functions.

---

### **Day 5**
#### **1. [closure.py](https://github.com/Ayush-Bitla/Python/blob/main/Day5/closure.py)**  
- Demonstrates how closures retain access to parent function variables after the parent function has returned.  
  - Explains the concept with examples of nested functions.  
  - Highlights practical applications such as maintaining state in callbacks.

#### **2. [string_formatting.py](https://github.com/Ayush-Bitla/Python/blob/main/Day5/f_string.py)**  
- Covers various string formatting methods:  
  - `f-strings` for efficient and flexible formatting.  
  - `str.format()` method and `%` formatting for compatibility.

#### **3. [enum_usage.py](https://github.com/Ayush-Bitla/Python/blob/main/Day5/rps6.py)**  
- Explores the use of `Enum` for better representation of constants in Python.  
  - Demonstrates defining enums and accessing their attributes.  
  - Shows how enums improve code readability and maintainability.

#### **4. [interactive_game.py](https://github.com/Ayush-Bitla/Python/blob/main/Day5/rps5.py)**  
- Implements a game using closures and `nonlocal` effectively to maintain and update state.  
  - Demonstrates how closures can simplify state management in interactive applications.  
  - Provides insights into writing cleaner and more modular code using closures.
     
---

### Day 6: Python Projects and Games

#### 1. [`hello_person.py`](https://github.com/Ayush-Bitla/Python/blob/main/Day6/hello_person.py)
- Provides personalized greetings in different languages.
- Features:
  - Accepts a name and language as command-line arguments.
  - Outputs a greeting based on the selected language.
- Highlights:
  - Uses `argparse` for parsing command-line arguments.
  - Demonstrates a dictionary-based approach to store greetings.

---

#### 2. [`kansas.py`](https://github.com/Ayush-Bitla/Python/blob/main/Day6/kansas.py)
- A script highlighting fun facts about Kansas.
- Features:
  - Contains constants like the capital, state bird, flower, and song.
  - Includes a function `randomfunfact()` to display random fun facts about Kansas.
- Highlights:
  - Uses Python's `random` module to select a fun fact.

---

#### 3. [`modules.py`](https://github.com/Ayush-Bitla/Python/blob/main/Day6/modules.py)
- Demonstrates the use of Python modules and importing.
- Features:
  - Imports and uses `math`, `random`, `kansas`, and `rps7` modules.
  - Prints the value of `pi` from the `math` module.
  - Calls `randomfunfact()` from `kansas.py`.
  - Executes the `rock_paper_scissors` function from `rps7.py`.
- Highlights:
  - Explores the `__name__` attribute for module execution.

---

#### 4. [`rps7.py`](https://github.com/Ayush-Bitla/Python/blob/main/Day6/rps7.py)
- Implements the "Rock-Paper-Scissors" game.
- Features:
  - Tracks game count, player wins, and Python wins.
  - Utilizes recursion to replay the game.
  - Uses `Enum` for better representation of choices.
- Highlights:
  - Incorporates `nonlocal` variables for maintaining state within nested functions.

---

#### 5. [`rps8.py`](https://github.com/Ayush-Bitla/Python/blob/main/Day6/rps8.py)
- Enhances the "Rock-Paper-Scissors" game with personalized gameplay.
- Features:
  - Accepts a player's name via command-line arguments.
  - Personalized prompts and messages using the provided name.
  - Tracks the player's and Python's wins.
- Highlights:
  - Leverages `argparse` for command-line input.
  - Demonstrates the combination of `Enum`, recursion, and `nonlocal` for a seamless gaming experience.

---

## 🧠 What I've Learned
- **Day 1**: Basics of Python programming, including variables, data types, and conditional statements.
- **Day 2**: Advanced data structures like dictionaries, sets, lists, and tuples.
- **Day 3**: Function definitions and arguments, looping constructs, and creating interactive games.
- **Day 4**: Recursion, global and nonlocal variable scopes, and enhanced interactive games (Rock-Paper-Scissors) with additional features like game count and input validation.
- **Day 5**: How closures retain access to parent variables, efficient string formatting with f-strings, leveraging Enum for constants, and using closures with nonlocal for state management in interactive games
- **Day 6**: Key learnings: argparse for command-line arguments, dictionary-based lookups, Enum for constants, recursion with nonlocal, and exploring module imports with __name__.


---

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Ayush-Bitla/Python.git
   cd Python

---

## Stay tuned for more updates as I continue my Python learning journey! 🚀

- Feel free to make edits or additions to personalize further! 😊
