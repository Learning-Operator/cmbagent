import copy

import os
os.environ["CMBAGENT_DEBUG"] = "false"
os.environ["CMBAGENT_DISABLE_DISPLAY"] = "true"

from cmbagent import CMBAgent
# cmbagent = CMBAgent(make_vector_stores='camb')
# cmbagent = CMBAgent(
# agent_llm_configs = {
#                     'engineer': {
#                 "model": "gemini-2.5-pro-exp-03-25",
#                 "api_key": os.getenv("GEMINI_API_KEY"),
#                 "api_type": "google"},
#                     'researcher': {
#                 "model": "gemini-2.5-pro-exp-03-25",
#                 "api_key": os.getenv("GEMINI_API_KEY"),
#                 "api_type": "google"},
# })
   

cmbagent = CMBAgent()
   


task = r"""

Researcher suggests value for H0 and omega_cdm
Engineer computes the age of the universe with classy.
Researcher then reports the result.

instructions for planner: 
- start with researcher
- then engineer 
- then researcher
"""

cmbagent.solve(task,
               max_rounds=500,
               initial_agent="planner",
               # mode="one_shot"
               shared_context = {'feedback_left': 0,
                                 # "number_of_steps_in_plan": 1,
                                 'maximum_number_of_steps_in_plan': 3}
              )

planning_output = copy.deepcopy(cmbagent.final_context)

## control

# cmbagent = CMBAgent(
# agent_llm_configs = {
#                     'engineer': {
#                 "model": "gemini-2.5-pro-preview-03-25",
#                 "api_key": os.getenv("GEMINI_API_KEY"),
#                 "api_type": "google"},
#                     'researcher': {
#                 "model": "gemini-2.5-pro-preview-03-25",
#                 "api_key": os.getenv("GEMINI_API_KEY"),
#                 "api_type": "google"},
# })

# cmbagent = CMBAgent(
# agent_llm_configs = {
#                     'engineer': {
#                         "model": "o3-mini-2025-01-31",
#                         "reasoning_effort": "medium",
#                         "api_key": os.getenv("OPENAI_API_KEY"),
#                         "api_type": "openai"},
#                     'researcher': {
#                         "model": "o3-mini-2025-01-31",
#                         "reasoning_effort": "medium",
#                         "api_key": os.getenv("OPENAI_API_KEY"),
#                         "api_type": "openai"},
# })

cmbagent = CMBAgent(
agent_llm_configs = {
                    'engineer': {
                        "model": "gpt-4o-mini",
                        # "reasoning_effort": "medium",
                        "api_key": os.getenv("OPENAI_API_KEY"),
                        "api_type": "openai"},
                    'researcher': {
                        "model": "gpt-4o-mini",
                        # "reasoning_effort": "medium",
                        "api_key": os.getenv("OPENAI_API_KEY"),
                        "api_type": "openai"},
})

cmbagent.solve(task,
                max_rounds=50,
                initial_agent="control",
                shared_context = planning_output
                )