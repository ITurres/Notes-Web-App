<div align="center">
    <img alt="notes website logo" src="readme-src/readme-media/notes-logo.png" width="100">
    <h1>Notes</h1>
</div>

> “Notes” is my cs50x final project Web Application. It is a basic web app that resembles a bit like 'Notes' from iCloud, and where you can create an account, sign in and start creating, updating, and deleting your notes, plus search for specific ones given their content.

#### Project Presentation (Video Demo): <https://youtu.be/UJucGYwoDCA>

---

#### **\*Previews at the end of this file.**

---

## Built With

- HTML - HTML5
- CSS - CSS3
- JavaScript
- Python 3
- Flask
- cs50 for SQL
- sqlite

#### [![My Skills](https://skillicons.dev/icons?i=html,css,js,python,flask,sqlite)](https://skillicons.dev)

---

<br>

## [![My Skills](https://skillicons.dev/icons?i=python)](https://skillicons.dev) Understanding .py files

## **> app.py**

> It is the engine of the website, where all the data manipulation, queries to the database and the rendering of each webpage happens.

### There are 8 main functions, all link to it's specific and individual route. (list below)

- index
- login
- logout
- register
- add_new_note
- update_note
- delete_note
- search_notes

- ### Note: ( index, add_new_note, update_note, delete_note and search_notes ) make use of @helpers.login_required (see helpers.py \*Understanding section)

### **>> index():**

> index will only be executed as long as @helpers.login_required has return correctly.
> This function routes you to the main/home/index webpage which only you (the user, if and only if has been successfully logged in) can access. And
> where through a SQL query the function will render the said main/home/index webpage with the user's data (name, notes).

### **>> login():**

> The login function, makes sure to first clean the current session and then process the data provided through the POST method to validate it.
> Login makes sure the 'user' enters valid data, such as username and password. It checks whether it's not empty if it is correct, and if it matches the data
> in the database or not. Again this last one uses an SQLite query.

> When a validation error occurs, the function will return by rendering the webpage again, keeping the 'user's input values in place and showing to
> the user, what's wrong with the input value.

> If the 'user' has successfully logged in, then the index.html webpage will be rendered and a -flash- message will be shown to the 'user'.

### **>> logout():**

> The logout function just clear the current 'user' session and return by rendering to index, which in consequence, will redirect to login.

### **>> register():**

> register, as the word says, will 'register' the new user. It again will process the data provided through the POST method to validate it.
> register will make sure the 'user' enters valid data, such as username, password, and password confirmation. It checks whether it's not empty if it is correct, and in the case of the password, if both the password and the confirmation match.
> Then it will insert all the validated data into the -'users'- database (see notes.db \*Understanding section).
> next it will query all data from the 'user', and store it in a variable to SET the current -session- with the 'user''s id
> afterwards will return by rendering index (/) and flash the user a "successfully register" message with the 'user''s name.

### **>> add_new_note():**

> This function when the request method is POST will first store the current session id in a variable, then validate the new note content (if it is empty or not)
> and will insert into the user_notes table in the database (see notes.db \*Understanding section) the note content where the 'user''s id matches.
> then will return by redirecting to index (/).

### **>> update_note():**

> update_note behaves like add_new_note, except that this function will query to update the column note_content if the note_id matches.
> The function will store the note content into a variable as well as the note's id and then proceeds to query the update.
> Finally, the function will return by redirecting to index (/).

### **>> delete_note():**

> The delete_note function when the request method is POST, will store the selected note's id and query the deletion to the note that matches the given id.
> Finally, the function will return by redirecting to index (/).

### **>> search_notes():**

> If the request method is POST, the function will store the current session id, and it will get the value from the input to be searched.
> This value (value_searched) will be concatenated with two % (percentage symbols) to insert it into the later query.
> Then the function will query for a list of all the notes found that match the current user id and the value_searched.
> Later it will store the length of that list (as the number of notes found, AKA results) and lastly, it will return by rendering
> search-results.html and passing results and the list (notes_found) to the html file.

---

## > helpers.py

> This file contains all the sub-functions used in app.py such as login_required and check_username.

### **>> login_required(f):**

> f (the parameter passed to login_required) will be the function to be wrapped. login_required returns the wrapped function. This is done by creating an inner function and returning it.
> Note that the first two returns are part of decorated_function (the inner function, not invoked in this code, just defined), while the third one is part of >
> login_required.
> decorated_function is a function returned by login_required (it's another function object every time login_required is called). That function will be used
> instead of the one passed for f. So every time one would call index function, the call would go to the function returned by login_required(index) instead.
> And here is the documentation on <a href="https://docs.python.org/3/library/functools.html#functools.wraps">@wraps</a>
> => credits to <a href="https://www.reddit.com/r/cs50/comments/ac6678/which_is_the_explanation_of_how_the_custom/">Blauelf</a>.

### **>> check_username(username):**

> This function will query the users table in the notes database to retrieve the username that matches the username passed as a parameter
> then it will check whether the query successfully retrieves any data or not, and return said result as a boolean (true/false).

---

## [![My Skills](https://skillicons.dev/icons?i=sqlite)](https://skillicons.dev) Understanding .db files

## > notes.db

> notes database is the main database, which holds four tables:

- 1: **users**, Which itself holds three columns => id (primary-key), username, hash. The last one is used as the password.
- 2: **user_notes**, which holds five columns => id (primary-key), user_id, note_content, date_time, and a reference to foreign key.
- 3: **sqlite_sequence**, the table automatically created by app.config.
- 4: and a UNIQUE INDEX table for username on **users** (1:).

> for a more graphical peek, have a look at the => notes-db-template.db -file-.

---

## [![My Skills](https://skillicons.dev/icons?i=js)](https://skillicons.dev) Understanding .js files within /animations folder

## > toggle-note-height.js

> The variable -noteTextarea- gets the element that has the data attribute indicated within [] square-brackets.
> then within a loop it listen for a click and as a result of it, this toggles two classes:

- 1: **large** => that apply a specific (height) to the element targeted, see folder animations/expand-note.css.
- 2: **hidden** => this last one is apply to the two times sibling's element, and it toggles the property (display) and (visibility).
  > see folder animations/toggle-visibility.css.

## > toggle-visibility.js

> There are two variables, -newNoteForm- and -toggleNewNoteFormBtn-, each gets the element that has the data attribute indicated
> within [] square-brackets.

> -toggleNewNoteFormBtn- is a collection of HTML elements, and on line 13 is associated with a forEach loop method that for each
> element it listens for a click (through an event listener) and calls the function -toggleHiddenClass()- (described next) passing as parameters the
> variable -newNoteForm- and -toggleNewNoteFormBtn- itself.

### **>> toggleHiddenClass(elements, element):**

> This function takes -elements- (a collection of HTML elements) and -element- (a single HTML element) as parameters.
> Within the function, it loops through -elements- with the "forEach" method, and for each element it toggles the element's class -hidden-.
> Finally, -element- also gets its class toggled.

---

<br>

## Previews

### **\* There are 7 short previews, each showing the following actions:**

- register
- add_new_note
- update_note
- delete_note
- search_notes
- login
- logout

### **register:**

<https://user-images.githubusercontent.com/100724715/230662591-87498795-1d2b-415e-8cb8-f682405120ed.mp4>

### **add_new_note:**

<https://user-images.githubusercontent.com/100724715/230662636-0a9fec94-2a69-43ae-970a-7901f072a374.mp4>

### **update_note:**

<https://user-images.githubusercontent.com/100724715/230662651-2ad322fe-aa22-4140-be2c-0d8b8a470bac.mp4>

### **delete_note:**

<https://user-images.githubusercontent.com/100724715/230662667-50784120-08a7-43b2-95e8-c26b87cf7427.mp4>

### **search_notes:**

<https://user-images.githubusercontent.com/100724715/230662677-2c397567-151a-4546-abf6-ce229ce8c8e8.mp4>

### **login:**

<https://user-images.githubusercontent.com/100724715/230662689-71edc721-9ae9-4c8e-995c-d1291c10382e.mp4>

### **logout:**

<https://user-images.githubusercontent.com/100724715/230662696-86e595d4-45cf-4121-bee9-3fc981db2037.mp4>

---

## Author

### 🙋‍♂️ Arthur Iturres

- #### [![My Skills](https://skillicons.dev/icons?i=github)](https://skillicons.dev) [@ITurres](https://github.com/ITurres)

- #### [![My Skills](https://skillicons.dev/icons?i=linkedin)](https://skillicons.dev) [Linkedin](https://www.linkedin.com/in/arturoemanuelguerraiturres/)

---

## Show your support

#### Give a ⭐ if you liked this project
