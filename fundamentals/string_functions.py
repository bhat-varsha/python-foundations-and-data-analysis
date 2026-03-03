name="varsha"
print(len(name)) # to count the length
reva="xuniversity  "
print(reva.strip("x")) # to remove the x
 #or if we give null ,it will remove the space
print(reva.replace("r","R").strip()) #to replace the word
print(reva.find("i")) #if i ask the position of number which is not ther it give -1
print(reva.index("v")) #in index it gives error when i ask the element which is not present


print(reva.isdigit()) # to check if the string only contain digit.if all characters are digits
#output boolean for both
Reva="college"
print(Reva.isalpha()) #to check if the string only contain alphabets

"""
len, find, index, isdigit, isalpha are built-in functions or methods, not keywords.
They can be called directly without defining,
but you can technically use them as variable names (not recommended, bad practice).

Keywords: reserved words with special meaning → if, def, for
Built-in functions/methods: ready-made functions → len(), print(), find(), index(), isdigit(), isalpha()
String methods: functions specific to string objects 
like find(), index(), strip(), replace(), isdigit(), isalpha()

So the main difference is: 
keywords are reserved and untouchable, 
built-in functions are predefined but technically replaceable.
bot are predeifned but built in function can be used as varibale name but not keywords

"""
