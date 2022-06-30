import os
from pprint import pprint

# file for file in os.listdir('C:\Net_Homework\Net_Homework_Reading_Files\Net_Homework_Reading_Writing_Files\file_writing') 
f_list_txt = [file for file in os.listdir('./file_writing') if file.endswith('.txt')]
print(f_list_txt)

dict_reader = {}

for item in f_list_txt:
    with open('./file_writing/' + item, encoding="utf-8") as f:
        lines = f.readlines()
        dict_value = [len(lines), lines]
        dict_reader[item] = dict_value

# pprint(dict_reader)        

sorted_dict_reader = dict(sorted(dict_reader.items(), key=lambda item: item[1][0]))
pprint(sorted_dict_reader)


with open('result.txt', 'w', encoding ="utf-8") as f:
    for key, values in sorted_dict_reader.items():
      f.write(key)
      f.write('\n')
      f.write(str(values[0]))
      f.write('\n')
      for line in values[1]:
          f.write(line)
      f.write('\n')
