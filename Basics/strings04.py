->Strings:
    Strings in python are surrounded by either single quotation marks,
    or double quotation marks.

    immutable-> xx modify xx delete xx add xx

 but strings can be:
     indexed
     sliced
     concatenated
     iterated
     <class str>

->Multiline Strings:
    You can assign a multiline string to a variable by using three quotes(""" ---------""")
    or three single quotes (''' --------- ''').

#tech = "python"
p  y  t  h  o  n
0  1  2  3  4  5  --> farward indeces
-6 -5 -4 -3 -2 -1 --> reverse indeces
This is what we call "SLICING".


->Slicing:
    You can return a range of characters by using the slice syntax.
    Specify the start index and the end index,
    separated by a colon, to return a part of the string.
    syntax:
        <strname>[<sindex> : <eindex>]
        print(tech[0:4]) # 0 1 2 3 --> pyth
        print(tech[:4])
        print(tech[2:])
        
        tech = "python and machine learning"
        <strname>[<sindex> : <eindex> : <step>]
        for forward accessing -> forward indexing
        print(tech[4:19:1]) #  4 5 6 7 8 ....... 18
        print(tech[4:19:2]) # 4 6 8 ........... 18
        print(tech[::2])
        for reverse accessing -> start index changes as end index and end as start.
        print(tech[12:2:-1])

->Concatenation:
    To concatenate, or combine, two strings you can use the + operator.
    a= "python"
    b= "language"
    print(a+b)

    c =3.7 -> xx
    c= "3.7"

->String literals:
    static storages
    %d -> int
    %f -> float
    %s -> str

     print("%s %s "(tech,c))
     print("%s %f "(tech,c))

name = "khan"
marks=70
 #khan has secured 70 marks
#khan has secured 70% marks
print("%s has secured %d marks" %(name,marks))
print("%s has secured %d %% marks" %(name,marks))

escape characters:
    %%
    \\

str(),repr() functions of strings:
    str() will not convert str to str
    repr() will convert str to str
    
        
        
        
        

 


