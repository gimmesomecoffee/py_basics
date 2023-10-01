# py_basics
I will put my notes here about python:

Jupyter - It works locally on your computer and u can execute python commands there. 

# f-strings
It's a new string formatting, very handy.
```
num = 10
print(f"2.25 times {num} is {2.25 * num:.2f})
```
Result will be: 22.50. To use f string formatting you need to put **f** before quote and in curly brackets put variables, methods or some math. You can also use formatting types, in our example I used **:.2f** It allowed me to precise how many decimal places I would have. To check whole list of formatting types, look for "formatting types python"
## Libraries
- **Pandas** It is python library used for working with data sets, It has functions for analyzing, cleaning, exploring and manipulating data. <br>

**How to use Pandas** <br>
pandas.read_csv("") - It will open the file, but you need to print it also. By default it's separate by coma ",", if we want to change it, we use **sep=""** for a second argument. If we know that our csv doesn't have header we have to use for an argument **header = None**, it will make default header, name it from 0, 1, 2...
```
df1 = pandas.read_csv("test.csv", sep=";")
df1
```
pandas.read_json("test.json") - here we need to remember to set index. set_index("ID")<br>
pandas.read_excel("test.xlsx", sheet_name=0) - here remember to set which sheet we want to read
iloc[] - we can filter data by this. We can use numbers of columns and rows or their names.
 >[!IMPORTANT]
 >In below example the second argument "1:3" will show only 2 columns, bcs it cut the last. It happends only when we put numbers instead of names of columns
```
df1.iloc[1:4,1:3]
```