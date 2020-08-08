# library_managment_software 

About:

Library Managment Software/Application

Description : 

It is a python programme designed for library managment which provides several features required to automatically managing an library.

Requirements :

python 3, time module.

Modes :

The application has two modes: 1.Admin 2.User 

1.Admin mode : this mode provides all the functions this application can perform. To login as admin, you require an 
adminkey which is automatically generated at the time of setup. It can be changed manually after the setup has completed. 

2.User mode : this mode allows only user-friendly functions i.e. Display all and currently availale books, lend books and return books.

Functions
1. Dislay all books of library --> Shows all books library have(Even the book is currently not available).
2. Display all available books in library --> Shows books available for lend.
3. Lend book from library --> Borrow books from library.
4. Return the lend book.
5. Delete books from library --> Delete books from library permanently. The books deleted from library will not display anywere, until added again. To delete books you need enter an del-key(deletion key) which is set by admin while initilaizing.
6. Display all lended book --> It shows books taken on lend with who has taken it.
7. Add new books to library.
8. Change keys --> With this you can change the secret key(admin key) and deletion key.

NOTE: Initialy the application generates admin key and deletion key automatically. These keys are required for root access of the application.

Working:

Step 0: Initallly, set up your library, application provides two ways to complete this step:

 0.1.Set up you library by entering your library name and initial stock of books in your library by entering total number of books and their name.(Recommanded)
 
                                  or
 
 0.2.Set your library name and initail book stock directlly in software code.

[NOTE: This step is performed by admin]

[NOTE: Step 0 is a one time process, just to initialize. Using 0.1 you have to enter your admin details through input() and using 0.2 you directly set all admin details in main software code.]

Step 1:Once your library is set up, enter you want to enter as admin or user.

Step 2: Perform the task you want to.

Step 3: Exit=0.  
>> Once you exit after your task, the programme again starts from step 1.

Made by
Prabal Gupta

