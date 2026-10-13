#for  write a file using python

# with open("file_name.txt","w")as file:
#     file.write("hello Shalah")
# with open("file_name.txt","a")as file:
#         file.write("\n welcome to python")
with open("file_name.txt","r")as file:
    content = file.read()
    print(content)