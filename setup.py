# resposible for creating my machine learning as a package
# and deploy in pyp
from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirments(file_path:str)->List[str]:
    '''this function will return the list of requirements'''
    requirments=[]
    with open(file_path) as file_obj:
        # as it read line a /n also gets readed
        # in order to remove that we wil use a list comprehension.
        requirements=file_obj.readlines()

        # this list comprehension will replace \n with ""
        requirments = [req.replace("\n","") for req in requirments]

        # we have use -e . to trigger the code and it will read by the
        # above list comprehension. To avoid that we made the below 
        # if else statement to remove it from requirements.
        if HYPHEN_E_DOT in requirments:
            requirments.remove(HYPHEN_E_DOT)
        
    return requirments



setup(name="MLProject", 
      version="0.0.1", 
      author="LakshayGoyal", 
      author_email="lakshaygoyal287@gmail.com", 
      packages=find_packages(),
      install_rquires=get_requirments("requirments.txt")
)
