# Zad 1
# class Comment:
#     def __init__(self,username,content,likes=0):
#         self.username = username
#         self.content = content
#         self.likes = likes

# comm = Comment("John", "Hello World") 
# print(comm.username)  # Output: John
# print(comm.content)   # Output: Hello World
# print(comm.likes)     # Output: 0

# Zad 2 
class Party:
    def __init_(self):
        self.people = []

party = Party()
line = input()
while line != "End":
    party.people.append(line)
    line = input()
print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")