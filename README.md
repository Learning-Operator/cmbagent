<img width="487" alt="Screenshot 2025-03-12 at 16 22 27" src="https://github.com/user-attachments/assets/00669d24-a0f8-4a60-b550-7aa0d8999a6c" />

# cmbagent

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![arXiv](https://img.shields.io/badge/arXiv-2412.00431-b31b1b.svg)](https://arxiv.org/abs/2412.00431) <a href="https://colab.research.google.com/github/CMBAgents/cmbagent/blob/main/docs/notebooks/cmbagent_colab_demo.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>


Multi-Agent System for Science, Made by Cosmologists, Powered by [AG2](https://github.com/ag2ai/ag2).

Try **cmbagent** in [Colab](https://colab.research.google.com/github/CMBAgents/cmbagent/blob/main/docs/notebooks/cmbagent_colab_demo.ipynb)!  

This is **open-source research-ready software**.  Please **star the  repo ⭐ and cite [Laverick et al (2024)](#reference)**. 


- This software is under MIT license. We bear no responsibility for any misuse of this software or its outputs.

- Check the [demo notebooks](https://github.com/CMBAgents/cmbagent/tree/main/docs/notebooks).

- Best perfmonces are obtained with [top-scoring models](https://lmarena.ai/?leaderboard). (We like gemini, gpt-4o/4.5/o3, claude ––see [our examples](https://github.com/CMBAgents/cmbagent/tree/main/docs/notebooks)).

- Currently, RAG agents use `file_search` on OpenAI vector stores.

> Note: Please fork and contribute to the repo. We give access to our top-tier OpenaAI, Anthropic and Cloud organizations to our top contributors.


We emphasize that [cmbagent](https://github.com/CMBAgents/cmbagent) is under active development and apologize for any bugs. 

## Stategy

**Cmbagent** acts according to a **Planning and Control** strategy with **no human-in-the-loop**.

You give a task to solve, then:

**Planing**

- A plan is designed from a conversation between a planner and a plan reviewer.
- Once the number of feedbacks (reviews) is exhausted the plan is recorded in context and **cmbagent** switches to **control**.

**Control**

- The plan is executed **step-by-step**.
- Sub-tasks are handed over to a single agent in each step.
- Reverts to admin (i.e., you) after final step of plan is completed. 

## Run

See [Installation](#installation), and then in a Jupyter notebook, do:

> The output of this session is [here](https://github.com/CMBAgents/cmbagent/blob/main/docs/notebooks/cmbagent_beta2_demo_finance.ipynb).

```python
import os
from cmbagent import CMBAgent

cmbagent = CMBAgent(agent_llm_configs = {
                    'engineer': {
                        "model": "o3-mini-2025-01-31",
                        "reasoning_effort": "high", ## for gpt-4.5-preview-2025-02-27, gpt-4o-2024-11-20, gpt-4o-mini, etc, comment out this line.
                        "api_key": os.getenv("OPENAI_API_KEY"),
                        "api_type": "openai",
                        },
                    'researcher': {
                        "model": "gemini-2.0-pro-exp-02-05",
                        "api_key": os.getenv("GEMINI_API_KEY"),
                        "api_type": "google",
                        }})

task = """
Generate simulated stock market data that mimics the behavior of 500 stocks across various sectors (similar to the S&P 500) over a 2-year period. 
Within this timeframe, incorporate a financial crisis lasting a few weeks in the middle of the period. 

Your simulation should capture:
Sudden volatility spikes, market jumps, and heavy-tailed returns.
Periods of extreme uncertainty and rapid price changes.
Realistic correlations among stocks, particularly reflecting sector-based dependencies.

After generating the simulated data, apply the Black-Scholes Merton model to price call options—focusing specifically on the impact of varying strike prices. 

Provide visualizations that illustrate:
The evolution of stock prices, highlighting the crisis period.
Volatility patterns and any market jumps.
The correlation structure among different sectors.
The pricing behavior of call options during both normal and crisis conditions.

Finally, analyze how the crisis impacts option pricing and discuss any limitations or insights regarding the model's performance under extreme market conditions.
"""

cmbagent.solve(task,
               max_rounds=500, # set to a high number, this is the max number of total agent calls
               shared_context = {'feedback_left': 1, # number of feedbacks on the plan, generally want to set to a low number, as this adds unnecessary complexity to the workflow. 
                                 'maximum_number_of_steps_in_plan': 5})
```

Your outputs will be stored in the output directory.


To update a vector stores with local files in your CMBAGENT_DATA folder (see [Getting the RAG data](#getting-the-rag-data)), for your RAG agents use:

```python
cmbagent = CMBAgent(make_vector_stores=['name_of_agent'])
```

## API Keys

Before you can use cmbagent, you need to set your OpenAI API key as an environment variable. Do this in a terminal, before launching Jupyter-lab.

For Unix-based systems (Linux, macOS), do:

```bash
export OPENAI_API_KEY="sk-..."  ## mandatory for the RAG agents
export ANTHROPIC_API_KEY="sk-..." ## optional 
export GEMINI_API_KEY="AI...." ## optional 
```
(paste in your bashrc or zshrc file, if possible.)

For Windows, use [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) and the same command.

By default, cmbagent uses models from oai/anthropic/google. If you want to pick different llms, just adapat `agent_llm_configs` as above, or the `default_agent_llm_configs` in [utils.py](https://github.com/CMBAgents/cmbagent/blob/main/cmbagent/utils.py).

## Reference

```bash
   @misc{Laverick:2024fyh,
      author = "Laverick, Andrew and Surrao, Kristen and Zubeldia, Inigo and Bolliet, Boris and Cranmer, Miles and Lewis, Antony and Sherwin, Blake and Lesgourgues, Julien",
      title = "{Multi-Agent System for Cosmological Parameter Analysis}",
      eprint = "2412.00431",
      archivePrefix = "arXiv",
      primaryClass = "astro-ph.IM",
      month = "11",
      year = "2024"
   }
```



## Installation

Before installing cmbagent, create a virtual environment (we use python3.12): 

```bash
python3.12 -m venv /path/to/your/envs/cmbagent_env
source /path/to/your/envs/cmbagent_env/bin/activate
```

Then, follow these steps:

Clone and install our package from GitHub.

```bash
git clone https://github.com/CMBAgents/cmbagent.git
cd cmbagent
pip install -e .
```

## Getting the RAG data

If you ignore this, it is OK, just note that `cmbagent_data` will go into your `$HOME`.

If you are a cosmologist, there is already some RAG files for you to play with. 
If you are not a cosmologist, just modify the code/documents so it does RAG on your own documents of interest. It's pretty straightforward. 

Then, do this:

```bash
git clone https://github.com/CMBAgents/cmbagent_data.git
export CMBAGENT_DATA=/where/you/have/cloned/cmbagent_data
```

Note that you need to set the `CMBAGENT_DATA` environment variable accordingly before using `cmbagent` 
in any future session. Maybe you want to add this to your `.bashrc` or `.zshrc` file, or in your `activate` script!


If you don't set this, the rag data will go into your home directory (you should see a folder `cmbagent_data` with same content as [here](https://github.com/CMBAgents/cmbagent_data).

## Structure

The core of the code is located in [cmbagent.py](https://github.com/CMBAgents/cmbagent/blob/main/cmbagent/cmbagent.py).

RAG agents can be found in [rag_agents](https://github.com/CMBAgents/cmbagent/tree/main/cmbagent/agents/rag_agents). You can make your own easily.

Apart from the RAG agents, we have assistant agents (like an engineer and a planner) and a code execution agent (executor).

All agents inherit from the `BaseAgent` class. You can find the definition of `BaseAgent` in the [base_agent.py](https://github.com/CMBAgents/cmbagent/blob/main/cmbagent/base_agent.py) file.


## Usage

Check the [demos](https://github.com/CMBAgents/cmbagent/blob/main/docs/notebooks). 

## Cosmology example

**Task:** 

```
"""
Provide a gif of the matter power spectrum varying z between 0 and 20, showing the scale where non-linear effects become important
"""
```

**Result:**

<img src="https://github.com/user-attachments/assets/304828cb-617b-4704-8b30-6d53b5f378a2" alt="matter_power_spectrum" width="400" />


(Note: after $z=5$, the matter pk is approximated by linear pk, as this is out of the range of our current emulators.)



## Acknowledgments

Our project is funded by the [Cambridge Centre for Data-Driven Discovery Accelerate Programme](https://science.ai.cam.ac.uk). We are grateful to [Mark Sze](https://github.com/marklysze) for help with [ag2](https://github.com/ag2ai/ag2).







