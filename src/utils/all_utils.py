import yaml
import os


def read_yaml(yaml_path:str) -> dict:
  """[summary]

  Args:
      yaml_path (str): [description]

  Returns:
      dict: [description]
  """
  with open(yaml_path) as yaml_file:
    content = yaml.safe_load(yaml_file)

  return content


def create_directory(dirs: list):
  """[summary]

  Args:
      dirs (list): [description]
  """
  for dir_path in dirs:
    os.makedirs(dir_path, exist_ok=True)
    print(f"directory created at {dir_path}.")

def save_local_df(data, data_path, index_status= False):
  data.to_csv(data_path, index = index_status)
  print(f"data is saved at {data_path}.")
