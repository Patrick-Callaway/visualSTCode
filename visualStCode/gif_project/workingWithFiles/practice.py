# Moving the file cursor using seek()
with open('testFile.txt', 'r') as file:
  file.seek(10)  # Move to the 10th byte
  content = file.read()