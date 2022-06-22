import logging
import sys
from logging.handlers import TimedRotatingFileHandler



from pathlib import Path


class Config:
  RANDOM_SEED = 27
  ROOT_PATH = Path("../")
  REPO = "https://github.com/gezish/USGS_3DEP_Python_LIDAR"
  LOG_FILE = ROOT_PATH / "log_manage/PythonLidara.log"
  DATA_PATH = ROOT_PATH / "D:/AK_BrooksCamp_2012/"
  ASSETS_PATH = ROOT_PATH / "assets/"
  LAZ_PATH = DATA_PATH / "laz"
  TIF_PATH = DATA_PATH / "tif"
  SHP_PATH = DATA_PATH / "shp"
  IMG_PATH = DATA_PATH / "img"
  USGS_3DEP_PUBLIC_DATA_PATH = "https://s3-us-west-2.amazonaws.com/usgs-lidar-public/"

FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")

# log handler
def get_console_handler():
  console_handler = logging.StreamHandler(sys.stdout)
  console_handler.setFormatter(FORMATTER)
  return console_handler


def get_file_handler():
  file_handler = TimedRotatingFileHandler(Config.LOG_FILE, when='midnight')
  file_handler.setFormatter(FORMATTER)
  return file_handler


def get_logger(logger_name):
  logger = logging.getLogger(logger_name)
  # better to have too much log than not enough
  logger.setLevel(logging.DEBUG)
  logger.addHandler(get_console_handler())
  logger.addHandler(get_file_handler())
  # with this pattern, it's rarely necessary to propagate the error up to parent
  logger.propagate = False
  return logger
