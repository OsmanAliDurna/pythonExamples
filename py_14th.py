passage = "Uzun uzun yazmak istemeyebilirsiniz benim gibi."

query = passage.find("bay")
query2 = passage.find("uzun")

print(query)        # bay kelimesi olmadığından -1 döner.
print(query2)       # uzun kelimesi 5. indexten başladığı için 5 döner. 

isThereStartwith = passage.startswith("b")
isThereStartwith2 = passage.startswith("U")

print(isThereStartwith)
print(isThereStartwith2)

isThereEndwith = passage.endswith("n")
isThereEndwith2 = passage.endswith(".")

print(isThereEndwith)
print(isThereEndwith2)

passageReplaced = passage.replace("istemeyebilirsiniz","istemiyorsunuz").replace("."," di mi.")
passageCenter = passage.center(50,"*")

print(passage)
print(passageReplaced)
print(len(passage))
print(passageCenter)