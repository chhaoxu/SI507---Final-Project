# SI507_finalProject: Book management system

Chenhao Xu

[Link to this repository](https://github.com/chhaoxu/SI507---Final-Project)

---

## Project Description

My project is to develop a book management system that can help people to manage the books thev've read and make some comments on every book they've read. It can realize many functions related to book management such as adding and deleting books and comments and books' types. And it also can show the recommendation books to the users as well.

## How to run

1. First, you should install all requirements with `pip install -r requirements.txt`.
2. Second, you should run `python SI507_finalProject.py runserver`.
3. Open your browser and type the url displayed on your terminal.
4. Then you can see the links on the website and go to every other page.

## How to use

1. First you should input the url that display on your terminal(e.g: http://127.0.0.1:5000/) and then you can go to the book management system's home page, and in that page, you can add your book's type, book's name and the comments related to that book. You can type repetive things and the system can manage them.
![image](https://github.com/chhaoxu/SI507---Final-Project/raw/master/projectSource/bookAdd.png)
2. Second, you can click the link "Click To View Book Recommendation" to go the the books recommendation page. The books in that page are all spidered from https://thegreatestbooks.org and you can refer to those books.
![image](https://github.com/chhaoxu/SI507---Final-Project/raw/master/projectSource/bookRecommendation.png)
3. Third, you can click the link "Back To Add Book" to back the the book adding page, and than you can click the link "Click To View My Book Repository" to go to your book repository page, and in that page you can see all things about your book repository.
![image](https://github.com/chhaoxu/SI507---Final-Project/raw/master/projectSource/bookList.png)
4. Last, you can delete the type, the book or the comment in the book repository page, but you should delete the comment first to delete a book.


## Routes in this application
- `/` -> this is the home page that you can add books.
- `/bookRecommendation` -> this route shows books recommendation to users.
- `/myBook` -> this route is your book repository.
- `/delete_book/<book_id>` -> this route can delete specific book and show if your operation is successful.
- `/delete_type/<type_id>` -> this route can delete specific book type and show if your operation is successful.
- `/delete_comment/<comment_id>` -> this route can delete specific book comment and show if your operation is successful.

## How to run tests
1. First we neet to open our terminal and cd into the main dictionary.
2. Second we need to pip install -r requirements.txt.
3. Then we need to run `python SI507project_tools.py` and then run `control + C` to exit the server.
4. Finally we need to run `python SI507project_tests.py` to run our test file and now we can see the test result in our terminal.

## In this repository:
- templates
  - success.html
  - myBook.html
  - bookRecommendation.html
  - book_manage.html
  - fail.html
- projectSource
  - database_diagram.png
  - bookRecommendation.png
  - bookAdd.png
  - bookList.png
- requirements.text
- SI507project_tools.py
- SI507project_tests.py
- SI507_finalProject.py
- sample_books.db
- README.md
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
- [x] Includes a clear and readable README.md that follows this template
- [x] Includes a sample .sqlite/.db file
- [x] Includes a diagram of your database schema
- [x] Includes EVERY file needed in order to run the project
- [x] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [x] Includes at least 3 different routes
- [x] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [x] Interactions with a database that has at least 2 tables
- [x] At least 1 relationship between 2 tables in database
- [x] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
- [x] Use of a new module
- [x] Use of a second new module
- [x] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
- [x] A many-to-many relationship in your database structure
- [x] At least one form in your Flask application
- [x] Templating in your Flask application
- [ ] Inclusion of JavaScript files in the application
- [x] Links in the views of Flask application page/s
- [ ] Relevant use of `itertools` and/or `collections`
- [x] Sourcing of data using web scraping
- [x] Sourcing of data using web REST API requests
- [x] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [x] Caching of data you continually retrieve from the internet in some way

### Submission
- [x] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [x] I included a summary of my project and how I thought it went **in my Canvas submission**!


### (PART 2)Database diagram
![image](https://github.com/chhaoxu/SI507---Final-Project/raw/master/projectSource/database_diagram.png)
<h3>(The database is put in the projectSource directory.)</h3>
