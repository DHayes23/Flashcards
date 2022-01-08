
# **Flashcards - Code Institute Milestone 3 Project**

## **Milestone Project 3** by Denis Hayes
---
---
 ## **Manual Test Procedures and Current Statuses**
 The following section documents the Testing Procedures used to test feature functionality and the feature's current status.
 ---
 ---
 ---
## **Feature Set - Base**
 ---
### **Favicon**
Expected Functionality:
* The Favicon, a small icon depicting a fanned-out set of cards, should display in the browser tab when visiting any Flashcards page.

Testing Procedure:
* Open the Flashcards website within a browser.
* Observe the tab in which the website is open.
* If the Favicon is present, this feature is functioning as expected.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

### **Header**
Expected Functionality:
* The Header should display the brand name (Flashcards) and a series of navigation links on the right side of the heading.
* The Header should follow the user as they scroll down a page.
* Clicking on any of the navigation links should redirect the user to a new page.
* The naviagion links should change depending on the access rights of the user.
* On small screens the navigation links should be replaced with a 'burger menu' icon.
* Clicking on the 'burger menu' icon should open a sidenav which contains the same link elements as would be found on a large screen, displayed vertically.

Testing Procedure:
* Open the Flashcards website on a large screen.
* Observe the Header. If the brand name (Flashcards) is displayed on the left hand side of the screen with navigation links to the right, this aspect of the feature is functioning as expected.
* If the Header follows the user as they scroll down a page, this aspect of the feature is functioning as expected.
* Click each of the navigation links. If each link redirects the user to a new page that corresponds to the link text, this aspect of the feature is functioning as expected.
* Log into the website with different types of account(Admin, Standard User) and observe the navigation links. If the navigation links change in line with the different access rights of the user, this aspect of the feature is functioning as expected.
* Change the screen size to that of a small screen using the browser's developer tools.
* If the navigation links are replaced with a 'burger menu', click the menu.
* If clicking the menu icon opens a sidenave which displays the same link elements as would be found on a large screen, albeit displayed vertically, this aspect of the feature is functioning as expected.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

### **Footer**
Expected Functionality:
* The Footer should appear at the bottom of every page on the website.
* Clicking on the GitHub icon should open my GitHub profile page in a separate tab.
* Clicking on the Email icon should open the user's default email client in a separate tab and automatically fill the 'To' field with a contact email address.
* Clicking on the 'Back to Top' button should gently scroll the user back to the top of any page that they're on.

Testing Procedure:
* Scroll to the bottom of any page within the site and observe the Footer.
* If the Footer is at the very bottom of the page, with no content (including whitespace) thereafter, this aspect of the feature is functioning as expected.
* Click on the GitHub icon. If a new tab opens in the browser displaying my GitHub profile page, this aspect of the feature is functioning as expected.
* Click on the Email icon. If a new tab opens with the user's default email client and automatically fills the 'To' field of the email with a contact email address, this aspect of the feature is functioning as expected.
* Click on the 'Back to Top' button. If the page scrolls gently back to the top, this aspect of the feature is functioning as expected. NOTE: If the page does not have sufficient content to navigate away from the top of the page, this button will not scroll. This is the expected functionality of the button.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

---
 ## **Feature Set - Index**
 ---

### **Heading/Call to Action**
Expected Functionality:
* The Heading/Call to Action should display a message to the user about the purpose of the site.
* The part of the Heading/Call to Action that reads "Create an Account" is a link that should redirect the user to the Create an Account page.

Testing Procedure:
* Click on the "Create an Account" link within the heading.
* If clicking the link redirects to the Create an Account page, this feature is functioning as expected.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

### **Deck Display - All Decks**
Expected Functionality:
* The All Decks Display should render a card element for each deck within the MongoDB collection 'Decks', containing the basic information of each deck.
* The Flag icon in each deck should correspond to the language underneath it.
* The Play button on each deck should redirect the user to the Play page that corresponds to the deck it is attached to.

Testing Procedure:
* Obeserve the All Decks display. Count or otherwise note the decks contained in the display.
* Log into MongoDB and browse the 'Decks' collection. If all of the decks that are in the 'Decks' collection are contained in the All Decks display, this aspect of the feature is functioning as expected.
* Observe the Flag icon in each deck. Check that the icon matches the language displayed underneath it. If the Flag icon and the language underneath match, this aspect of the feature is performing as expected.
* Click the Play button on a deck.
* If clicking the Play button redirects to that specific deck's corresponding Play page, this aspect of the feature is functioning as expected.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

---
 ## **Feature Set - Create an Account**
 ---
 ### **Create Your Account - Form**
 Expected Functionality:
* Clicking either the Username or the Password input on the form should allow the user to type.
* Filling out the form in the accepted manner should allow the user to click the 'Create Account' button and instantiate a new user object in the MongoDB 'Users' collection. The user should then be redirected to their new 'My Decks' page.
* If the user inputs a username already in use, a flash message should inform them of this fact and the form should not be submitted to the database.
* If the user does not match the required format of the input, the line under the input should turn red, and clicking the 'Create Account' button should prompt the user to change their inputs, without submitting the form to the database.

Testing Procedure:
* Log into MongoDB and browse the 'Users' collection.
* Fill out the 'Create Your Account' form inputs in the accepted manner.
* Click the 'Create Account' button.
* Check the MongoDB 'Users' collection for the new user. If the new user has been created, this aspect of the feature is functioning as expected.
* Fill out the 'Create Your Account' form inputs in the accepted manner, but provide a username that you know already exists.
* Click the 'Create Account' button. 
* If a flash message appears stating 'Sorry, that username is taken!', this aspect of the feature is functioning as expected.
* Fill out the 'Create Your Account' form inputs in a manner that is not acceptable (e.g. Enter a username that is only 2 characters long).
* Click the 'Create Account' button.
* If upon clicking the button a prompt appears requesting changes be made to the input/s, this aspect of the feature is functioning as expected.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

 ### **Call to Action**
Expected Functionality:
* The Call to Action should display a message to the user asking if they already have an account.
* The part of the Call to Action that reads "Log in here!" is a link that should redirect the user to the Log In page.

Testing Procedure:
* Click on the "Log in here!" link within the heading.
* If clicking the link redirects to the Log In page, this feature is functioning as expected.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

 ---
 ## **Feature Set - Log In**

 ---
### **Log In - Form**
 Expected Functionality:
* Clicking either the Username or the Password input on the form should allow the user to type.
* Filling out the form in the accepted manner should allow the user to click the 'Log In' button. The user should then be redirected to their 'My Decks' page.
* If the user inputs an incorrect username or password, a flash message should inform them of this fact and the Log In page should refresh.
* If the user does not match the required format of the input, the line under the input should turn red, and clicking the 'Log In' button should prompt the user to change their inputs.

Testing Procedure:
* Fill out the 'Log In' form inputs in the accepted manner with the username and password of an existing account.
* Click the 'Log In' button.
* If clicking the button redirects to the My Decks page for the user whose information was input into the form, this aspect of the feature is functioning as expected.
* Fill out the 'Log In' form inputs in the accepted manner, but provide a username or password that you know does not exist.
* Click the 'Log In' button. 
* If a flash message appears stating 'Please enter a valid Username and Password', this aspect of the feature is functioning as expected.
* Fill out the 'Log In' form inputs in a manner that is not acceptable (e.g. Enter a username that is only 2 characters long).
* Click the 'Log In' button.
* If upon clicking the button a prompt appears requesting changes be made to the input/s, this aspect of the feature is functioning as expected.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

### **Call to Action**
Expected Functionality:
* The Call to Action should display a message to the user asking if they do not yet have an account.
* The part of the Call to Action that reads "Create an Account!" is a link that should redirect the user to the Create an Account page.

Testing Procedure:
* Click on the "Log in here!" link within the heading.
* If clicking the link redirects to the Log In page, this feature is functioning as expected.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

 ---
 ## **Feature - Log Out**
 ---
Expected Functionality:
* The Log Out button is displayed in with the navigation links in the header, and should be visible to any user who has logged in.
* Clicking the Log Out button removes all session cookies from a user, thereby removing access rights, and redirects the user to the Index page.

Testing Procedure:
* Click on the Log Out button.
* If clicking the button removes all session cookies and redirects the user to the Index page, this feature is functioning as expected.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

## **Feature Set - My Decks**
 ---
### **Username Banner**
 Expected Functionality:
* The Username Banner should display the user's username at the top of their profile, followed by the word 'Profile'.
* For example, if the user's username is 'TestUser' the Username Banner would read 'TestUser's Profile'.

Testing Procedure:
* Log in as any user.
* Observe the Username Banner. If the user's username is being displayed correctly, this feature is functioning as expected.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

 ### **Your Decks - Deck Display**
 Expected Functionality:
* The Your Decks Display should render a card element for each deck within the MongoDB collection 'Decks' and whose creator is the user that is currently logged, containing the basic information of each deck.
* The Flag icon in each deck should correspond to the language underneath it.
* The Play button on each deck should redirect the user to the Play page that corresponds to the deck it is attached to.
* The Edit button on each deck should redirect the user to the Edit Deck page that corresponds to the deck it is attached to.

Testing Procedure:
* Obeserve the My Decks display. Count or otherwise note the decks contained in the display.
* Log into MongoDB and browse the 'Decks' collection. If all of the decks that are in the 'Decks' collection and whose creator is the user that is currently logged in, are contained in the My Decks display, this aspect of the feature is functioning as expected.
* A secondary indicator that the My Decks display is functioning is that all decks contained within the display feature the user's username in the 'Deck created by:' section of the deck.
* Observe the Flag icon in each deck. Check that the icon matches the language displayed underneath it. If the Flag icon and the language underneath match, this aspect of the feature is performing as expected.
* Click the Play button on a deck.
* If clicking the Play button redirects to that specific deck's corresponding Play page, this aspect of the feature is functioning as expected.
* Click the Edit button on a deck.
* If clicking the Edit button redirects to that specific deck's corresponding Edit Deck page, this aspect of the feature is functioning as expected.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

 ### **Create New Deck Button**
 Expected Functionality:
* The Create New Deck button should be displayed at the top of the Your Decks Deck Display.
* Clicking on this button should redirect the user to the Create Deck page.

Testing Procedure:
* Click on the Create New Deck button.
* If clicking the button redirects to the Create Deck Page, this feeature is functioning as expected.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

 ### **Decks You Love - Deck Display**
Expected Functionality:
* The Decks You Love Display should render a card element for each deck within the MongoDB collection 'Decks' which contains the currently logged in user's _id in the 'deck_loved_by' array, containing the basic information of each deck.
* The Flag icon in each deck should correspond to the language underneath it.
* The Play button on each deck should redirect the user to the Play page that corresponds to the deck it is attached to.

Testing Procedure:
* Obeserve the My Decks display. Count or otherwise note the decks contained in the display.
* Log into MongoDB and browse the 'Decks' collection. If all of the decks that are in the 'Decks' collection and whose creator is the user that is currently logged in, are contained in the My Decks display, this aspect of the feature is functioning as expected.
* A secondary indicator that the My Decks display is functioning is that all decks contained within the display feature the user's username in the 'Deck created by:' section of the deck.
* Observe the Flag icon in each deck. Check that the icon matches the language displayed underneath it. If the Flag icon and the language underneath match, this aspect of the feature is performing as expected.
* Click the Play button on a deck.
* If clicking the Play button redirects to that specific deck's corresponding Play page, this aspect of the feature is functioning as expected.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

---
## **Feature - Love System**
 ---
 Expected Functionality:
* The Love System should allow a user to click the Heart icon on the Play page for any deck (of which they are not the creator), which will then add that user's _id to that deck's 'deck_loved_by' array within the MongoDB 'Decks' collection.
* Decks that are 'loved' by a user should have their Heart icon, in all of its instances, change to a new, filled in version of that same icon.
* Clicking on the new filled in version of the icon should remove the user's _id from that deck's 'deck_loved_by' array within the MongoDB 'Decks' collection, reverting the Heart icon to its original state and allowing the user to 'love' the deck again.

Testing Procedure:
* Log in as any user.
* Navigate to the Play Deck page of any deck that was not created by the currently logged in user.
* Click the Heart Icon. If the Heart icon changes to a filled in version of the icon, this aspect of the feature is functioning as expected.
* Log into MongoDB and browse the 'Decks' collection. Find the currently logged in user's _id in the 'Users' collection. Find the deck that has just been 'loved' within the 'Decks' collection, and check that its 'deck_loved_by' array contains the _id of the currently logged in user. If the user's _id can be found within the array, this aspect of the feature is functioning as expected.
* Navigate to the currently logged in user's My Decks page. Observe the Decks You Love Deck Display. Check that the deck that has just been 'loved' is present in the display. If the deck is present, this aspect of the feature is functioning as expected.
* Click the filled in Heart icon. If the heart icon changes to a hollowed out version of the icon, this aspect of the feature is functioning as expected.
* Check the deck's 'deck_loved_by' array for the currently logged in user's _id again. If the _id is no longer present, this aspect of the feature is functioning as expected.
* Navigate to the currently logged in user's My Decks page. Observe the Decks You Love Deck Display. Check that the deck that has just been 'unloved' is no longer present in the display. If the deck is not present, this aspect of the feature is functioning as expected.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

## **Feature Set - Create New Deck**
---
 ### **Create New Deck - Deck Information Modal**
  Expected Functionality:
* The Deck Inforamtion Modal button (The 'i' icon) should be displayed under the 'Deck Overview' heading on the Create Deck form.
* Clicking on the 'i' icon should display a modal to the user which provides tips on how to properly build a deck.
* Clicking the 'Close' button within the modal, or clicking anywhere outside of the modal, should close the modal.

Testing Procedure:
* Click on the 'i' icon.
* If clicking the icon displays the modal, this aspect of the feature is fucntioning as expected.
* Click the 'Close' button within the modal.
* If clicking the 'Close' button closes the modal, this aspect of the feature is fucntioning as expected.
* Click on any part of the website outside of the modal.
* If clicking any part of the website outside of the modal closes the modal, this aspect of the feature is fucntioning as expected.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

 ### **Create New Deck - Deck Overview - Form**
  Expected Functionality:
* Clicking an input on the form should allow the user to type.
* Filling out the form in the accepted manner should allow the user to click the 'Create Deck' button. The user should then be redirected to their 'My Decks' page and a flash message stating 'Deck Created!' should appear.
* If the user does not match the required format of the input, the line under the input should turn red, and clicking the 'Create Deck' button should prompt the user to change their inputs.

Testing Procedure:
* NOTE: Both the Deck Overview and the Cards form sections must be completed and tested simultaneously for these testing procedures to be valid.
* Fill out the 'Create Deck' form inputs in the accepted manner with the username and password of an existing account.
* Click the 'Create Deck' button.
* If clicking the button redirects to the My Decks page and flashes a message saying 'Deck Created!' , this aspect of the feature is functioning as expected.
* Fill out the 'Create Deck' form inputs in a manner that is not acceptable (e.g. Leave an input blank).
* If the line under the incorrect inputs turns red, this aspect of the feature is funtioning as expected.
* Click the 'Create Deck' button.
* If upon clicking the button a prompt appears requesting changes be made to the input/s, this aspect of the feature is functioning as expected.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

 ### **Create New Deck - Cards - Form**
   Expected Functionality:
* Clicking an input on the form should allow the user to type.
* Filling out the form in the accepted manner should allow the user to click the 'Create Deck' button. The user should then be redirected to their 'My Decks' page and a flash message stating 'Deck Created!' should appear.
* If the user does not match the required format of the input, the line under the input should turn red, and clicking the 'Create Deck' button should prompt the user to change their inputs.
* Clicking the 'Add New Card' button should create a new card element with new inputs and an 'X' icon.
* New form elements created with the 'Add New Card' button must be filled out correctly before the 'Create Deck' button will submit the form.
* Clicking the 'X' icon on a new form element created with the 'Add New Card' button will remove that card element.

Testing Procedure:
* NOTE: Both the Deck Overview and the Cards form sections must be completed and tested simultaneously for these testing procedures to be valid.
* Fill out the 'Create Deck' form inputs in the accepted manner with the username and password of an existing account.
* Click the 'Create Deck' button.
* If clicking the button redirects to the My Decks page and flashes a message saying 'Deck Created!' , this aspect of the feature is functioning as expected.
* Fill out the 'Create Deck' form inputs in a manner that is not acceptable (e.g. Leave an input blank).
* If the line under the incorrect inputs turns red, this aspect of the feature is funtioning as expected.
* Click the 'Create Deck' button.
* If upon clicking the button a prompt appears requesting changes be made to the input/s, this aspect of the feature is functioning as expected.
* Click the 'Add New Card' button.
* If clicking this button creates a new card element with new inputs and an 'X' icon, this aspect of the feature is funtioning as expected.
* Click the 'X' icon within the newly created card element.
* If clicking the icon removes the card element to which it is associated, this aspect of the feature is functioning as expected.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

 ---
## **Feature Set - Edit Deck**
---
 ### **Edit Deck - Deck Overview - Form**
   Expected Functionality:
* The Deck Overview form elements should be pre-filled with the corresponding values as found in the MongoDB database that apply to the specific deck being edited.
* Clicking an input on the form should allow the user to type and replace the existing content of the input.
* Filling out the form in the accepted manner should allow the user to click the 'Create Deck' button. The user should then be redirected to their 'My Decks' page and a flash message stating 'Deck Created!' should appear.
* If the user does not match the required format of the input, the line under the input should turn red, and clicking the 'Create Deck' button should prompt the user to change their inputs.

Testing Procedure:
* NOTE: Both the Deck Overview and the Cards form sections must be completed and tested simultaneously for these testing procedures to be valid.
* Observe the Deck Overview form elements. If the form elements are pre-filled with the corresponding values as found in the MongoDB database that apply to the specific deck being edited, this aspect of the feature is functioning as expected.
* Fill out the 'Create Deck' form inputs in the accepted manner with the username and password of an existing account.
* Click the 'Create Deck' button.
* If clicking the button redirects to the My Decks page and flashes a message saying 'Deck Created!' , this aspect of the feature is functioning as expected.
* Fill out the 'Create Deck' form inputs in a manner that is not acceptable (e.g. Leave an input blank).
* If the line under the incorrect inputs turns red, this aspect of the feature is funtioning as expected.
* Click the 'Create Deck' button.
* If upon clicking the button a prompt appears requesting changes be made to the input/s, this aspect of the feature is functioning as expected.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

 ### **Edit Deck - Cards - Form**
Expected Functionality:
* Each Card's form elements should be pre-filled with the corresponding values as found in the MongoDB database that apply to the specific deck being edited.
* Clicking an input on the form should allow the user to type and replace the existing content of the input.
* Filling out the form in the accepted manner should allow the user to click the 'Create Deck' button. The user should then be redirected to their 'My Decks' page and a flash message stating 'Deck Created!' should appear.
* If the user does not match the required format of the input, the line under the input should turn red, and clicking the 'Create Deck' button should prompt the user to change their inputs.

Testing Procedure:
* NOTE: Both the Deck Overview and the Cards form sections must be completed and tested simultaneously for these testing procedures to be valid.
* Observe each Card's form elements. If the form elements are pre-filled with the corresponding values as found in the MongoDB database that apply to the specific deck being edited, this aspect of the feature is functioning as expected.
* Fill out the 'Create Deck' form inputs in the accepted manner with the username and password of an existing account.
* Click the 'Create Deck' button.
* If clicking the button redirects to the My Decks page and flashes a message saying 'Deck Created!' , this aspect of the feature is functioning as expected.
* Fill out the 'Create Deck' form inputs in a manner that is not acceptable (e.g. Leave an input blank).
* If the line under the incorrect inputs turns red, this aspect of the feature is funtioning as expected.
* Click the 'Create Deck' button.
* If upon clicking the button a prompt appears requesting changes be made to the input/s, this aspect of the feature is functioning as expected.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

 ### **Edit Deck - Delete All Cards - Button**
   Expected Functionality:
* The Delete All Cards button should be displayed under the 'Edit Deck' heading on the Edit Deck form.
* Clicking on the Delete All Cards button should display a modal to the user which asks the user to confirm that their intention is to delete all cards in a deck.
* Clicking the 'Delete' button within the modal should remove all of the elements in the 'deck_card_fronts' and 'deck_card_backs' for the specific deck being edited, thereby removing all card elements from the deck.
* If the user confirms the deletion, a flash message should appear with the message 'Cards Deleted'. 
* If the user confirms the deletion, a new placeholder card should also be created to ensure that the user always has a card available to add content to.
* Clicking the 'Cancel' button within the modal, or clicking anywhere outside of the modal, should close the modal.

Testing Procedure:
* Click on the Delete All Cards button.
* If clicking the button displays the modal, this aspect of the feature is fucntioning as expected.
* Log into MongoDB and browse the 'Decks' collection. Find the deck that is currently being edited and check that its 'deck_card_fronts' and 'deck_card_backs' arrays contain the correct data. 
* Click the Delete button within the modal to confirm the deletion operation.
* If a flash message stating 'Cards Deleted' is displayed, this aspect of the feature is functioning as expected.
* Check the contents of the deck's 'deck_card_fronts' and 'deck_card_backs' arrays again. If the arrays are now empty, this aspect of the feature is functioning as expected.
* If a new placeholder card is now present in the Cards section of the form, this aspect of the feature is funtioning as expected.
* Click the 'Close' button within the modal.
* If clicking the 'Close' button closes the modal, this aspect of the feature is functioning as expected.
* Click on any part of the website outside of the modal.
* If clicking any part of the website outside of the modal closes the modal, this aspect of the feature is fucntioning as expected.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

 ### **Edit Deck - Delete This Deck - Button**
  Expected Functionality:
* The Delete This Deck button should be displayed under the 'Edit Deck' heading on the Edit Deck form.
* Clicking on the Delete This Deck button should display a modal to the user which asks the user to confirm that their intention is to delete this deck.
* Clicking the 'Delete' button within the modal should remove the deck from the MongoDB 'Decks' collection.
* If the user confirms the deletion, they will be redirected to their My Decks page and a flash message should appear with the message 'Deck Deleted'. 
* Clicking the 'Cancel' button within the modal, or clicking anywhere outside of the modal, should close the modal.

Testing Procedure:
* Click on the Delete Deck button.
* If clicking the button displays the modal, this aspect of the feature is fucntioning as expected.
* Log into MongoDB and browse the 'Decks' collection. Find the deck that is currently being edited. 
* Click the Delete button within the modal to confirm the deletion operation.
* If clicking the Delete button redirects to the My Decks page, this aspect of the feature is functioning as expected.
* If a flash message stating 'Deck Deleted' is displayed, this aspect of the feature is functioning as expected.
* Check the MongoDB 'Decks' collection to confirm that the deck has been removed.
* Click the 'Close' button within the modal.
* If clicking the 'Close' button closes the modal, this aspect of the feature is functioning as expected.
* Click on any part of the website outside of the modal.
* If clicking any part of the website outside of the modal closes the modal, this aspect of the feature is fucntioning as expected.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

 ### **Edit Deck - Love Counter Display**
Expected Functionality:
* The Love Counter Display is presented to the upper left of the Edit Deck Form.
* The display should present a message to the user stating how many other users have 'loved' the deck which is being edited.
* The integer used by the display to tell a user how many people love this specific is derived from the 'deck_love_counter' field for each deck in the 'Decks' collection in database.

Testing Procedure:
* Log into MongoDB and browse the 'Decks' collection. Find the deck that is currently being edited. 
* Note the 'deck_love_counter' field's value.
* Compare the integer in the 'deck_love_counter' field in the database with that presented in the Love Counter Display. If the values match, this feature is functioning as expected.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

 ### **Edit Deck - Report Counter Display**
Expected Functionality:
* The Report Counter Display is presented to the upper right of the Edit Deck Form.
* The display should present a message to the user stating how many other users have reported the deck which is being edited.
* The integer used by the display to tell a user how many people love this specific is derived from the 'deck_report_counter' field for each deck in the 'Decks' collection in database.

Testing Procedure:
* Log into MongoDB and browse the 'Decks' collection. Find the deck that is currently being edited. 
* Note the 'deck_report_counter' field's value.
* Compare the integer in the 'deck_report_counter' field in the database with that presented in the Report Counter Display. If the values match, this feature is functioning as expected.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

 ---
## **Feature Set - Play Deck**
---
 ### **Play Deck - Deck Display**
 Expected Functionality:
* The Deck Display on the Play page should present the user with a render of the main details of the deck being played in a card format. 

Testing Procedure:
* Navigate to the Play page for any deck and observe the Deck Display. If the details of the deck are displayed correctly this feature is functioning as expected.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

 ### **Play Deck - Love Deck**
 Expected Functionality:
* See the Expected Functionality of the Love System. 

Testing Procedure:
* See the Testing Procedure for the Love System. 


Current Status: **See the Current Status of the Love System.**

 ### **Play Deck - Report Deck**
  Expected Functionality:
* When clicked, the Report Deck flag icon should redirect the user to the Create Report page.

Testing Procedure:
* Navigate to the Play page for any deck not created by the currently logged in user.
* Click the Report Deck flag icon.
* If the site redirects to the Create Report page, this feature is functioning as expected. 

Current Status: <span style="color:green">**FUNCTIONAL**</span>

 ### **Play Deck - Cards**
 Expected Functionality:
* The Play page displays all cards contained within a deck, derived from the 'deck_card_fronts' and 'deck_card_backs' arrays.
* Each card displays the English version of the vocabulary on the 'front' of the card.
* On each card front there is a 'Flip' button. Clicking this button should 'flip' the card(trigger an animation that simulates the flipping of a card) and display the 'back' of the card.
* Each card displays both the English and translated verson of the vocabulary on the 'back' of the card.
* When the card is flipped, the Flip button is removed from the card.

Testing Procedure:
* Navigate to the Play page for any deck.
* Click the flip button on every card. If all cards correctly play the 'flipping' animation, this aspect of the feature is functioning as expected.
* Log into MongoDB and browse the 'Decks' collection. Find the deck that is currently being played. 
* Cross reference the cards displayed on the Play page with the 'deck_card_fronts' and 'deck_card_backs' for the corresponding deck. If the data matches, this aspect of the feature is functioning as expected.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

 ### **Play Deck - Reset Deck - Button**
  Expected Functionality:
* The Reset Deck buttons re-initialise the Play Deck page, returning it to its original state.

Testing Procedure:
* Navigate to the Play page for any deck.
* Flip any combination of the cards on the Play page.
* Click either of the Reset Deck buttons. If all cards on the Play deck page return to their original state, this feature is functioning as expected.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

 ---
## **Feature Set - Report Deck**
---
 ### **Report Deck - Deck Display**
 Expected Functionality:
* The Deck Display on the Report Deck page should present the user with a render of the main details of the deck being reported in a card format. 

Testing Procedure:
* Navigate to the Report Deck page for any deck and observe the Deck Display. If the details of the deck are displayed correctly this feature is functioning as expected.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

### **Report Deck - Information Display**
Expected Functionality:
* The Information Display should display an overview of the Report process to the user on large screens.

Testing Procedure:
* Navigate to the Report Deck page for any deck while using a large screen and observe the Information Display. If the Information Display is visible, this aspect of the feature is functioning as expecting.
* Navigate to the Report Deck page for any deck while using a small screen and observe the Information Display. If the Information Display is not visible, this aspect of the feature is functioning as expecting.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

### **Report Deck - Form**
Expected Functionality:
* Clicking any of the 6 checkboxes will cause that checkbox to be filled with a 'tick'.
* Filling out the form in the accepted manner should allow the user to click the 'Report' button. The user should then be redirected to their 'My Decks' page and a flash message should state 'Thanks, your report has been submitted!'.
* If the user does not match the required format of the input, the line under the Report Details input should turn red, and clicking the 'Report' button should prompt the user to change their input.

Testing Procedure:
* Fill out the 'Report' form in the accepted manner.
* Click the 'Report' button.
* If clicking the button redirects to the user's My Decks page and displays a flash message that states 'Thanks, your report has been submitted!', this aspect of the feature is functioning as expected.
* Fill out the 'Report form in a manner that is not acceptable (e.g. Enter Report Details that are less than 20 characters.).
* Click the 'Report' button.
* If upon clicking the Report button a prompt appears requesting changes be made to the form, this aspect of the feature is functioning as expected.

Current Status: <span style="color:green">**FUNCTIONAL**</span>

---
## **Feature Set - Admin Utility - User Management**
---
### **User Management - Administrator Display**
Expected Functionality:
* The Administrator Display should show a tabular set of data of all of the administrators on the site.

Testing Procedure:
* Navigate to the User Management Page, which requires administrator access.
* Log into MongoDB and browse the 'Users' collection.
* Cross reference the data displayed on the Administrator Display with the data found in the 'Users' collection. If the appropriate data is being displayed, this feature is functioning as expected. 

Current Status: <span style="color:green">**FUNCTIONAL**</span>

### **User Management - Standard Users Display**
Expected Functionality:
* The Standard Users Display should show a tabular set of data of all of the standard users on the site.

Testing Procedure:
* Navigate to the User Management Page, which requires administrator access.
* Log into MongoDB and browse the 'Users' collection.
* Cross reference the data displayed on the Standard Users Display with the data found in the 'Users' collection. If the appropriate data is being displayed, this feature is functioning as expected. 

Current Status: <span style="color:green">**FUNCTIONAL**</span>

---
## **Feature Set - Admin Utility - Deck Management**

---
### **Deck Management - All Decks Display**
Expected Functionality:
* The All Decks Display should show a tabular set of data of all of the decks on the site.

Testing Procedure:
* Navigate to the Deck Management Page, which requires administrator access.
* Log into MongoDB and browse the 'Decks' collection.
* Cross reference the data displayed on the All Decks Display with the data found in the 'Decks' collection. If the appropriate data is being displayed, this feature is functioning as expected. 

Current Status: <span style="color:green">**FUNCTIONAL**</span>

---
## **Feature Set - Admin Utility - Report Management**

---
### **Report Management - Open Reports Display**
Expected Functionality:
* The Open Reports Display should show a collapsible element for each open report as found in the MongoDB 'Reports' collection.

Testing Procedure:
* Navigate to the Report Management Page, which requires administrator access.
* Log into MongoDB and browse the 'Reports' collection.
* Cross reference the data displayed on the Open Reports Display with the data found in the 'Reports' collection. If the appropriate data is being displayed, this feature is functioning as expected. 

Current Status: <span style="color:green">**FUNCTIONAL**</span>

### **Report Management - Archived Reports**
Expected Functionality:
* The Archived Reports Display should show a collapsible element for each open report as found in the MongoDB 'Reports' collection.

Testing Procedure:
* Navigate to the Report Archive page, which requires administrator access.
* Log into MongoDB and browse the 'Reports' collection.
* Cross reference the data displayed on the Archived Reports Display with the data found in the 'Reports' collection. If the appropriate data is being displayed, this feature is functioning as expected. 

Current Status: <span style="color:green">**FUNCTIONAL**</span>

---
---
 ## **Browser Compatibility**
 The following section documents the compatibility of the site with a variety of browsers.
 ---
 ---
  ---
## **Browser Compatibility - Google Chrome**
 ---
**Testing Status:** <span style="color:green">**COMPLETE**</span>

**Testing Result:** <span style="color:green">**FULLY COMPATIBLE**</span>

---
## **Browser Compatibility - Firefox**
 ---
**Testing Status:** <span style="color:green">**COMPLETE**</span>

**Testing Result:** <span style="color:green">**FULLY COMPATIBLE**</span>

---
## **Browser Compatibility - Microsoft Edge**
 ---
**Testing Status:** <span style="color:green">**COMPLETE**</span>

**Testing Result:** <span style="color:green">**FULLY COMPATIBLE**</span>

---
## **Browser Compatibility - Internet Explorer**
 ---
**Testing Status:** <span style="color:green">**COMPLETE**</span>

**Testing Result:** <span style="color:red">**INCOMPATIBLE**</span>

**Details:**
* Internet Explorer does not support the animation used to 'flip' cards, thereby making all Play screens unusable.
* The Materialize library of JavaScript components is not compatible with Internet explorer, meaning that all elements using the library do not function.
* Due to the sweeping nature of the incompatibilities and the fact that Microsoft is retiring Internet Explorer, no attempt to make this website compatible with the browser will be made.

---
## **Browser Compatibility - Safari**
 ---
**Testing Status:** <span style="color:red">**INCOMPLETE**</span>

**Testing Result:** <span style="color:orange">**UNKNOWN**</span>

---
---
 ## **Code Validation**
 The following section documents the validation test results for code document.
 ---
 ---
 ---
## **Code Validation - App.py**
 ---
**Testing Method:** PEP8(Pycodestyle) Linter

**Testing Result:** <span style="color:green">**NO ERRORS**</span>

 ---
## **Code Validation - Style.css**
 ---
**Testing Method:** The W3C CSS Validation Service https://jigsaw.w3.org/css-validator/validator

**Testing Result:** <span style="color:green">**NO ERRORS**</span>

 ---
## **Code Validation - Script.js**
 ---
**Testing Method:** JSHint https://jshint.com/ NOTE: The following code must be inserted at the start of the JSHint document to avoid errors with ES6:

 ` /*jshint esversion: 6 */ `

**Testing Result:** <span style="color:green">**ONLY FALSE ERRORS**</span>

 ---
## **Code Validation - Template - 404_error.html**
 ---
**Testing Method:** The W3C Markup Validation Service https://validator.w3.org/#validate_by_input

**Testing Result:** <span style="color:green">**NO ERRORS**</span>

 ---
## **Code Validation - Template - 500_error.html**
 ---
**Testing Method:** The W3C Markup Validation Service https://validator.w3.org/#validate_by_input

**Testing Result:** <span style="color:green">**NO ERRORS**</span>

 ---
## **Code Validation - Template - admin_view_decks.html**
 ---
**Testing Method:** The W3C Markup Validation Service https://validator.w3.org/#validate_by_input

**Testing Result:** <span style="color:green">**NO ERRORS**</span>

 ---
## **Code Validation - Template - all_decks.html**
 ---
**Testing Method:** The W3C Markup Validation Service https://validator.w3.org/#validate_by_input

**Testing Result:** <span style="color:green">**NO ERRORS**</span>

 ---
## **Code Validation - Template - create_an_account.html**
 ---
**Testing Method:** The W3C Markup Validation Service https://validator.w3.org/#validate_by_input

**Testing Result:** <span style="color:green">**NO ERRORS**</span>

---
## **Code Validation - Template - create_deck.html**
 ---
**Testing Method:** The W3C Markup Validation Service https://validator.w3.org/#validate_by_input

**Testing Result:** <span style="color:green">**NO ERRORS**</span>

---
## **Code Validation - Template - create_new_admin.html**
 ---
**Testing Method:** The W3C Markup Validation Service https://validator.w3.org/#validate_by_input

**Testing Result:** <span style="color:green">**NO ERRORS**</span>

---
## **Code Validation - Template - create_report.html**
 ---
**Testing Method:** The W3C Markup Validation Service https://validator.w3.org/#validate_by_input

**Testing Result:** <span style="color:red">**ERRORS**</span>

---
## **Code Validation - Template - deck_management.html**
 ---
**Testing Method:** The W3C Markup Validation Service https://validator.w3.org/#validate_by_input

**Testing Result:** <span style="color:green">**NO ERRORS**</span>

---
## **Code Validation - Template - edit_deck.html**
 ---
**Testing Method:** The W3C Markup Validation Service https://validator.w3.org/#validate_by_input

**Testing Result:** <span style="color:green">**NO ERRORS**</span>

---
## **Code Validation - Template - index.html**
 ---
**Testing Method:** The W3C Markup Validation Service https://validator.w3.org/#validate_by_input

**Testing Result:** <span style="color:orange">**ONE ERROR - REPEATED**</span>

**Error Details:** Element br not allowed as child of element ul in this context.

**Error Handling:** Due to the late discovery of this error, it can not be rectified without breaking the deck display. In the future the br tags can be removed and replaced with Materialize grid elements. This error is present on all pages where a deck is displayed, but will only be referenced here.

---
## **Code Validation - Template - login.html**
 ---
**Testing Method:** The W3C Markup Validation Service https://validator.w3.org/#validate_by_input

**Testing Result:** <span style="color:green">**NO ERRORS**</span>

---
## **Code Validation - Template - my_decks.html**
 ---
**Testing Method:** The W3C Markup Validation Service https://validator.w3.org/#validate_by_input

**Testing Result:** <span style="color:green">**NO ERRORS**</span>

---
## **Code Validation - Template - play_deck_anonymous.html**
 ---
**Testing Method:** The W3C Markup Validation Service https://validator.w3.org/#validate_by_input

**Testing Result:** <span style="color:green">**NO ERRORS**</span>

---
## **Code Validation - Template - play_deck.html**
 ---
**Testing Method:** The W3C Markup Validation Service https://validator.w3.org/#validate_by_input

**Testing Result:** <span style="color:green">**NO ERRORS**</span>

---
