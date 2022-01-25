import os
import shutil

if os.path.exists('custom'):
  shutil.rmtree('custom', ignore_errors = False)
