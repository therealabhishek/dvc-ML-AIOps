from src.utils.all_utils import read_yaml, create_directory, save_local_df
import argparse
import pandas as pd
import os
from sklearn.model_selection import train_test_split

def split_save_data(config_path, params_path):
  """[summary]

  Args:
      config_path ([type]): [description]
  """

  # read data:
  config = read_yaml(config_path)
  params = read_yaml(params_path)
  
  # path to load local data:
  artifacts_dir = config["artifacts"]["artifacts_dir"]
  raw_local_dir = config["artifacts"]["raw_local_dir"]
  raw_local_file = config["artifacts"]["raw_local_file"]

  raw_local_file_path = os.path.join(artifacts_dir, raw_local_dir, raw_local_file)
  df = pd.read_csv(raw_local_file_path)
  #print(df.head())

  split_ratio =  params["base"]["test_size"]
  random_state = params["base"]["random_state"]

  # splitting data:
  train, test = train_test_split(df, test_size= split_ratio, random_state= random_state)

  # saving train and test files:
  split_data_dir = config["artifacts"]["split_data_dir"]

  create_directory([os.path.join(artifacts_dir, split_data_dir)])

  train_data_filename = config["artifacts"]["train_data"]
  test_data_filename = config["artifacts"]["test_data"]

  train_data_path = os.path.join(artifacts_dir, split_data_dir, train_data_filename)
  test_data_path = os.path.join(artifacts_dir, split_data_dir, test_data_filename)

  for data, data_path in (train, train_data_path), (test, test_data_path):
    save_local_df(data, data_path)





if __name__ == "__main__":
  args = argparse.ArgumentParser()

  args.add_argument("--config", "-c", default="config/config.yaml")
  args.add_argument("--params", "-p", default="params.yaml")

  parsed_args = args.parse_args()

  split_save_data(config_path= parsed_args.config, params_path = parsed_args.params)

