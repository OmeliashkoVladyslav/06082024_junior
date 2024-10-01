with open('file.txt', mode='r') as source_file, open('file.txt2', mode='w') as dest_file:
    content = source_file.read()
    print(content)
    dest_file.write(content)
