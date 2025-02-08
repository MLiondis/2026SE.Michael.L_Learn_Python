type = input("Type? ")

if ".jpg" in type:
    print("image/jpeg")
elif ".jpeg" in type:
    print("image/jpeg")
elif ".gif" in type:
    print("image/gif")
elif ".png" in type:
    print("image/png")
elif ".pdf" in type:
    print("applicaition/pdf")
elif ".txt" in type:
    print("text/plain")
elif ".zip" in type:
    print("application/zip")
else:
    print("application/octet-stream")
