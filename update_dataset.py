from calendar import c
import sys
import subprocess
import os

def print_usage():
  print("Usage: python update_dataset.py <path_to_fake> <path_to_real>")

def print_help_message():
  print("The path to the fake directory should be relative to the current directory")

def main():
  if len(sys.argv) != 3:
    print_usage()
    sys.exit(1)

  fake_directory = sys.argv[1]
  real_directory = sys.argv[2]

  if not os.path.exists(os.path.join(os.getcwd(), fake_directory)):
    print("Directory {} does not exist".format(fake_directory))
    print_help_message()
    sys.exit(1)

  if not os.path.exists(os.path.join(os.getcwd(), fake_directory)):
    print("Directory {} does not exist".format(fake_directory))
    print_help_message()
    sys.exit(1)

  fake_path = os.path.join(os.getcwd(), fake_directory)
  real_path = os.path.join(os.getcwd(), real_directory)
  base_output_path = os.path.join(os.getcwd(), 'data/dataset')
  fake_output = os.path.join(base_output_path, 'fake')
  real_output = os.path.join(base_output_path, 'real')

  base_command = 'pwsh -Command'

  fake_command = f'New-Item -Path {fake_output} -ItemType SymbolicLink -Value {fake_path} -Force'
  real_command = f'New-Item -Path {real_output} -ItemType SymbolicLink -Value {real_path} -Force'

  subprocess.call(f'{base_command} {fake_command}', shell=True)
  subprocess.call(f'{base_command} {real_command}', shell=True)
  
  print('Done!')

if __name__ == "__main__":
  main()