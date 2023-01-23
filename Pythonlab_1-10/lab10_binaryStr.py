try:
    inp1 = "0b110001"
except:
    print("sahi number daal")

op = (int(inp1, 2))
if op % 2 == 0:
    print("its even")
else:
    print("its odd")
