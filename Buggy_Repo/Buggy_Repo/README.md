### Fixing the Buggy Code

- This code has 30 issues out of which 1 is no code in style.css . 
- The total marks for the entire codebase is 40, some issues have more marks than the other one. Style.css is of 5 marks. It will get scaled down to 20. All team members will get equal marks.
- You are suppose to work in teams of 4 or 5
- Each team member has to identify atleast 4 issues and fix atleast 4 issue. If someone doesn't do this, their marks get deducted.
- You are suppose to work on a git repository as collaborators

### What kind of bugs are there

- Bugs which will break your code
- Bugs might be a single word
- Bugs might be section of removed code
- Bugs might be section of unnecessary code
- Bugs might be useless files
- Bugs might be in the UI/UX of the pages
- Bugs might be in the api calls
- Bugs might be in the dependencies  

### submission format

- Make submissions on moodle
- Do not remove .git folder 
- Only 1 submission per team
- Submit it as Corrected_Code.zip

### Add the names of the members and roll numbers of your team below

- Arya Mirani : 2024101145
- Chandrani Saha : 2024113002
- Mehrish Khan : 2024111014
- Maithily Bhala : 2024117011
- Kimaya Kashyap : 2024115001

### Table to keep track

| ID  | Issue Description                        | Identified By | Fixed By     |
|-----|------------------------------------------|---------------|--------------|
| 1   | Style.css is not filled                                    |         arya |     arya     |
| 2   | quiz.py: changed to return a random question | Chandrani   | Chandrani       |
| 3   | quiz.py: changed method for /answer from get to post    | Chandrani        | Chandrani             |
| 4   | Users.py: Edit 1: Changed POST to GE        |  Kimaya      |
| 5   | Users.py: Edit 2: delete_all() to delete_one()| Kimaya   |  Kimaya      |
| 4   | analytics.py: Inefficient import: `init_db` was imported inside function                        | Mehrish       | Mehrish      |
| 5   | analytics.py: Dummy data used in users list (e.g., `["A1", "B2", "C3"]`)                         | Mehrish       | Mehrish      |
| 6   | analytics.py: No error handling for database fetch                                               | Mehrish       | Mehrish      |
| 7   | analytics.py: Unsafe dict access for `["names"]` and `["usernames"]` – could throw KeyError      | Mehrish       | Mehrish      |
| 8   | analytics.py: Unnecessary histogram generation in API logic                                      | Mehrish       | Mehrish      |
| 9 | items.py: router is incorrectly defined as a dictionary ({}) instead of APIRouter().                                        | Maithily              | Maithily             |
| 10  | items.py: Duplicate @router.post("/") decorators for create_item, causing route conflicts.                                         | Maithily               | Maithily             |
| 11| items.py: delete_item uses ObjectId without validating if item_id and item_details are valid ObjectId strings.                                        | Maithily              | Maithily             |
| 12  | items.py: delete_item attempts to delete two items but only checks the result of the first deletion, leading to potential logical errors.                                         | Maithily               | Maithily             |
| 13 | items.py: Missing import for Item model validation, which may cause runtime errors if Item is not properly defined.                                         | Maithily              | Maithily             |
| 16  | Models.py:Edit 1:Item class inherits from BaseModel | Kimaya            | Kimaya           |
| 17  | Models.py:Edit 2: Name type should be str|Kimaya             |   Kimaya           |
| 18  | quiz.py: using Request and await json | Chandrani            | Chandrani             |
| 19  |  index.html    - added quiz.html                   |  arya             |    arya          |
| 20  |  news.js - changed the code so that the searching and sortign works      |        arya       |     arya         |
| 21  | quiz.py: changed to make sure question is not repeated                                            |  Chandrani           | Chandrani             |
| 22  | profile.html - added quiz.html                                         |         arya      |       arya       |
| 23  | items.html- edit 1:Added missing container to hold all item content                                         |    Kimaya           |      Kimaya        |
| 24  | items.html- edit 2:Added form with id 'itemForm' for adding new items |  Kimaya             | Kimaya             |
| 25  | items.html- edit 3:Added search input                                        | Kimaya              |  Kimaya            |
| 26  | items.html- edit 4:Added item count and list container                                       |     Kimaya          |  Kimaya            |
| 27  |  added all the pages in the menu bar in all 6 of the html pages                                      |       arya        |     arya         |
| 28  | Added gameOver Check in loadQuestion Function                                     |        Chandrani       |      Chandrani        |
| 29  |     Added Error Handling for Missing Answer and Invalid ID                                     |      Chandrani         |  Chandrani            |
| 30  |    Reset Button and Game State Management                                      |   Chandrani            |    Chandrani          |
| 31  | items.html: Added dynamic item count element and JS interaction for item count	|Mehrish |Mehrish|
| 32	|items.html: Corrected <ul> ID from 'items-list' to 'itemList' as per JS reference	|Mehrish |Mehrish|
