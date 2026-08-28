from datetime import datetime
from collections import UserList
from typing import Iterable
import json

MESSAGES_JSON_FILE = "messages.json"

class User:
    id = 0

    def __init__(self, first_name: str, last_name: str, phone_number: str) -> None:
        User.id += 1
        self.id = User.id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def to_json(self) -> dict:
            return {
                "id": self.id,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "phone_number": self.phone_number
            }

    def __str__(self) -> str:
        return f'{self.id} | {self.first_name} {self.last_name} | {self.phone_number}'

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

    def to_json(self) -> dict:
        return {
            "content": self.content,
            "sending_time": str(self.sending_time),
            "receiving_time": str(self.receiving_time),
            "author": self.author.to_json(),
            "recipient": self.recipient.to_json()
        }

    def __lt__(self, other: Message) -> bool:
        return self.sending_time < other.sending_time

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

    def save_to_file(self):
        with open(MESSAGES_JSON_FILE, "w") as json_file:
            json.dump(self.data, json_file, default=lambda o: o.to_json(), indent=2)

    def read_from_json(self):
        # id_set = set()
        # user_set = set()
        users_dict = {}
        message_list = []
        with open(MESSAGES_JSON_FILE) as json_file:
            json_data = json.load(json_file)
            for message_dict in json_data:
                author = None
                recipient = None
                author_id, recipient_id = message_dict['author']["id"], message_dict['recipient']["id"]
                if author_id in users_dict:
                    author = users_dict[author_id]
                else:
                    author_dict = message_dict["author"]
                    author = User(author_dict["first_name"], author_dict["last_name"], author_dict["phone_number"])
                    author.id = author_dict["id"]
                    users_dict[author.id] = author
                message_list.append(Message(message_dict['content'], author, None))
            return message_list
                    
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

        return sorted(list(user_set))

user_john = User("John", "Doe", "7678632482")
user_jane = User("Jane", "Doe", "0987765576")
user_jack = User("Jack", "Doe", "0987765576")

message_one = Message("Hello, Jane!", user_john, user_jane)
message_two = Message("Hello, John!", user_jane, user_john)
message_three = Message("How are you doing?", user_john, user_jane)

message_four = Message("Todo: finish homework", user_john, user_john)
message_five = Message("Hello, I'm Jack", user_jack, user_john)

messages = [message_one, message_two, message_three, message_four, message_five]

message_system = MessageSystem()
# message_system.save_to_file()
print(message_system.read_from_json())
# print(message_system.get_all_chats(user_john))
# for message in message_system.get_messages_between_users(user_john, user_jane):
#     print(message)





        
        




    