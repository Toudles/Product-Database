For this project you will be re-writing the "product database" program from Assignment 08 using dictionaries. This will help you to compare and contrast how dictionaries and lists operate in similar yet different ways. You'll also notice that some tasks tend to be much easier (and more efficient!) to write with dictionaries, while others may be more challenging.

Next, you are going to write a dictionary implementation of the "product database" assignment. To start copy the following dictionary into your program:

inventory = {
                'soft drink': [0.99, 10],
                'onion rings': [1.29, 5],
                'small fries': [1.49, 20]
            }
Each 'key' in the dictionary is a product (string). Each 'key' has a value (list) which contains the price of that product in position 0 and the amount of that product in position 1.

You can access items in the dictionary using two sets of square brackets. For example:
  - print ("soft drinks cost:", inventory["soft drink"][0])
  - print ("we have:", inventory["soft drink"][1], "soft drinks at our store")
Your task is to add the following functionality to this program:
  - Overarching menu system
  = Search for a product
  = List all products
  = Add a product
  = Remove a product
  = Update a product
  = Report on all products
