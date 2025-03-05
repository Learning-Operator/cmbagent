from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

from cmbagent.cmbagent import CMBAgent

import os

load_dotenv(dotenv_path= "/mnt/c/Users/Kiran/Desktop/cmbagent/cmbagent/.env")

Api_key = os.getenv('OPENAI_API_KEY')
print(Api_key)
Data_key = os.getenv('CMBAGENT_DATA')
print(Data_key)
Debug = os.getenv('Debug')
print(Debug)


Agent = CMBAgent(verbose= True,
                 Api_key= Api_key,
                 model="gpt4o",
                 make_vector_stores=False,
                 )


task = """ Use the planck 2018 collaboration data and scale that data back to obtain parameter values for the first second of the universe after inflation"""

Agent.solve(task)


