import file_compare as fc

f1 = open("input/input.py", "r")
input_file1 = f1.read()
f1.close()

f2 = open("samples/tg_x.py", "r")
input_file2 = f2.read()
f1.close()

print(fc.file_compare(input_file1, input_file2))
