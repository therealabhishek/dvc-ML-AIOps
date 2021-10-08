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
