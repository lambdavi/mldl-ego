import gdown
import subprocess
import os
url = 'https://drive.google.com/u/0/uc?id=1bnbD7oTyJlr8c6YbVI2maVWWi6GD-kUA&export=download&confirm=t&uuid=27117e92-518b-4ba5-8f1a-357812f865cb&at=AB6BwCBpBsbIwbhmBFXwfUbsDQlm:1691672248452'
output = 'ek_data/P01_01.tar.gz'
gdown.download(url, output, quiet=False)
