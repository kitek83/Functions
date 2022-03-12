#arbitrary_keyword_arguments.py
"""Using arbitrary keyword arguements. Showing the function, that accept as many key-value pairs
as the calling statement provides. Using Pandas Series and Pandas DataFrame for obtained dictionaries from the
def user_data(first,last,**user_info). """
import pandas as pd
#function that takes first and last name but it accepts an arbitrary number of keyword arguments as well
def user_data(first,last,**user_info): #parameter **user_info - create an empty dictionary and pack whatever keu-values it receives.
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user1 = user_data('Kris', 'Kozak',          #function takes 2 positional arguments: 'Kris', 'Kozak' and infinite number of key = value
                  Location='Szczecn',
                  Field='Programming',
                  Age='38',
                  Country='Poland')

user2 = user_data('Jacek', 'Mencel',
                  Location='Switzerland',
                  Field='Documentation',
                  Age='38',
                  Country='Poland'
                  )

print(f'user1={user1}')
print(f'user2={user2}')
print()

#try to use Pandas Series to structrure data ,user_data(), which returns dictionary
user1_pd = pd.Series(user1)
print(f'user1_pd=\n{user1_pd}')
"""pd.Series shows key and value pairs from dictionary:
user1_pd=
Location          Szczecn
Field         Programming
Age                    38
Country            Poland
first_name           Kris
last_name           Kozak
dtype: object"""
#acces individuael element of the Series user1_pd, which has custom indices
print(f"user1_pd['Location']={user1_pd['Location']}")
#the same
print(f'user1_pd.Country = {user1_pd.Country}')  #If the custom indices are strings, Pandas automatically add them to the Series as attributes, that you can access viat a dot(.)

#if Series contains strings, you can use string 'str' attribute
print(f"user1_pd.str.contains('Szczecn'):\n{user1_pd.str.contains('Szczecn')}")
#user1_pd.str.contains('Szczecn') determines whether the value of each element contains string 'Szczecn' and return boolean value
"""out:
ocation       True
Field         False
Age           False
Country       False
first_name    False
last_name     False
dtype: bool"""
print()

print(f'user1_pd.str.upper()=\n{user1_pd.str.upper()}')
"""out:
user1_pd.str.upper()=
Location          SZCZECN
Field         PROGRAMMING
Age                    38
Country            POLAND
first_name           KRIS
last_name           KOZAK
dtype: object"""


#try to use Pandas DataFrame to structrure data ,user_data(), which returns dictionary
print()
user2_fr = pd.DataFrame((user1, user2),['label1','label2']) #first argument is a touple, becuase DataFrame takes only 1 arguemnt and indexes, each value of the touple is the dictionary
print(f'user2_fr=\n{user2_fr}')

"""
out:
user2_fr=
           Location          Field Age Country first_name last_name
label1      Szczecn    Programming  38  Poland       Kris     Kozak
label2  Switzerland  Documentation  38  Poland      Jacek    Mencel"""
print()

#acces the row of DataFrame via it's loc attribute
c = 0
for row in ('label1','label2'):
    c += 1
    print(f"row{c}=label{c}=\n{user2_fr.loc[row]}")
    print()
"""out:
row1=label1=
Location          Szczecn
Field         Programming
Age                    38
Country            Poland
first_name           Kris
last_name           Kozak
Name: label1, dtype: object

row2=label2=
Location        Switzerland
Field         Documentation
Age                      38
Country              Poland
first_name            Jacek
last_name            Mencel
Name: label2, dtype: object"""
print()
print(3*'--------------iloc[i]')
#Access the rows by integer zero-based indices using the iloc attribute (the i in iloc means that it's used with integer indices)
for i in range(2):
    print(f"label{i+1}=user2_fr.iloc[{i}]=\n{user2_fr.iloc[i]}")
    print()
"""out:
label1=user2_fr.iloc[0]=
Location          Szczecn
Field         Programming
Age                    38
Country            Poland
first_name           Kris
last_name           Kozak
Name: label1, dtype: object

label2=user2_fr.iloc[1]=
Location        Switzerland
Field         Documentation
Age                      38
Country              Poland
first_name            Jacek
last_name            Mencel
Name: label2, dtype: object"""
print()
#selecting the rows via slices
print(f"user2_fr.loc['label1':'label2']=\n{user2_fr.loc['label1':'label2']}")

print()

print(f"user2_fr.iloc[0:2]=\n{user2_fr.iloc[0:2]}")
print()

print(f"user2_fr.loc['label1':'label2',['Location','Field']]=\n{user2_fr.loc['label1':'label2',['Location','Field']]}")
"""out:
user2_fr.loc['label1':'label2',['Location','Field']]=
           Location          Field
label1      Szczecn    Programming
label2  Switzerland  Documentation
"""
print()

print(f"user2_fr.iloc[[0,1],0:3]=\n{user2_fr.iloc[[0,1],0:3]}")
"""out:
user2_fr.iloc[[0,1],0:3]=
           Location          Field Age
label1      Szczecn    Programming  38
label2  Switzerland  Documentation  38"""
print()

#Transposing the DataFrame wit T attribute
print(f"user2_fr.T=\n{user2_fr.T}")
"""out:
user2_fr.T=
                 label1         label2
Location        Szczecn    Switzerland
Field       Programming  Documentation
Age                  38             38
Country          Poland         Poland
first_name         Kris          Jacek
last_name         Kozak         Mencel"""
print()

#Sorting by rows by their indices using sort_index(ascending=False/True) with its keyword argument sort_index
print(f"user2_fr.sort_index(ascending=False)=\n{user2_fr.sort_index(ascending=False)}")
"""out:
user2_fr.sort_index(ascending=False)=
           Location          Field Age Country first_name last_name
label2  Switzerland  Documentation  38  Poland      Jacek    Mencel
label1      Szczecn    Programming  38  Poland       Kris     Kozak"""






