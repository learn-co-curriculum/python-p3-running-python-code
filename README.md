# Running Python Code

## Learning Goals

- Run Python code from a file
- Log output to the terminal
- Run Python code from the interpreter
- Run ??? tests in Python

## Introduction

In this lesson, you'll get some practice running Python code, and see a few
different ways to check what your code is doing. Make sure to code along to get
comfortable in this new environment!

## Creating a Python Application

Let's dive right in. To get started on any new Python application, the first
thing we need is a file. Create a new file in this lab directory called
`app.py`. In this file, add the following:

```python
# app.py
print("Hello world!")
```

`print()` is a built-in Python function that will output a string of text to the
terminal. It's the Python equivalent of `console.log()` in JavaScript. It will
print the string "Hello world!" along with a line break at the end.

The line above `print()` is a Python comment. In Python, any line that starts with
a `#` won't be executed by the interpreter. This is the Python equivalent of
`//` in JavaScript.

## Running Python Applications

Unlike JavaScript, you won't be running Python applications in the browser.
Instead, you'll need to use the Python interpreter to run your code from the
terminal. You can check which version of Ruby you're using with this command:

```console
$ python --version
Python 3.8.13
```

To run the application, enter the command `python filename.py`, where
`filename.py` is the relative path to the file you'd like to run:

```console
$ python app.py
Hello world!
```

Congrats on running your first Python application! 🎉

## Displaying Data with "print()"

Now that we have a place to write some code, let's explore a few of Python's
built-in options for displaying data in different ways.

### Standard print() Statements

By default, `print()` includes a newline character at the end of your string.
Try entering several `print()` statements in a row in `app.py`:

```python
# app.py
print("Hello world!")
print("Hello sun!")
print("Hello sky!")
```

What do you see when you execute `app.py` from the command line?

```console
$ python app.py
Hello world!
Hello sun!
Hello sky!
```

### Choosing your own print() Ending

Let's say you're writing a full paragraph and don't need a newline character
after every sentence. `print()` can accommodate that through its optional `end`
parameter. Try modifying your `print()` statements as follows:

```python
# app.py
print("Hello world!", end="")
print("Hello sun!", end=" ")
print("Hello sky!", end="\n")
```

What do you see when you execute `app.py` from the command line with these new
`end` strings?

```console
$ python app.py
Hello world!Hello sun! Hello sky!
```

`end` can be a string of any length, including special characters like the
newline `\n`.

## Exploring Python with the Python Interpreter

Python comes with a command line interpreter (often called the "Python shell")
for running a Python REPL (read-evaluate-print-loop) in the terminal, which
provides similar functionality to the browser console that you're familiar with
from JavaScript. Using the Python shell is a great way to quickly test out some
code, or check your syntax, without needing to run an entire application.

To use the Python shell, go into the terminal and enter `python`:

```console
$ python
Python 3.8.13 (default, Jun  2 2022, 15:59:12)
[Clang 13.1.6 (clang-1316.0.21.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

This gives you a prompt where you can enter Python code. Try entering in
`print("Hello Python shell")`:

```console
$ python
Python 3.8.13 (default, Jun  2 2022, 15:59:12)
[Clang 13.1.6 (clang-1316.0.21.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello Python shell")
Hello Python shell
```

Try running a few more expressions in the Python Shell:

```console
>>> first_number = 7
>>> first_number
7
>>> print(first_number)
7
```

In the code above, we've declared a **local variable** called `first_number` and
assigned it a value of `7`. Note the difference between just entering
`first_number` and entering `puts first_number`: in the first case, the **return
value** is `7`, in the second case, the **return value** is `nil`. Using the
correct return value will become more important once we start writing methods,
so remember: the `puts` method **always returns `nil`**.

> In Ruby, it's convention to use underscores (\_) to separate words in
> variables. This is referred to as **snake case** (as opposed to **camel
> case**, which is the convention in JavaScript).

You can exit IRB by typing `exit`, or pressing `ctrl + d`.

## Running RSpec Tests

All the lessons in the Ruby curriculum use the RSpec library for testing your
Ruby code.

In this lesson, you'll see a `spec` folder with two files, `app_spec.rb` and
`spec_helper.rb`. The `spec_helper.rb` file does a bit of general-purpose setup
for our tests. `app_spec.rb` is where we've defined tests specifically for this
lesson.

RSpec is a Ruby gem (the Ruby equivalent of a npm package) that provides a
domain-specific language, or DSL, that makes it very nice way to write tests.
The RSpec library was installed on your system as part of installing the
`learn-co` gem earlier in the program.

Let's take one of these tests as an example to see RSpec's DSL:

```rb
it 'outputs the string "Pass this test, please." using the print method' do
  expect { load 'app.rb' }.to output(a_string_including("Pass this test, please.")).to_stdout
end
```

All of this is valid Ruby code, but it should read (more or less) like English:

> Expect that loading the `app.rb` file will output a string including the text
> "Pass this test, please." to the terminal's standard output.

Clear out the code in `app.rb` to start from scratch so we can try getting these
tests to pass.

To run the tests, you can use either the `rspec` command or `learn test`. Run
the command, then take a moment to study the output:

```console
$ learn test

the program
  has a file app.rb
  outputs the string "Hello World!" using the puts method (FAILED - 1)
  outputs the string "Pass this test, please." using the print method (FAILED - 2)
  outputs the array [1, 2, 3] using the p method (FAILED - 3)

Failures:

  1) the program outputs the string "Hello World!" using the puts method
     Failure/Error: expect { load 'app.rb' }.to output(a_string_including("Hello World!\n")).to_stdout

       expected block to output a string including "Hello World!\n" to stdout, but output nothing
       Diff:
       @@ -1 +1 @@
       -(a string including "Hello World!\n")
       +""

     # ./spec/app_spec.rb:10:in `block (2 levels) in <top (required)>'

  2) the program outputs the string "Pass this test, please." using the print method
     Failure/Error: expect { load 'app.rb' }.to output(a_string_including("Pass this test, please.")).to_stdout

       expected block to output a string including "Pass this test, please." to stdout, but output nothing
       Diff:
       @@ -1 +1 @@
       -(a string including "Pass this test, please.")
       +""

     # ./spec/app_spec.rb:14:in `block (2 levels) in <top (required)>'

  3) the program outputs the array [1, 2, 3] using the p method
     Failure/Error: expect { load 'app.rb' }.to output(a_string_including("[1, 2, 3]\n")).to_stdout

       expected block to output a string including "[1, 2, 3]\n" to stdout, but output nothing
       Diff:
       @@ -1 +1 @@
       -(a string including "[1, 2, 3]\n")
       +""

     # ./spec/app_spec.rb:18:in `block (2 levels) in <top (required)>'

Finished in 0.04406 seconds (files took 0.28088 seconds to load)
4 examples, 3 failures

Failed examples:

rspec ./spec/app_spec.rb:6 # the program outputs the string "Hello World!" using the puts method
rspec ./spec/app_spec.rb:13 # the program outputs the string "Pass this test, please." using the print method
rspec ./spec/app_spec.rb:17 # the program outputs the array [1, 2, 3] using the p method
```

RSpec provides all kinds of useful information about what went right and wrong
with our code, so make sure to spend your time reading all the output here! It
will tell you:

- Which tests passed/didn't passed
- Why each failing test failed (the difference between the expected output and
  the actual output)
- The line number of the failing test

You can also use the `--fail-fast`, or `--f-f` flag to tell RSpec to stop running
after the first failing test. This technique is helpful for focusing your attention
on one problem at a time:

```console
$ learn test --f-f

the program
  has a file app.rb
  outputs the string "Hello World!" using the puts method (FAILED - 1)

Failures:

  1) the program outputs the string "Hello World!" using the puts method
     Failure/Error: expect { load 'app.rb' }.to output(a_string_including("Hello World!\n")).to_stdout

       expected block to output a string including "Hello World!\n" to stdout, but output nothing
       Diff:
       @@ -1 +1 @@
       -(a string including "Hello World!\n")
       +""

     # ./spec/app_spec.rb:10:in `block (2 levels) in <top (required)>'

Finished in 0.0389 seconds (files took 0.24407 seconds to load)
2 examples, 1 failure

Failed examples:

rspec ./spec/app_spec.rb:6 # the program outputs the string "Hello World!" using the puts method
```

## Instructions

To finish this lab, use the `puts`, `print`, and `p` methods in the `app.rb` file
as described by the tests:

- Use `puts` to display the string `"Hello World!"`
- Use `print` to display the string `"Pass this test, please."`
- Use `p` to display the array `[1,2,3]`

Using `learn test` will run the tests and sync your progress with GitHub and
Canvas. When your tests are all passing, the lab is complete!

## Conclusion

This lesson covered a good amount of material, but now you should be familiar
with running code in a Ruby environment, and using tools like IRB and RSpec
as well as built-in methods like `puts` to understand what happens when your
Ruby code is running. You'll need all these tools going forward, so make sure
to get practice with all of them as you progress through this phase!

## Resources

- [Python print() function](https://www.w3schools.com/python/ref_func_print.asp)
- [Python Getting Started](https://www.w3schools.com/python/python_getstarted.asp)
- [pytest Documentation](https://docs.pytest.org/en/7.1.x/)