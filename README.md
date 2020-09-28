## MerWebPy (1.0.0)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/b72632b30f3940aba091eb22c0113924)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=kessec/MerriamWebsterPy&amp;utm_campaign=Badge_Grade)

A Python wrapper for the Merriam-Webster Dictionary API that lets you quickly query the database.

Requires a key from the Merriam-Webster Dictionary Developer Portal.

#### Example of wrapper usage:
```python
while(True):
    k = input("What word do you want queryed? ")
    y = query_database(_KEY,k)
    print("Word: " + y["word"])
    print("Defintion: " + y["definition"])
    print("Type: " + y["type"])
    print("Offensive: " + y["offensive"])
```
