import subprocess
import os

def convert_c_to_ir(c_file, ir_file):
    if not os.path.exists(c_file):
        raise FileNotFoundError(f"The C file {c_file} does not exist.")
    
    command = ['clang', '-S', '-emit-llvm', c_file, '-o', ir_file]
    
    try:
        subprocess.run(command, check=True)
        print(f"LLVM IR generated successfully: {ir_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")

c_file = './IR_Generator/highlevel.c'
ir_file = './IR_Generator/ir.ll'

convert_c_to_ir(c_file, ir_file)
