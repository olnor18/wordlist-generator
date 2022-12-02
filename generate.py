banner = """
 _    _               _   _     _        
| |  | |             | | (_)   | |       
| |  | | ___  _ __ __| |  _ ___| |_ _ __ 
| |/\| |/ _ \| '__/ _` | | / __| __| '__|
\  /\  / (_) | | | (_| | | \__ \ |_| |   
 \/  \/ \___/|_|  \__,_|_|_|___/\__|_|   
                                         """

words = []

def addPerson():
    prompts = ["Name", "Relation", "Other words"]
    inputs = [input(prompt+": ") for prompt in prompts]
    for inp in inputs:
        if inp:
            words.extend(inp.split(" "))
    
def addAnimal():
    pass

def addLocation():
    pass

def addWorkplace():
    pass

def addSchool():
    pass

def addDate():
    pass

def addOldPassword():
    pass

def addOtherWord():
    pass

def geneateList():
    filename = input("Filename: ")
    passwords = []
    for word1 in words:
        password.append(word1)
        for word2 in words:
            password.ap
    with open(filename, "w") as f:


commands = [
    ("Add person", addPerson),
    ("Add animal", addAnimal),
    ("Add location", addLocation),
    ("Add workplace", addWorkplace),
    ("Add school", addSchool),
    ("Add date", addDate),
    ("Add old password", addOldPassword),
    ("Add other word", addOtherWord)
    ("Generate list", geneateList)
]

def menu():
    return "===============================\n"+"\n".join([f"{i+1}) {c[0]}" for i, c in enumerate(commands)])

def parseOption(option):
    try:
        id = int(option) - 1
        command = commands[id]
        if command:
            command[1]()
    except KeyboardInterrupt:
        inp = input("Are you sure you want to quit? (y/N)")
        if inp.lower() == "y":
            exit(0)
    except:
        print("Invalid option")

def main():
    print(banner)
    while True:
        print(menu())
        option = input("> ")
        parseOption(option)

if __name__ == "__main__":
    main()
