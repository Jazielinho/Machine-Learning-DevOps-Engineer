
we will take your software skills to the next level by focusing on the specifics needed to move code into a production setting.

These specifics will focus on:

* Handling errors
* Writing tests and logs
* Model drift
* Automated vs. non-automated retraining

With these skills in your toolkit, you will be ready to take on the project for this course, as well as contribute to your team's production codebase!


# Catching Errors

you saw how to use try/ except blocks in order to catch errors. There are actually a lot of different considerations to errors, so if you would like to learn more, the link below provides some additional resources.


Catching errors in Python code is essential for writing robust and reliable applications. One common method for handling errors is using try-except blocks, which allow you to catch exceptions that occur during the execution of your code and handle them gracefully.

```python
try:

    result = 10 / 0  # Attempting division by zero

except ZeroDivisionError as e:

    print("Error:", e)

    result = None
```

In this example, a ZeroDivisionError is raised when attempting to divide by zero. By wrapping the problematic code within a try block and specifying the exception type to catch in the except block, we can gracefully handle the error and prevent it from crashing the program.


Additionally, you can use the else block in combination with try-except to execute code only if no exceptions are raised.

```python
try:

    result = int(input("Enter a number: "))

except ValueError:

    print("Invalid input. Please enter a valid integer.")

else:

    print("You entered:", result)
```

Here, the code attempts to convert user input to an integer. If successful, the input is printed; otherwise, a ValueError is caught, and an error message is displayed.


Furthermore, you can utilize the finally block to execute cleanup code, regardless of whether an exception occurs or not.

```python
try:

    file = open("example.txt", "r")

    content = file.read()

except FileNotFoundError:

    print("File not found.")

else:

    print("File content:", content)

finally:

    if file:

        file.close()  # Ensuring file is closed even if an exception occurs
```

In this snippet, the file is opened for reading, and its content is displayed. If the file is not found, a FileNotFoundError is caught. Regardless of the outcome, the file is closed in the finally block to ensure proper resource management.


Handling errors effectively in Python enhances the reliability and maintainability of your codebase. By employing try-except blocks, you can anticipate and gracefully handle exceptions, ensuring smooth execution of your programs even in the face of unexpected issues.

https://docs.python.org/3/tutorial/errors.html


# Tests

Testing your code is essential before deployment. It helps you catch errors and faulty conclusions before they make any major impact. Today, employers are looking for data scientists with the skills to properly prepare their code for an industry setting, which includes testing their code.

## Testing and data science

Problems that could occur in data science aren’t always easily detectable; you might have values being encoded incorrectly, features being used inappropriately, or unexpected data breaking assumptions.
To catch these errors, you have to check for the quality and accuracy of your analysis in addition to the quality of your code. Proper testing is necessary to avoid unexpected surprises and have confidence in your results.
Test-driven development (TDD): A development process in which you write tests for tasks before you even write the code to implement those tasks.
Unit test: A type of test that covers a “unit” of code—usually a single function—independently from the rest of the program.

Resources
* Four Ways Data Science Goes Wrong and How Test-Driven Data Analysis Can Help: Blog Post(opens in a new tab): https://www.predictiveanalyticsworld.com/machinelearningtimes/four-ways-data-science-goes-wrong-and-how-test-driven-data-analysis-can-help/6947/
* Ned Batchelder: Getting Started Testing: Slide Deck(opens in a new tab) and Presentation Video: https://speakerdeck.com/pycon2014/getting-started-testing-by-ned-batchelder, https://www.youtube.com/watch?v=FxSsnHeWQBY

## Unit Tests

We want to test our functions in a way that is repeatable and automated. Ideally, we'd run a test program that runs all our unit tests and cleanly lets us know which ones failed and which ones succeeded. Fortunately, there are great tools available in Python that we can use to create effective unit tests!

Unit Testing: Advantages and Disadvantages
The advantage of unit tests is that they are isolated from the rest of your program, and thus, no dependencies are involved. They don't require access to databases, APIs, or other external sources of information. However, passing unit tests isn’t always enough to prove that our program is working successfully. To show that all the parts of our program work with each other properly, communicating and transferring data between them correctly, we use integration tests. In this lesson, we'll focus on unit tests; however, when you start building larger programs, you will want to use integration tests as well.

To learn more about integration testing and how integration tests relate to unit tests, see Integration Testing(opens in a new tab). That article contains other very useful links as well.
https://www.fullstackpython.com/integration-testing.html

## Unit Tests Tools

To install `pytest`, run `pip install -U pytest` in your terminal. You can see more information on getting started here(opens in a new tab). https://docs.pytest.org/en/latest/getting-started.html

* Create a test file starting with test_.
* Define unit test functions that start with `test_` inside the test file.
* Enter `pytest` into your terminal in the directory of your test file and it detects these tests for you.

`test_` is the default; if you wish to change this, you can learn how in this `pytest` configuration(opens in a new tab). https://docs.pytest.org/en/latest/example/pythoncollection.html

In the test output, periods represent successful unit tests and Fs represent failed unit tests. Since all you see is which test functions failed, it's wise to have only one assert statement per test. Otherwise, you won't know exactly how many tests failed or which tests failed.

Your test won't be stopped by failed assert statements, but it will stop if you have syntax errors.

Launching tests for ML models in production settings will be covered in more detail throughout this lesson, as well as in the project. However, it is also often done using cloud-based software; some additional resources can be found here on testing using Google's cloud-based systems(opens in a new tab). https://developers.google.com/machine-learning/testing-debugging/pipeline/deploying?hl=es-419