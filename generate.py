import re

banner = """
 _    _               _   _     _        
| |  | |             | | (_)   | |       
| |  | | ___  _ __ __| |  _ ___| |_ _ __ 
| |/\| |/ _ \| '__/ _` | | / __| __| '__|
\  /\  / (_) | | | (_| | | \__ \ |_| |   
 \/  \/ \___/|_|  \__,_|_|_|___/\__|_|   
                                         """

words = []

def getData(prompts):
    inputs = [input(prompt+": ") for prompt in prompts]
    for inp in inputs:
        if inp:
            if re.match("^\d{1,2}/\d{1,2}/\d{4}$", inp):
                words.extend(inp.lower().split("/"))
            words.extend(inp.lower().split(" "))

def addPerson():
    prompts = ["Name", "Relation", "Date of birth", "Other words"]
    getData(prompts)
    
def addAnimal():
    prompts = ["Name", "Species", "Date of birth", "Other words"]
    getData(prompts)

def addLocation():
    prompts = ["Name", "Country", "Date",  "Other words"]
    getData(prompts)

def addWorkplace():
    prompts = ["Name", "City", "Date",  "Other words"]
    getData(prompts)

def addSchool():
    prompts = ["Name", "City", "Date", "Class", "Other words"]
    getData(prompts)

def addDate():
    prompts = ["Description", "Date", "Other words"]
    getData(prompts)

def addOldPassword():
    prompts = ["Password"]
    getData(prompts)

def addOtherWord():
    prompts = ["Words"]
    getData(prompts)

def geneateList():
    filename = input("Filename: ")
    passwords = []
    for word1 in words:
        passwords.append(word1)
        passwords.append(word1[0].upper()+word1[1:])
        for word2 in words:
            if (word1 == word2):
                continue
            passwords.append(word1+word2)
            passwords.append(word1[0].upper()+word1[1:]+word2)
            passwords.append(word1[0].upper()+word1[1:]+word2[0].upper()+word2[1:])
            for word3 in words:
                if (word2 == word3):
                    continue
                passwords.append(word1+word2+word3)
                passwords.append(word1[0].upper()+word1[1:]+word2+word3)
                passwords.append(word1[0].upper()+word1[1:]+word2[0].upper()+word2[1:]+word3[0].upper()+word3[1:])
    
    with open(filename, "w") as f:
        for password in passwords:
            for i in range(2010, 2025):
                f.write(password+str(i)+"\n")
                f.write(password+str(i)+"!\n")
                f.write(password+"\n")
                f.write(password+"!\n")
    print("Done! Happy cracking!")
    exit(0)

commands = [
    ("Add person", addPerson),
    ("Add animal", addAnimal),
    ("Add location", addLocation),
    ("Add workplace", addWorkplace),
    ("Add school", addSchool),
    ("Add date", addDate),
    ("Add old password", addOldPassword),
    ("Add other word", addOtherWord),
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
    except Exception as e:
        print(e)
        #print("Invalid option")

def main():
    print(banner)
    while True:
        print(menu())
        option = input("> ")
        parseOption(option)

if __name__ == "__main__":
    main()
