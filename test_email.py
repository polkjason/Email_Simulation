import unittest
from email import Inbox


class TestEmail(unittest.TestCase):
    
    def test_inbox_create_emails(self):
        inbox = Inbox()
        
        
        inbox.create_email("test_email@sebootcamp.com", "Welcome to HyperionDev", "Hello, Welcome to HyperionDev!")

        #test email count in inbox
        self.assertEqual(inbox.get_emails_count(), 1)
        
        #test if an email id exists
        self.assertEqual(inbox.email_id_exists(1), 1)
    

if __name__ == '__main__':
    unittest.main()