---
title: 01 - Python: Fundamentals
layout: post
author: dylan
permalink: /01---python:-fundamentals/
source-id: 1MZYaoBdwkzqXAoVG8UrclBnwXBJO7m3H7E7D59jLhQs
published: true
---
**Music**

* [Concentration | Programming Music 001 (part 1)](https://www.youtube.com/watch?v=svngvOLPd5E)

**Resources**

* [Python Glossary](http://www.codecademy.com/glossary/python#class)

* [Python Term Overlaps](http://eli.thegreenplace.net/2012/03/30/python-objects-types-classes-and-instances-a-glossary)

* [Flashcards: Python ](https://quizlet.com/14957313/python-terminology-flash-cards/)[Terminology](https://www.google.com/url?q=https%3A%2F%2Fquizlet.com%2F14957313%2Fpython-terminology-flash-cards%2F&sa=D&sntz=1&usg=AFQjCNFkVbdmAy1XQkVIS8bnfDkg5r_jXg)

* [Python Example Index](http://www.tutorialspoint.com/python/python_dictionary.htm)

* [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_0.jpg)

Placeholder

* * *


# Console

* * *


### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_1.jpg) = Programming...

* n/a

    * A Tron program represents the concept of programming.

* They can code up statistical models

![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_2.jpg)

* * *


# Console

* * *


### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_3.png) = Shell Commands...

* There Is a talking shell on a pole out front telling people what to do. 

    * A commanding shell represents shell commands. 

### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_4.png) = Comments...

* There are symbols # and ""” written all over this as two people complain about the hours.

    * Commenting on an hours of operation sign represents comments. 

* #

* ""”

<table>
  <tr>
    <td></td>
  </tr>
</table>


### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_5.jpg)  = Printing...

* [Print Formatting Examples](https://pyformat.info/)

* The front desk area is a FedEx Kinkos with copy machines you can print to. 

    * The printer represents the concept of printing. 

* print(var1, var2) #Comma line method | In Python 3 it's print(i,end=" ")

* print('\n' * 5) #Prints 5 empty lines

* print("this dog is {} inches long and name d {}".format(var1, var2, var3) #Bracket printing method

* print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2) # Percent printing method

* %f will print floats

* %c is for ints

<table>
  <tr>
    <td></td>
  </tr>
  <tr>
    <td>
This will zero pad the 1's</td>
  </tr>
  <tr>
    <td>
Dates</td>
  </tr>
</table>


### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_6.jpg) = Escaping...

* There is an escape hatch like a dog door down below. A con artist cat hops through it. The handle looks a bit like a backslash \ that could get out of the building through the wall. 

    * An escape hatch represents the concept of escaping.

### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_7.jpg) = Concatenation...

* Working the desk a cat who is a slimy con artists car salesman. 

    * A cat car salesman represents concatenation. 

* var1 = "Camelot"

* var2 = "place"

* print(var1 + " " + var2) #Concatenation method

* print "Grades:", grades

### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_8.jpg)![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_9.jpg) = Tabbing & White Space...

* There is a stack of white printer paper on the counter with a Tab soda resting on top. 

    * Reams of white paper represent whitespace.

    * Tab soda represent tabbing.

* In Python whitespace matters.

<table>
  <tr>
    <td>"Return", one tab in will return a squared list (correct)</td>
    <td>“Return”, two tabs in will return a single scalar squared (incorrect)</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
  </tr>
</table>


![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_10.jpg)

* * *


# Namespaces

* * *


### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_11.jpg) = Namespaces...

* Ralph's job is to ensure that anybody who goes up the steps has a name badge on. 

    * And name tag represents a namespace. 

* Your name spaces holds the functions, classes and vars your module has access to. 

* In Python, each package, module, class, function and method function owns a "namespace" in which variable names are resolved. 

* There's also a **global namespace** that's used if the name isn't in the local namespace.

* To use libraries you have to load them into you name space.

#### + Locals & Globals...

* Pythonistas might also say that functions have their own namespace. This means Python looks first in the namespace of the function to find variable names when it encounters them in the function body. Python includes a couple of functions that let us look at our namespaces.

<table>
  <tr>
    <td>Locals</td>
    <td>Globals</td>
  </tr>
  <tr>
    <td></td>
    <td>Locals() prints local variables
Globals() print global variables

The built in globals function returns a dictionary containing all the variable names Python knows about. </td>
  </tr>
</table>


### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_12.png) =  Variables...

* Ralph is holding a magic 8-ball in his right hand.

    * A Magic 8-Ball represents the concept of variables. 

* A variable is any characteristics, number, or quantity that can be measured or counted. 

* Age, sex, business income or country of birth are variables because the value may change over time. 

<table>
  <tr>
    <td>Variable's Scope</td>
    <td>Variable’s Lifetime</td>
  </tr>
  <tr>
    <td>
Python’s scope rule is that variable creation always creates a new local variable but variable access (including modification) looks in the local scope and then searches all the enclosing scopes to find a match

Scope Rules cause a "NameError"</td>
    <td>
The namespace created for our function foo is created from scratch each time the function is called and it is destroyed when the function ends.</td>
  </tr>
</table>


### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_13.gif) = State...

* He puts the 8 ball in his mouth and swallowed the whole thing.

    * Ralph dressed as a state represent the concept of states. 

* State is termed used to refer to this current variable's value. 

### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_14.jpg) = Mutation...

* In Ralph's other hand is a toy rockstead who is telling people that he Is depressed because he used to be a human. 

    * A toy rockstead represents the concept of a mutation. 

* Mutation is the process the variable goes through as it changes. 

* An un-immutable variable is a variable that cannot change. 

#### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_15.jpg) + Control Flow…

* n/a

    * He can't control his nose running everywhere. 

* It's a reference for controlling the process of variable state mutation through, loops, conditionals, functions, etc. 

![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_16.jpg)

* * *


# Pythonic Style

* * *


### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_17.jpg) = Style Guide...

* [Googles Python Style Guide ](https://google.github.io/styleguide/pyguide.html)

* n/a

    * A trendy guide camel represents the python style guide.

### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_18.png)![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_19.jpg)** **= Being Pythonic...

* [Pythonic Video](https://www.youtube.com/watch?v=x3v9zMX1s4s&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=17)

* n/a

    * A duck represents duck typing.

    * A checkbook represents not filling code with checks.

<table>
  <tr>
    <td>Duck Typing</td>
    <td>Asking Forgiveness, Not Permission (EAFP)</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>If an object walks, like a duck and talks like a duck, then it's a duck. Regardless of what the returned object type is.</td>
    <td>Don’t fill your code with permission checks to see if something will work, just assume it does then fix it if it doesn't.</td>
  </tr>
</table>


### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_20.jpg) = PyLint...

* [Integrate PyLint w/ PyCharm](http://softwaretester.info/integrate-pylint-in-pycharm/)

* n/a

    * Belly button lint represents the utility PyLint.

* pylint is a tool for finding bugs and style problems in Python source code. It finds problems that are typically caught by a compiler for less dynamic languages like C and C++. Because of the dynamic nature of Python, some warnings may be incorrect; however, spurious warnings should be fairly infrequent.

### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_21.png) = Upper Case...

* [Python Naming Conventions](http://visualgit.readthedocs.org/en/latest/pages/naming_convention.html) | [Googles Python Sytle Guide](https://google.github.io/styleguide/pyguide.html)

* n/a

    * An upper staircase represents uppercase words.

* + GLOBAL_CONSTANT_NAME

### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_22.png)![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_23.jpg) = Camel Case...

* The camel is helping hold up the staircase. 

    * A camel standing under a staircase represents camelcase.

* + ClassName

* + ExceptionName

### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_24.png) = Lower Case...

* n/a

    * The lower part of a staircase represents lower case. 

* + module_name

* + package_name 

* + method_name

* + function_name

* + global_var_name

* + instance_var_name

* + function_parameter_name

* + local_var_name

![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_25.png)

* * *


# Operators

* * *


### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_26.png)![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_27.jpg) = Operator Precedence Order...

* [Python Operators Precedence Example](http://www.tutorialspoint.com/python/operators_precedence_example.htm)

* All of the people below are work the phones and sitting on the steps. 

    * Phone operators represent the concept of operators. 

    * A phone order catalogue for princes represents operator precedence order

* The following table lists all operators from highest precedence to lowest.

<table>
  <tr>
    <td>Operator</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>**</td>
    <td>Exponentiation (raise to the power)</td>
  </tr>
  <tr>
    <td>~ + -</td>
    <td>Ccomplement, unary plus and minus (method names for the last two are +@ and -@)</td>
  </tr>
  <tr>
    <td>* / % //</td>
    <td>Multiply, divide, modulo and floor division</td>
  </tr>
  <tr>
    <td>+ -</td>
    <td>Addition and subtraction</td>
  </tr>
  <tr>
    <td>>> <<</td>
    <td>Right and left bitwise shift</td>
  </tr>
  <tr>
    <td>&</td>
    <td>Bitwise 'AND'td></td>
  </tr>
  <tr>
    <td>^ |</td>
    <td>Bitwise exclusive `OR' and regular `OR'</td>
  </tr>
  <tr>
    <td><= < > >=</td>
    <td>Comparison operators</td>
  </tr>
  <tr>
    <td><> == !=</td>
    <td>Equality operators</td>
  </tr>
  <tr>
    <td>= %= /= //= -= += *= **=</td>
    <td>Assignment operators</td>
  </tr>
  <tr>
    <td>is is not</td>
    <td>Identity operators</td>
  </tr>
  <tr>
    <td>in not in</td>
    <td>Membership operators</td>
  </tr>
  <tr>
    <td>not or and</td>
    <td>Logical operators</td>
  </tr>
</table>


### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_28.jpg)![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_29.jpg) = Arithmetic Operators...

* [Arithmetic Operators](http://www.tutorialspoint.com/python/arithmetic_operators_example.htm) | [Modulo](https://www.youtube.com/watch?v=b5cb_nfDyyM)

* n/a

    * Brahmagupta represents arithmetic. 

    * A net with apples represents Modulo

<table>
  <tr>
    <td>+ % (Modulo)
5 = 5%14, NaN = 5%0, 0 = 5%1</td>
    <td></td>
  </tr>
  <tr>
    <td>
% (modulus) In programming the modulo operation return the remainder of from a division problem. </td>
    <td>
a = Apples
n = Nets
The farmer will only accept nets (n) with n number of apples (a). Whatever is left over is the modulo. </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
  </tr>
</table>


### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_30.jpg)![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_31.jpg)![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_32.jpg) = Bitwise Operators...

* [Python Bitwise Operators](http://www.tutorialspoint.com/python/bitwise_operators_example.htm)

* n/a

    * This kid drinking a Budweiser represents bitwise operators. 

* Bitwise is a base 2 systems so…

<table>
  <tr>
    <td>Base 10</td>
    <td>Base 2</td>
  </tr>
  <tr>
    <td>100 = 1, 101 = 10, 102= 100, 103 = 1000</td>
    <td>20 = 1, 21 = 2, 22 = 4, 23 = 8, 24 = 16</td>
  </tr>
  <tr>
    <td></td>
    <td>Contrary to counting in base 10, where each decimal place represents a power of 10, each place in a binary number represents a power of two (or a bit)</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>
The bitwise AND (&) operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if the corresponding bits of both numbers are 1.</td>
    <td>
The bitwise OR (|) operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if either of the corresponding bits of either number are 1</td>
  </tr>
</table>


### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_33.jpg)![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_34.jpg) = Comparison (Relational) Operators...

* [Python Comparison Operators](http://www.tutorialspoint.com/python/comparison_operators_example.htm)

* Next are two identical twins sitting across from each other. One is from a before workout photo and one is from an after work at photo.

    * Before and after sisters represent comparison operators.

<table>
  <tr>
    <td></td>
    <td>Description</td>
    <td>Example</td>
  </tr>
  <tr>
    <td>==</td>
    <td>If the values of two operands are equal, then the condition becomes true.</td>
    <td>(a == b) is not true.</td>
  </tr>
  <tr>
    <td>!=</td>
    <td>If values of two operands are not equal, then condition becomes true.</td>
    <td></td>
  </tr>
  <tr>
    <td><></td>
    <td>If values of two operands are not equal, then condition becomes true.</td>
    <td>(a <> b) is true. This is similar to != operator.</td>
  </tr>
  <tr>
    <td>></td>
    <td>If the value of left operand is greater than the value of right operand, then condition becomes true.</td>
    <td>(a > b) is not true.</td>
  </tr>
  <tr>
    <td><</td>
    <td>If the value of left operand is less than the value of right operand, then condition becomes true.</td>
    <td>(a < b) is true.</td>
  </tr>
  <tr>
    <td>>=</td>
    <td>If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.</td>
    <td>(a >= b) is not true.</td>
  </tr>
  <tr>
    <td><=</td>
    <td>If the value of left operand is less than or equal to the value of right operand, then condition becomes true.</td>
    <td>(a <= b) is true.</td>
  </tr>
</table>


### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_35.jpg)![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_36.jpg) = Assignment Operators...

* [Python Assignment Operators Example](http://www.tutorialspoint.com/python/assignment_operators_example.htm)

* Below him is it guy whose face you can't see because he's covered in assignments that you supposed to do. 

    * The guy covered in work papers represents the assignment operators 

<table>
  <tr>
    <td>Operator</td>
    <td>Description</td>
    <td>Example</td>
  </tr>
  <tr>
    <td>=</td>
    <td>Assigns values from right side operands to left side operand</td>
    <td>c = a + b assigns value of a + b into c</td>
  </tr>
  <tr>
    <td>+= Add AND</td>
    <td>It adds right operand to the left operand and assign the result to left operand</td>
    <td>c += a is equivalent to c = c + a</td>
  </tr>
  <tr>
    <td>-= Subtract AND</td>
    <td>It subtracts right operand from the left operand and assign the result to left operand</td>
    <td>c -= a is equivalent to c = c - a</td>
  </tr>
  <tr>
    <td>*= Multiply AND</td>
    <td>It multiplies right operand with the left operand and assign the result to left operand</td>
    <td>c *= a is equivalent to c = c * a</td>
  </tr>
  <tr>
    <td>/= Divide AND</td>
    <td>It divides left operand with the right operand and assign the result to left operand</td>
    <td>c /= a is equivalent to c = c / ac /= a is equivalent to c = c / a</td>
  </tr>
  <tr>
    <td>%= Modulus AND</td>
    <td>It takes modulus using two operands and assign the result to left operand</td>
    <td>c %= a is equivalent to c = c % a</td>
  </tr>
  <tr>
    <td>**= Exponent AND</td>
    <td>Performs exponential (power) calculation on operators and assign value to the left operand</td>
    <td>c **= a is equivalent to c = c ** a</td>
  </tr>
  <tr>
    <td>//= Floor Division</td>
    <td>It performs floor division on operators and assign value to the left operand</td>
    <td>c //= a is equivalent to c = c // a</td>
  </tr>
</table>


### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_37.jpg)![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_38.jpg) = Identity Operators...

* [Python Identity Operators Example](http://www.tutorialspoint.com/python/identity_operators_example.htm)

* Below him is the guy from Bourne Identity he's holding a gun to the pile of papers towing the man to reveal himself.

    * The guy from Bourne Identity represents the identity operators.

* Identity operators compare the memory locations of two objects. There are two Identity operators.

<table>
  <tr>
    <td>Operator</td>
    <td>Description</td>
    <td>Example</td>
  </tr>
  <tr>
    <td>is</td>
    <td>Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.</td>
    <td>x is y, here is results in 1 if id(x) equals id(y).</td>
  </tr>
  <tr>
    <td>is not</td>
    <td>Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.</td>
    <td>x is not y, here is not results in 1 if id(x) is not equal to id(y).</td>
  </tr>
</table>


### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_39.jpg)![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_40.jpg) = Membership Operators...

* [Python Membership Operators Example](http://www.tutorialspoint.com/python/membership_operators_example.htm)

* Behind him is this Roger type gym membership sales guy. He recommends to the person on his phone that they buy a membership to work in progress. 

    * Roger selling gym memberships represents a membership operator.

* Membership operators test for membership in a sequence, such as strings, lists, or tuples. 

<table>
  <tr>
    <td>Operator</td>
    <td>Description</td>
    <td>Example</td>
  </tr>
  <tr>
    <td>in</td>
    <td>Evaluates to true if it finds a variable in the specified sequence and false otherwise.</td>
    <td>x in y, here in results in a 1 if x is a member of sequence y.</td>
  </tr>
  <tr>
    <td>not in</td>
    <td>Evaluates to true if it does not finds a variable in the specified sequence and false otherwise.
</td>
    <td>x not in y, here not in results in a 1 if x is not a member of sequence y.</td>
  </tr>
</table>


### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_41.jpg)![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_42.jpg)  = Logical Operators...

* [Python Logical Operators Example](http://www.tutorialspoint.com/python/logical_operators_example.htm)

* At the very bottom of the steps is spok. He Is welcoming everybody to the steps with his traditional "live long and prosper ".

    * Spock represents a logical operator. 

<table>
  <tr>
    <td>Operator</td>
    <td>Description</td>
    <td>Example</td>
  </tr>
  <tr>
    <td>and Logical AND</td>
    <td>If both the operands are true then condition becomes true.</td>
    <td>(a and b) is true.</td>
  </tr>
  <tr>
    <td>or Logical OR</td>
    <td>If any of the two operands are non-zero then condition becomes true.</td>
    <td>(a or b) is true.</td>
  </tr>
  <tr>
    <td>not Logical NOT</td>
    <td>Used to reverse the logical state of its operand.</td>
    <td>Not(a and b) is false.</td>
  </tr>
</table>


![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_43.jpg)

![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_44.jpg)

* * *


# Types

* * *


## Top of Steps

### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_45.jpg) = Types...

* [List of Python Data Types](https://docs.python.org/2/library/datatypes.html)

* The Geico gecko is sitting on the floor having a conversation with people as they come to the top of the steps. While he types an interesting story on his typewriter his skin color keeps changing along with his moods. 

    * The typewriter represents types.  

* Types: Integers, Strings, Lists, Tuples and Dictionaries, etc...

<table>
  <tr>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
  </tr>
</table>


### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_46.png) = Casting vs. Coercion…

* [Python Casting](http://usingpython.com/python-casting/)

* n/a

    * The color changing gecko represents coercion.

    * A castrated gecko represents casting.

* When you multiply an int and a float python will coerce the int, into a float, then do the math as if they were both floats.

<table>
  <tr>
    <td></td>
    <td>Cast is explicit. 
Coerce is implicit.</td>
  </tr>
</table>


### = Abstract Data Types (ADTs)...

* An Abstract Data Type is a data type whose properties, domain and operations are independent of any particular implementation

<table>
  <tr>
    <td>ADT data types come with 4 operations.</td>
    <td></td>
  </tr>
  <tr>
    <td>Constructor
Creates a new instance</td>
    <td>Iterator
Allows us to process all of the items in a data structure sequentially.</td>
  </tr>
  <tr>
    <td>Observer
Lets us look at a data value without changing it.</td>
    <td>Transformer
Change it to state of one or more data values of an instance. </td>
  </tr>
</table>


![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_47.jpg)

* * *


# Strings

* * *


### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_48.jpg) = String Literals...

* [Example Database (Strings)](http://www.tutorialspoint.com/python/python_strings.htm)

* In the first seat Lindsay Stringham is sitting on her knees jamming out for the grim reaper.

    * Lindsay string that represents the concept of strings.

    * Littering her bow represents the concept of string literals. 

### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_49.jpg) = Unicode...

* n/a

    * A unicorn represents unicode.

* There is also 'u' for unicode >> u ‘item1’, u ‘item2’ etc…

* Unicode is an international encoding standard for use with different languages and scripts, by which each letter, digit, or symbol is assigned a unique numeric value that applies across different platforms and programs.

### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_50.png) = Repr...

* Next to her is the angel of death who snatches up the unicorn and take her to the afterlife.

    * The Grim Reaper represents the concept of Repr.

* The goal of str is to print something readable, the goal repr is to print something you could cut and past back into python and use.  

<table>
  <tr>
    <td></td>
  </tr>
</table>


### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_51.jpg) = Raw Input...

* There is a community bowl of raw nuts for anyone who wants them on this table. 

    * A bowl of raw nuts represents raw input.

![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_52.jpg)

* * *


# Digits

* * *


### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_53.jpg) = Ints...

* [Example Database (Numbers)](http://www.tutorialspoint.com/python/python_numbers.htm)

* The sesame street gang is sitting at the top of the table working on a conference about numbers "Number Con"

    * Sesame street teaching numbers represent ints.

* An integer is just a number without a decimal part (for instance, -17, 0, and 42 are all integers, but 98.6 is not).

### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_54.jpg) = Floats...

* They are working on a magic trick where they hold the numbers up like in the picture above  but then add a period with the other hand then walk away from them and they stay floating in the air.

    * The numbers floating in air represent floats. 

### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_55.png) = Boolean Digits…

* n/a

    * A ghost sheet over a floating number represents a boolean digit.

* Booleans act like the numbers 0 and 1

    * print 1+f  # 1

    * print 1+t  # 2

### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_56.jpg) = Time Series…

* n/a

    * The guy from Quantum Leap represents the time series data type.

<table>
  <tr>
    <td></td>
  </tr>
</table>


![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_57.jpg)

* * *


# Lists

* * *


### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_58.gif) = Lists...

* [Example Database (Lists)](http://www.tutorialspoint.com/python/python_lists.htm)

* George has been given a long list spread out all the way down the table of work to do.

    * A long list represents the concept of list. 

<table>
  <tr>
    <td></td>
  </tr>
</table>


### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_59.jpg)![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_60.jpg) = Tuples...

* George Costanza is furious about this giant phone bill he got.

    * Toupee represents tuples.

* Tuples are immutable lists.

#### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_61.jpg) + Zip…

* n/a

    * Having your zipper down represents the zip function. 

* The zip function will make pairs of tuples out of lists.

### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_62.jpg)![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_63.jpg) = Dictionary...

* [Great Link](http://book.pythontips.com/en/latest/collections.html)

* This guy is a dick. He just sits with his feet up in the middle of the room telling everyone how smart he is because he has read the whole dictionary.

    * A dick guy represents a dictionary.

<table>
  <tr>
    <td></td>
  </tr>
</table>


#### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_64.jpg) + Hash Tables...

* n/a

    * Hashtag fingers represent a hash table. 

* A python dictionary uses a hash table, which is a data structure that uses a **hash function** to compute an index into an array of **buckets or slots**, from which the desired value can be found.

<table>
  <tr>
    <td></td>
    <td>When a function is used to make an index it does not matter the order of the index in regards to speed, one location is not any faster to retrieve than another. 
</td>
  </tr>
</table>


#### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_65.png) + Manual Python Hashing…

* n/a

<table>
  <tr>
    <td></td>
    <td>b  = size of hash table AKA number of buckets</td>
  </tr>
  <tr>
    <td></td>
    <td>ord = Ordinal
We also need a way to turn a string into a number </td>
  </tr>
  <tr>
    <td></td>
    <td>chr = Character
The inverse of this is called character </td>
  </tr>
</table>


### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_66.jpg) =  Enumerate...

* Elmer Fudd has numb fingers when he touches a rake that buggs bunny replaced his gun with. 

    * Elmer Fudd represents the concept of enumeration. 

* Enumerate works by supplying a corresponding index to each element in the list that you pass it. Each time you go through the loop, index will be one greater, and item will be the next item in the sequence. It's very similar to using a normal for loop with a list, except this gives us an easy way to count how many items we've seen so far.

### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_67.jpg) = Range...

* The Lone Ranger gave for Elmer Fudd the workload.

    * Lone Ranger represents the concept of range. 

### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_68.jpg) = List Slicing...

* The Lone Ranger's way to eating pizza is to first cutting it into slices. 

    * Slices of a rabbit meat pizza represent list slicing. 

* The start describes where the slice **starts (inclusive)**, end is where it **ends (exclusive)**, and **stride** describes the **space between** items in the sliced list. 

* For example, a stride of 2 would select every other item from the original list to place in the sliced list.

![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_69.jpg)

* * *


# Sets & Collections

* * *


### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_70.jpg) = Sets...

* n/a

    * The table of fine China represents sets.

* There is no order function

* Sets use this notation: {}

* Every item in the set can only occur once.

* The next table over has a full dinner set waiting for the day. 

### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_71.jpg) = Collections...

* [Collections Info](https://docs.python.org/2/library/collections.html)

* n/a

    * Beanie Babies represent the concept of collections. 

### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_72.jpg)![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_73.png) = Combinations & Permutations...

* n/a

    * This Barber who does perms represents the concept of permutations.

    * Combo represents combinations.

![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_74.jpg)

* * *


# Numpy

* * *


### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_75.gif)![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_76.jpg) = Numpy Arrays...

* n/a

    * Pinky the dentist numbing a patient with liquid pie represents numpy arrays.

* NumPy lets Python work like Matlab to do scientific computing.

![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_77.png)![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_78.jpg)** = Linear Algebra**…

* Pinky is on stilts to reach the patients and is wearing the merchants turbin. 

    * The Agraba merchant selling excel represents Linear Algebra. 

    * The stilts represent the concept of linearity. 

* Useful linear algebra methods like, fourier transforms and random number capability.

### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_79.jpg) = Arrays…

* n/a

    * An air raid represents numpy arrays.

* A powerful N-dimensional array object

### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_80.jpg)![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_81.jpg) = Broadcasting Functions…

* n/a

    * A lit "ON AIR" broadcast sign represents broadcasting.

    * Neo represents the concept of a matrix. 

* Sophisticated (broadcasting) functions

* Broadcasting refers to how Octave binary operators and functions behave when their matrix or array operands or arguments differ in size.

![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_82.jpg)

* * *


# Pandas

* * *


### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_83.jpg) = Pandas...

* [Overview](http://pandas.pydata.org/)

* n/a

    * Pandas represent the python module pandas.

* Makes Python work like R: Series, Data frames, CSV importing.

* Provids high-performance, easy-to-use data structures and data analysis tools for the Python

### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_84.jpg) = Series...

* The pandas just won the world series. 

    * Pandas represent the python module pandas.

    * The world series trophy represents the concept of a series. 

### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_85.jpg) = DataFrame...

* [YouTube](https://www.youtube.com/watch?v=1uVWjdAbgBg) | [Github](https://github.com/gjreda/pydata2014nyc/blob/master/demo.ipynb)

* There is a TV mounted into the wall around a picture frame. Its showing the Star Trek bridge with data in the middle.

    * A tv with a picture frame around it represent a data frame. 

* One important thing about pandas is that you can vectorize everything, not looping.

<table>
  <tr>
    <td>pd.read_csv('yo.csv')</td>
    <td>pd.read_json('yo.com/j.json')</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>df.info()</td>
    <td>df.describe()</td>
    <td>df.head()</td>
  </tr>
  <tr>
    <td>NaN vs. NULLS</td>
    <td></td>
    <td>Also: tail()</td>
  </tr>
  <tr>
    <td>df.set_index('date')</td>
    <td>df.ix['2015-05-23']</td>
    <td>df.ix[‘2015-05-23’, ‘col’]</td>
  </tr>
  <tr>
    <td>After: reset_index()</td>
    <td>Only works after set_index()</td>
    <td>Returns a series</td>
  </tr>
  <tr>
    <td>data[data['Pclass'] == 3]</td>
    <td>towed[(towed.color == 'BLK') & (towed.state == 'MI')]</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>& = and</td>
    <td>| = Or</td>
  </tr>
  <tr>
    <td>df[(df.make == 'PO') | (df.state == 'NY')].sort(['make', 'color'], ascending=[True, False])</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>We want the make to stay sorted ascending and the color descending.
When you want to do something with multiple columns you pass a list </td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>dv.value_counts()</td>
    <td>data[data['Pclass'] == 3].sort(‘state’, ascending=False)</td>
    <td></td>
  </tr>
  <tr>
    <td>Returns "True" or “False”</td>
    <td></td>
    <td></td>
  </tr>
</table>


#### + concat & merge...

* [Great Example](http://chrisalbon.com/python/pandas_join_merge_dataframe.html)

<table>
  <tr>
    <td></td>
    <td>pd.concat([apple, google])
This can be nice when you pass multiple frame into it to combine them all.

pd.merge(google, apple, left_on="Date", right_on="Date", how="right")
</td>
  </tr>
</table>


* n/a

<table>
  <tr>
    <td>
+ Vectorize, Don't loop…
In 10 days we don't really hope we create a function and then use the apply method to apply it</td>
    <td>
+ Split, Apply Combine…
It's often most efficient to break something down into smaller pieces then apply some kind of a function to each piece and then put them back together </td>
  </tr>
  <tr>
    <td>
+ Group By…
This allows us to group data into sections that we specify. </td>
    <td></td>
  </tr>
</table>


### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_86.png)![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_87.png) = Data Wrangling...

* [Great overview video](http://pandas.pydata.org/)

* n/a

    * Jessie represents data wrangling.

* You can select data in many different ways, time series, arithmetic searches, SQL like grouping, group transforms, merging and filters.

* Basic stats, linear regression, mean, standard deviation, summary stats.

### ![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_88.jpg)![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_89.jpg) = Sparse and Dense Matrices

* n/a

    * A spartan race person in matrix code represents a sparse matrices.

* Sparse matrices are very nice in some situations. For example, in some machine learning tasks, especially those associated with textual analysis, the data may be mostly zeros. Storing all these zeros is very inefficient. We can create and manipulate sparse matrices as follows:

    * There are several other sparse formats that can be useful for various problems:

    * CSC (compressed sparse column)

    * BSR (block sparse row)

    * COO (coordinate)

    * DIA (diagonal)

    * DOK (dictionary of keys)

* The scipy.sparse submodule also has a lot of functions for sparse matrices including linear algebra, sparse solvers, graph algorithms, and much more.

![image alt text]({{ site.url }}/public/VFwBGwUzXZUrSMiUtZaJoA_img_90.png)

* * *


# Raw Input

* * *


