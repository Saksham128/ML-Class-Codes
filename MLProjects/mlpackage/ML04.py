import os
print("os.name = " ,  os.name  )
print("os.getenv('PATH')= ", os.getenv('PATH')  )
print("os.getcwd() = ", os.getcwd()   )

os.mkdir("MyDir")
print("New Folder created successfully.")

print("os.getcwd() = ", os.getcwd()   )
os.chdir("MyDir")
print("Folder locaton chaged.")
print("os.getcwd() = ", os.getcwd()   )

os.listdir()
os.chdir("..")
os.rmdir('MyDir')
print("Folder deleted.")