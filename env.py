import os
import sys
import warnings

DATASET_PATH = '/dbstore/datasets/'
PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(PROJECT_PATH, 'submodules/tf_model/research/struct2depth'))
sys.path.append(os.path.join(PROJECT_PATH, 'submodule/tfoptflow/'))

os.environ['OMP_NUM_THREADS'] = '4'
os.environ['OPENBLAS_NUM_THREADS'] = '4'
os.environ['MKL_NUM_THREADS'] = '6'
os.environ['VECLIB_MAXIMUM_THREADS'] = '4'
os.environ['NUMEXPR_NUM_THREADS'] = '6'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
warnings.simplefilter('ignore')
