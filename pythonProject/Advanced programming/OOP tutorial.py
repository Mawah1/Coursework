#  Every class should have a set of defined attributes (in our email example, an email
# has subject, body, and recipients attributes) and a set of defined methods (in our
# example, only an “init” method was defined)
# • The init method is especially important and is called the constructor. It is used to
# initialize all the attributes belonging to an object.
# • When defining classes, the parameter “self” is always used to refer to
# attributes/methods belonging to the object itself. 7
# Why we need self
# • Remember that classes only define the template that will be used later on
# • The self keyword can be understood as a stand in for any object created from this
# template
# • self should always be the first keyword of any method belonging to the class
# template.
# • dot notation can be used to set or access any attribute/behaviour belonging to that
## object
class Email:
    def __init__(self, subject, body, recipients):
        self.subject = subject
        self.body = body
        self.recipients = recipients

    def __str__(self):
        return f"Subject: {self.subject}\nBody: {self.body}\nRecipients: {', '.join(self.recipients)}"
test = Email("Hello World", "This is a test email.",
["example1@example.com", "example2@example.com"])
print(test)

import json

python_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
json_string = json.dumps(python_dict)
print(json_string)  # Output will be a JSON formatted string




