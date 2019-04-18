# SI507_finalProject: Book management system

Chenhao Xu

[Link to this repository](https://www.example.com)

---

## Project Description

My project is to develop a book management system that can help people to manage the book thev've read and make some comments on every book they've read. It can realize many functions related to book management such as registing, logging in, logging out, adding and deleting books and comments, etc.

## How to run

1. First, you should install all requirements with `pip install -r requirements.txt`.
2. Second, you should run `python SI507_finalProject.py runserver`.
3. Open your browser and type the url displayed on your terminal.

## How to use

1. First you should input the url: http://127.0.0.1:5000/login and select "register" button to make your acconut, and then you can use the username and password you registed to log in, and then you can go to the book management system's home page.
2. Second, after you acess the home page, you can input the book you've read, the type of book you've read and your comment of this book.
3. Third, you can delete the type, the book or the comment you've added in any time you want.
4. (Optional): Markdown syntax to include an screenshot/image: ![alt text](image.jpg)

## Routes in this application
-
- `/` -> this is the home page.
- `/register` -> this route has a form for user to register.
- `/login` -> this route has a form for user to login.
- `/delete_book/<book_id>` -> this route can delete specific book.
- `/delete_type/<type_id>` -> this route can delete specific book type.
- `/delete_comment/<comment_id>` -> this route can delete specific book comment.

## How to run tests
1. First we neet to open our terminal and cd into the main dictionary.
2. Second we need to pip install -r requirements.txt.
3. Then we need to run `python SI507project_tools.py` and then run `control + C` to exit the server.
4. Finally we need to run `python SI507project_tests.py` to run our test file and now we can see the test result in our terminal.

## In this repository:
- templates
  - login.html
  - register.html
  - book_manage.html
- requirements.text
- SI507project_tools.py
- SI507project_tools.py
- SI507_finalProject.py
**......(I haven't done it yet.)**
---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as demonstrated.
- [x] This is a completed requirement.
- [ ] This is an incomplete requirement.

Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [x] Project is submitted as a Github repository
- [x] Project includes a working Flask application that runs locally on a computer
- [x] Project includes at least 1 test suite file with reasonable tests in it.
- [x] Includes a `requirements.txt` file containing all required modules to run program
- [ ] Includes a clear and readable README.md that follows this template
- [x] Includes a sample .sqlite/.db file
- [x] Includes a diagram of your database schema
- [ ] Includes EVERY file needed in order to run the project
- [ ] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [x] Includes at least 3 different routes
- [x] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [x] Interactions with a database that has at least 2 tables
- [x] At least 1 relationship between 2 tables in database
- [x] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
- [x] Use of a new module
- [ ] Use of a second new module
- [ ] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
- [x] A many-to-many relationship in your database structure
- [x] At least one form in your Flask application
- [x] Templating in your Flask application
- [ ] Inclusion of JavaScript files in the application
- [x] Links in the views of Flask application page/s
- [ ] Relevant use of `itertools` and/or `collections`
- [ ] Sourcing of data using web scraping
- [ ] Sourcing of data using web REST API requests
- [x] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [ ] Caching of data you continually retrieve from the internet in some way

### Submission
- [ ] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [ ] I included a summary of my project and how I thought it went **in my Canvas submission**!

### What I have left to do?
**I will develop the frontend files in the next week(those HTML files), I want to make my websites to be more beautiful.**

### (PART 2)Database diagram
![image](https://github.com/chhaoxu/SI507---Final-Project/raw/master/projectSource/database_diagram.png)
<h3>(The database is put in the projectSource directory.)</h3>
