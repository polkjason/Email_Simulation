### --- OOP Email Simulator --- ###
#This application has been named StandPoint as a synonym of Outlook.
#It's purpose is to simulate an email application. Currently, the application is capable of managing inbox,
# deleted, and spam mailboxes. The inbox, deleted, and spam mailboxes derive their base functionality from a mailbox class.
# Currently, only the inbox subclass has any methods unique to it, but parking_lot.txt contains information on
# further features to be added only to deleted and spam mailboxes that are unique to each.
#A factory design pattern was intended, but requirements of the task stated for the email class to have methods within it.
# Regardless, OOP encapsulation is adequately established to ensure only mailbox can access email data, and
# StandPointApplication only can manage mailboxes.
#Some methods are put in place due to belief they be useful either immediately when they were written or in future refactoring.
#Splash text was also put in for added flare when starting the application.
#The application is also designed to run using app.run() method to ensure cleaner execution and design.
# The app.display_all_mailboxes() method is only included for testing and specifically as a means to quickly review the
# results of all the actions taken by the user when running the application.
###################################

class Email:

    def __init__(self, email_id, email_address, subject_line, email_content):
        self._email_id = email_id
        self._email_address = email_address
        self._subject_line = subject_line
        self._email_content = email_content
        self._has_been_read = False
        self._deleted = False
        self._spam = False

    def set_email_id(self, email_id):
        self._email_id = email_id

    def get_email_id(self):
        return self._email_id

    def get_email_address(self):
        return self._email_address

    def get_subject_line(self):
        return self._subject_line

    def get_email_content(self):
        return self._email_content

    def is_read(self):
        return self._has_been_read

    def is_deleted(self):
        return self._deleted

    def is_spam(self):
        return self._spam

    def mark_as_read(self):
        self._has_been_read = True

    def mark_as_deleted(self):
        self._deleted = True

    def mark_as_spam(self):
        self._spam = True

    #Displays the entire email, including email_content
    def to_string(self):
        return_string = f"Email ID: {self._email_id} \n"
        return_string += f"Email Address: {self._email_address} \n" 
        return_string += f"Subject Line: {self._subject_line} \n"

        if(self.is_read() == True):
            return_string += f" Email marked as read \n"
        else:
            return_string += f"Email marked as unread \n"

        if(self.is_deleted() == True):
            return_string += f"Email marked as deleted \n"

        if(self.is_spam() == True):
            return_string += f"Email marked as spam \n"

        return_string += f"Email Content: \n"
        return_string += f"{self._email_content} \n"

        return return_string

    #Displays just the email_id, email_address, subject_line of the email, and whether it has been read.
    # Preview_email was chosen as the name because I couldn't think of a better method name.
    def preview_email(self):
        return_string = f"Email ID: {self._email_id} \n" 
        return_string += f"Subject Line: {self._subject_line} \n"

        return return_string

class MailBox:

    def __init__(self, mailbox_name = "mailbox"):
        self._emails = []
        self._emails_count = 0
        self._mailbox_name = mailbox_name

    def get_emails_count(self):
        return self._emails_count

    def get_mailbox_name(self):
        return self._mailbox_name

    def create_email(self, email_address, subject_line, email_content):
        new_email_id = len(self._emails) + 1
        email = Email(new_email_id, email_address, subject_line, email_content)
        self._emails.append(email)
        self._emails_count += 1

    def list_emails(self):

        if(self._emails_count > 0):
            for e in self._emails:
                print(e.preview_email())
        else:
            print(f"There are no emails to show.")

    def find_email_index(self, email_id):
        for i in range(0, self._emails_count):
            if(email_id == self._emails[i].get_email_id()):
                return i
        
        #Return -1 if email not found.
        return -1            

    def read_email(self, email_id):

        email_index = self.find_email_index(email_id)
        if(email_index == -1):
            print(f"No email exists with email ID {email_id}.")
        else:
            if(self._emails[email_index].is_read() == False):
                print(f"Email ID {email_id} is currently Unread. Now marking as read.")
                self._emails[email_index].mark_as_read()

            print(self._emails[email_index].to_string())

    #Correct the email ids to make the counting contiguous.
    # Generally, this will be called after being removed or added to
    # a different email list
    def condense_email_ids(self):
        current_emails_count = len(self._emails)
        
        for i in range(0, current_emails_count):
            self._emails[i].set_email_id(i + 1)

    def add_email(self, email):
        self._emails.append(email)
        self._emails_count += 1
        self.condense_email_ids()

    def remove_email_by_email_id(self, email_id):
        email_index = self.find_email_index(email_id)
        if(email_index == -1):
            print(f"No email exists with email ID {email_id}.")
            return Email(-1, "", "", "")
        else:
            email = self._emails[email_index]
            self._emails.remove(self._emails[email_index])
            self._emails_count -= 1
            self.condense_email_ids()
            return email

    def email_id_exists(self, email_id):
        for i in range(0, self._emails_count):
            if(email_id == self._emails[i].get_email_id()):
                return True
        
        #Return -1 if email not found.
        return False

    def to_string(self):
        if(self._emails_count == 0):
            print(f"The mailbox named {self.get_mailbox_name()} is empty.")
        else:
            for e in self._emails:
                print(e.to_string())

class Inbox(MailBox):

    def __init__(self, mailbox_name = "inbox"):
        super().__init__(mailbox_name)

    def is_unread_emails(self):
        for e in self._emails:
            if(e.is_read() == False):
                return True
        return False
                
    def preview_unread_emails(self):
        display_string = ""
        for e in self._emails:
            if(e.is_read() == False):
                display_string += e.preview_email()
        
        if(display_string == ""):
            display_string = f"There are currently no unread messages."
        
        print(display_string)

class Deleted(MailBox):
    def __init__(self, mailbox_name = "deleted"):
        super().__init__(mailbox_name)

class Spam(MailBox):
    def __init__(self, mailbox_name = "spam"):
        super().__init__(mailbox_name)

class StandPointApplication:
    INBOX = "inbox"
    DELETED = "deleted"
    SPAM = "spam"

    def __init__(self):
        self.__inbox = Inbox()
        self.__deleted = Deleted()
        self.__spam = Spam()

    def run(self):
        self.display_splash_text()

        #self.populate_inbox()

        while True:
            user_choice = int(input('''\nWould you like to:
            1. Read an email
            2. View unread emails
            3. Quit application

            Enter selection: '''))
            
            if user_choice == 1:
                self.list_emails_menu()
                # add logic here to read an email
                
            elif user_choice == 2:
                self.display_unread_emails_menu()
                # add logic here to view unread emails
                    
            elif user_choice == 3:
                print(f"Goodbye")
                break
                # add logic here to quit appplication

            else:
                print("Oops - incorrect input.")

    def display_splash_text(self):
        display_splash = f"--------------------StandPoint-------------------- \n"
        display_splash += f"Welcome. \n"
        display_splash += f"This application is a simulation of an email application. \n"
        display_splash += f"---------------By: Jason Polk--------------------- \n"
        display_splash += f"---------------Date: 2024------------------------- \n"

        print(display_splash)

    def display_inbox_unread(self):
        if(self.__inbox.get_emails_count() == 0):
            print("Inbox is currently empty.")
        else:
            self.__inbox.preview_unread_emails()

    def display_inbox(self):
        if(self.__inbox.get_emails_count() == 0):
            print("Inbox is currently empty.")
        else:
            self.__inbox.list_emails()

    def display_deleted(self):
        if(self.__deleted.get_emails_count() == 0):
            print("Deleted is currently empty.")
        else:
            self.__deleted.list_emails()

    def display_spam(self):
        if(self.__spam.get_emails_count() == 0):
            print("Inbox is currently empty.")
        else:
            self.__spam.list_emails()

    def display_unread_emails_menu(self):
        print("Listing unread emails...")
        self.display_inbox_unread()
        if(self.__inbox.is_unread_emails() == True):
            self.read_email_menu(self.__inbox)

    def list_emails_menu(self):

        while(True):
            user_choice = int(input('''\nWould you like to:
            1. List unread emails
            2. List all inbox emails
            3. List all deleted emails
            4. List all spam emails
            5. Quit to main menu

            Enter selection: '''))

            if user_choice == 1:
                self.display_unread_emails_menu()
                # add logic here to read an email
                
            elif user_choice == 2:
                self.display_inbox()
                if(self.__inbox.get_emails_count() != 0):
                    self.read_email_menu(self.__inbox)
                # add logic here to view unread emails

            elif user_choice == 3:
                self.display_deleted()
                if(self.__deleted.get_emails_count() != 0):
                    self.read_email_menu(self.__deleted)
                # add logic here to read an email

            elif user_choice == 4:
                self.display_spam()
                if(self.__spam.get_emails_count() != 0):
                    self.read_email_menu(self.__spam)
                # add logic here to read an email
                    
            elif user_choice == 5:
                break
                # add logic here to quit appplication

            else:
                print("Oops - incorrect input.")

    def read_email_menu(self, mailbox):
        
        while(True):
            user_choice = int(input('''\nEnter the ID of the email you wish to read:
            Enter -1 to return to previous menu.            

            Enter selection: '''))

            if(user_choice == -1):
                print(f"Returning to previous menu.")
                return
            else:
                #mailbox.read_email(user_choice)
                self.select_email_option_menu(mailbox, user_choice)
                return

    def read_email(self, mailbox, email_id):
        mailbox.read_email(email_id)

    def select_email_option_menu(self, mailbox, email_id):
        while True:
            print(f"Options for email with ID {email_id}:")
            menu = f"\nWould you like to: \n"
            menu += f"1. Read email \n"

            if(mailbox.get_mailbox_name() == self.INBOX):
                menu += f"2. Delete email \n"
                menu += f"3. Move to spam \n"
                menu += f"4. Return to previous menu \n"
            else:
                menu += f"2. Return to previous menu \n"
            menu += f"\nEnter selection: "

            user_choice = int(input(menu))

            """
            = int(input('''\nWould you like to:
            1. Read email
            2. Delete email
            3. Move to spam
            4. Return to previous menu

            Enter selection: '''))
            """

            if user_choice == 1:
                self.read_email(self.__inbox, email_id)
                # add logic here to read an email

            if user_choice == 2:
                if(mailbox.get_mailbox_name() == self.INBOX):
                    self.delete_an_inbox_email_by_id(email_id)
                    return
                else:
                    return
                # add logic here to read an email

            if user_choice == 3 and mailbox.get_mailbox_name() == self.INBOX:
                self.move_email_from_inbox_to_spam_by_id(email_id)
                return
                # add logic here to read an email

            if user_choice == 4 and mailbox.get_mailbox_name() == self.INBOX:
                return
                # add logic here to read an email

    def delete_an_inbox_email_by_id(self, email_id):
        email = self.__inbox.remove_email_by_email_id(email_id)
        email.mark_as_deleted()
        print(f"Email with ID {email_id} has been deleted.")
        print(f"Returning to perevious menu.")
        self.__deleted.add_email(email)

    def move_email_from_inbox_to_spam_by_id(self, email_id):
        email = self.__inbox.remove_email_by_email_id(email_id)
        email.mark_as_spam()
        print(f"Email with ID {email_id} has been moved to spam.")
        print(f"Returning to perevious menu.")
        self.__spam.add_email(email)

    def create_email_to_inbox(self, email_address, subject_line, email_content):
        self.__inbox.create_email(email_address, subject_line, email_content)

    #Used for testing
    def display_all_mailboxes(self):
        print()
        print(f"The following are the contents of all mailboxes.")
        print()
        print(f"Now displaying all contents of the mailbox named {self.__inbox.get_mailbox_name()}:")
        self.__inbox.to_string()
        print()

        print(f"Now displaying all contents of the mailbox named {self.__deleted.get_mailbox_name()}:")
        self.__deleted.to_string()
        print()

        print(f"Now displaying all contents of the mailbox named {self.__spam.get_mailbox_name()}:")
        self.__spam.to_string()
        print()                

#Used for testing
def populate_inbox(app):
        # Create 3 sample emails and add it to the Inbox list.
        app.create_email_to_inbox("test_email@sebootcamp.com", "Welcome to HyperionDev", "Hello, Welcome to HyperionDev!")
        app.create_email_to_inbox("test_email@sebootcamp.com", "Great Work on the Bootcamp", "Hello, Great work on the Bootcamp!")
        app.create_email_to_inbox("test_email@sebootcamp.com", "Your Excellent Marks",\
            "Hello, Congratulations on achieving excellent marks in the bootcamp!")


app = StandPointApplication()

#Used for testing
populate_inbox(app)

app.run()

#Used for testing to quickly view the results of all actions taken while the StandPoint application was running.
app.display_all_mailboxes()

