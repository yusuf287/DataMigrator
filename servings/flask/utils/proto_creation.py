import os
import utils.names as names

test_case_proto_file_name = names.test_case_proto_file_name
input_output_proto_file_name = names.input_output_proto_file_name

def compile_test_case_proto(testing_dir):
	proto_string = '		syntax = "proto3";\n\
		import "%s";\n\
		\n\
		message TestCase{\n\
			Input input = 1;\n\
			Output output = 2;\n\
		}\n\
		\n\
		message TestCases{\n\
			repeated TestCase test_case = 1;\n\
		}\n\
		\n\
		message Outcome{\n\
			Input input = 1;\n\
			Output expected_output = 2;\n\
			Output actual_output = 3;\n\
			string result = 4;\n\
		}\n\
		\n\
		message Outcomes{\n\
			repeated Outcome outcome = 1;\n\
		}'%(input_output_proto_file_name)
	test_case_proto_file = os.path.join(testing_dir, test_case_proto_file_name)
	

	with open(test_case_proto_file, "w") as f:
		f.write(proto_string)

	os.system("protoc --proto_path=%s --python_out=%s %s"%(testing_dir, testing_dir, test_case_proto_file))