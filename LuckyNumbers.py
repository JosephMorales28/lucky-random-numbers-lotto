#My own lucky random Numbers Lottery
import random

ultralotto=random.sample(range(1,59),6)
grandlotto=random.sample(range(1,56),6)
nationallotto=random.sample(range(1,43),6)
megalotto=random.sample(range(1,46),6)
superlotto=random.sample(range(1,50),6)

lotto=input("Select lotto you want to display:\n")
print(lotto)

if lotto == "ultralotto":
   print(f"Ultra lotto results:\n{ultralotto}")
elif lotto == "grandlotto":
   print(f"Grand lotto results:\n{grandlotto}")
elif lotto == "nationallotto":
   print(f"National lotto results:\n{nationallotto}")
elif lotto == "megalotto":
   print(f"Mega lotto results:\n{megalotto}")
elif lotto == "superlotto":
   print(f"Super lotto results:\n{superlotto}")
else:
   print("invalid keywords")
