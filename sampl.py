#task-1  Read a File and Handle Errors 

try:
    
    # Try to open the file
    file = open("sample.txt", "r")
    
    for line in file:
        print(line.strip())
    file.close()

except:
    
    print("The file 'sample.txt' was not found.")


#task-2


text = input("Write something: ")

file = open("output.txt", "w")
file.write(text + "\n")
file.close()

more_text = input("Write more to add: ")

file = open("output.txt", "a")
file.write(more_text + "\n")
file.close()

file = open("output.txt", "r")
print("\nFile content:")
print(file.read())
file.close()
