extension = input("Media type: ").strip().lower()

if extension.endswith(".gif"):
    print("image/gif")
elif extension.endswith(".jpg"):
    print("image/jpg")
elif extension.endswith(".jpeg"):
    print("image/jpeg")
elif extension.endswith(".png"):
    print("image/png")
elif extension.endswith(".pdf"):
    print("document/pdf")
elif extension.endswith(".txt"):
    print("text/txt")
elif extension.endswith(".zip"):
    print("archive/zip")
else:
    print("application/octet-stream")
    
