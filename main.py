from datetime import datetime
from collections import UserList
from typing import Iterable

class User:
    def __init__(self, first_name: str, last_name: str, phone_number: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} | {self.phone_number}'

    def __repr__(self) -> str:
        return str(self)

class Message:
    def __init__(self, content: str, author: User, recipient: User) -> None:
        self.content = content
        self.author = author
        self.recipient = recipient
        self.sending_time = datetime.now()
        self.receiving_time = None

    def is_message_read(self) -> bool:
        return self.receiving_time is not None

    def mark_message_as_read(self):
        self.receiving_time = datetime.now()

    def __str__(self) -> str:
        return f"Message from [{self.author}] to [{self.recipient}] | '{self.content} {self.sending_time}'"

    def __repr__(self) -> str:
        return str(self)

class MessageSystem(UserList):
    def __init__(self, messages: list[Message] = []) -> None:
        super().__init__(messages)

    def get_messages_between_users(self, user_one: User, user_two: User) -> list[Message]:
        messages_list = []
        # Go through all the messages that are in the system
        for message in self:
            # In the message we need to get the information about sender and recipient
            author, recipient = message.author, message.recipient
            # Check if the message is between user_one and user_two
            if (author == user_one and recipient == user_two) or (author == user_two and recipient == user_one):
                messages_list.append(message)
        return messages_list

    def get_all_chats(self, user: User) -> list[User]:
        user_set = set()
        # Go through all the messages that are in the system
        for message in self:            
            # In the message we need to get the information about sender and recipient 
            author, recipient = message.author, message.recipient
            # Check when the user is author
            if user == author:
                user_set.add(recipient) 
            # Check when the user is recipient 
            if user == recipient:
                user_set.add(author)  
            # Check when the user is author and recipient

        return list(user_set)

user_john = User("John", "Doe", "7678632482")
user_jane = User("Jane", "Doe", "0987765576")
user_jack = User("Jack", "Doe", "0987765576")

message_one = Message("Hello, Jane!", user_john, user_jane)
message_two = Message("Hello, John!", user_jane, user_john)
message_three = Message("How are you doing?", user_john, user_jane)

message_four = Message("Todo: finish homework", user_john, user_john)
message_five = Message("Hello, I'm Jack", user_jack, user_john)

messages = [message_one, message_two, message_three, message_four, message_five]

message_system = MessageSystem(messages)
# print(message_system.get_all_chats(user_john))
for message in message_system.get_messages_between_users(user_john, user_jane):
    print(message)





        
        




    