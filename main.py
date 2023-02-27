student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}
for (key, value) in student_dict.items():
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    pass

import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data.to_dict)

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)