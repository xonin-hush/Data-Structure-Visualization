numbers = numbers.split()
    numbersList = [int(i) for i in numbers]
    print(numbersList)
    root = None
    for key in numbersList:
        root = insert(root, key)
    visualizeInOrder(root)
    label.config(text="Check your files...Thank you :)",font= ('Helvetica 13'))