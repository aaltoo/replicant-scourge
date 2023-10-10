import file_compare as fc
import helpers as helpers

f1 = open("input/input.py", "r")
input_file1 = f1.read()
f1.close()

f2 = open("samples/tg_x.py", "r")
input_file2 = f2.read()
f2.close()

print(fc.file_compare(input_file1, input_file2))

f3 = open("samples/sum.js", "r")
input_file3 = f3.read()
f3.close()

print(helpers.remove_comments(input_file3, "js"))