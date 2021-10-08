from src.utils.all_utils import read_yaml, create_directory, save_local_df
import argparse
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import joblib

def train_model(config_path, params_path):
  """[summary]

  Args:
      config_path ([type]): [description]
      params_path ([type]): [description]
  """


  # read data:
  config = read_yaml(config_path)
  params = read_yaml(params_path)
  
  # path to load local data:
  artifacts_dir = config["artifacts"]["artifacts_dir"]
  split_data_dir = config["artifacts"]["split_data_dir"]


  train_data_filename = config["artifacts"]["train_data"]


  train_data_path = os.path.join(artifacts_dir, split_data_dir, train_data_filename)

  train_data = pd.read_csv(train_data_path)

  train_y = train_data['quality']
  train_X = train_data.drop('quality', axis=1)

  alpha = params["model_params"]["ElasticNet"]["alpha"]
  l1_ratio = params["model_params"]["ElasticNet"]["l1_ratio"]
  random_state = params["base"]["random_state"]

  linear_reg = ElasticNet(alpha= alpha, l1_ratio= l1_ratio,random_state=random_state)
  linear_reg.fit(train_X, train_y)
  #print("done")

  model_dir = config["artifacts"]["model_dir"]
  model_filename = config["artifacts"]["model_filename"]

  model_dir = os.path.join(artifacts_dir, model_dir)

  create_directory([model_dir])

  model_path = os.path.join(model_dir, model_filename)

  joblib.dump(linear_reg, model_path)




if __name__ == "__main__":
  args = argparse.ArgumentParser()

  args.add_argument("--config", "-c", default="config/config.yaml")
  args.add_argument("--params", "-p", default="params.yaml")

  parsed_args = args.parse_args()

  train_model(config_path= parsed_args.config, params_path = parsed_args.params)

