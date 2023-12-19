# MinimaList Student Organisation App
#### Video Demo:  https://youtu.be/cCF-_LsYZRQ
#### Description:

# Intro
I produced a stand-alone application which allows the user to access features such as Notes, Calendar, Calculator, Stop Watch, Flip Clock and Alarm Clock all in once place. This would improve any user’s productivity and allow them to organise their day alongside work effectively. Because Python offers easy access to the tkinter library, the best toolkit for developing GUI-based applications, I will utilise it to code this program.

# Use of Libraries
The use of additional libraries allowed me to develop a GUI that was user-friendly and played a core role in establishing the minimalism in my minimalist student organisation app. With the import of Tkinter I was able to work closer towards my goal of a simple and clean UI design as it is one of the best toolkits for creating simple graphical desktop apps. In addition to this my use of a databases, through sqlite3, allows my user to save sensitive details such as a passwords and usernames within the database for repeated use while ensuring security.

# Use of Simple Selection
The use of simple selection in my code has recurring purposes. The first is done to verify if a user has successful inputted the login details and if they are met with a login successful prompt. Under the circumstances those criteria are met the program decides the next course of action and runs it, which is welcoming the user and asking them to close the window to proceed. Moreover simple selection helps within the login page to decide which text box to prompt at the user in the event of an error during the account creation. If a username has been stored and a the same one is entered, a text box warning a same name is shown, otherwise the account creation is successful and the user is updated.

# Use of Complex Selection
Complex selection was used within the development of the calculator program. The nested loops allowed multiple procedures to be run for one common function without having to create multiple smaller individual loops. Moreover in picture above, complex selection is used to within the calculator to check for potential errors, invalid inputs or blank fields to accordingly prompt a text box at the user with an error message. This ensures the user’s output for any calculation work is not compromised and that they can rely on the software

# Abstraction
Abstraction was implemented in the program through multiple user defined functions. One large program was broken down into smaller programs divided in the form of unique windows for each feature. Rather than coding an application in which each function is dependent or integrated on each other, abstractions allows me to develop multiple smaller features simultaneously. This proves to be exceptionally useful when an error occurs within the code and each window is able to function without crashing or simply not running.

# User defined function
User defined functions are used throughout my application for defining each feature, such as notes, calendars, stopwatch, alarms clock, flip clock and calculator. Moreover user defined functions make it easier for the programer to code a text box to be prompted for events such as alarms being set. Messages like this act as a confirmation for the user that a task is not set in acorn and it will be completed. Abstraction’s user defined functions play a key role isolating certain tasks and features from each other making the app less dependent and more likely to function well even in the circumstance of a bug or error.

# User defined function with parameters
User defined functions with parameters are used within the login page for widgets to denote a specific quantity to each parameter. The GUI can easily be developed with tools like this when buttons are developed within user defined functions, colour, size and font specifications can all be written without much of a hassle and be directly integrated with the program. The parameters allow the geometry to stay consistent and the app to maintain one size and appearance, improving the user-friendly aspect of it.

# User defined function with return value
User defined functions with return values are used throughout the code to return no value in certain tasks and programs. Return is the keyword which means a certain value needs to be returned from a function. It acts as a indicator that the program has been run successfully and it can be terminated once the return statement presents a value. In my code specifically the calendar function returns a value of 0 when the calendar buttons for ‘show’ to display the data and ‘clear’ to erase the values is presented as a sign that these procedures have carried out as needed.

# Inheritance
Inheritance refers to the action of inheriting functions, methods, variables from the parent classes or other classes. In my program I have used inheritance to inherit functions and variables from classes such as ‘main’ and GUI(Tk). With access to the parent’s functionality I am able to reuse the objects multiple times, making the code more reliable and effective.

# Encapsulation
Encapsulation is hiding the details of a program. In my code I have encapsulated all the functions inside one class defined as ‘GUI’. The encapsulation of all these lines of code makes it more easy to location and pinpoint bugs within a code, division of tasks using abstraction makes the development process simpler as it’s easier to navigate within the code. This makes changes, syntax fixes and development more organised.

# Polymorphism
Polymorphism means acquiring different forms, and this can be achieved by overriding or writing same named methods in subclass formed. This can also be achieved using "super" in python which inherits all the super class functionalities in sub-class.

# Object Oriented Programming
Object oriented programming is a method of code organisation in order to increase the extent of reusability. With this form of programming, specific objects that can can be interacted by the user and program are comprised and shut, essentially making all objects self contained, which improves any method of troubleshooting drastically. Moreover through the reusability of inheritance and flexibility of polymorphism it is an excellent problem solving method.