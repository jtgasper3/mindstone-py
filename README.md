# Mindstone Py

## Overview
Mindstone Py is a set of Python scripts that interacts with an OpenAI style API to generate chat completions using qwen2.5/3 model. The application can run locally, in a Docker container, or a [devcontaner](https://containers.dev/) for easy setup.

While we are using "conversations" to interact with the AI, it is the python script(s) that is conversing with the LLM. There is no direct user interaction being conducted here. This style of integration would lend itself to being incorporated into something like Help Desk tooling, where we don't expect the help desk operator to converse with the AI, but to simply request "account troubleshooting" from the application menu and the operator being given the final output/response from the LLM. Another way of thinking about this is that the Python app is the "user" of the LLM, not the human operator.

- `v1`: demonstrates a conceptual use of Retrieval-Augmented Generation (RAG)
- `v2`: demonstrates the LLM identifying issue with user email account using the RAG for its rules.
- `v3`: Pivoting to formal OpenAI API model for building prompts, RAGs and an initial (agentic) "tool"  demonstrating the LLM looking up account data before identifying the account issues.
- `v4`: Providing additional (agentic) tools to the LLM and then asking the LLM to "fix" the accounts to see what it tries to do.

> Note: The code uses Docker's model support, but changes to use Ollama or another AI engine should be trivial. You'll need to change the hostname (and maybe endpoint) of the "OpenAI" API URL. An API Key maybe needed 

## Requirements
The runtime must have Python 3.

## Setup
1. Clone the repository or download the project files.
2. Run with your preferred method:
    1. Open the project in VS Code and activate the devcontainer when prompted.
    2. Build (`docker build -t mindstone-py .` and run the container (`docker run -it mindstone-py`).
    3. Run the project locally. Besure to run `pip install -r requirements.txt` to install the dependencies.

## Running the Application
Each version has a README.md with the appropriate commands to run the scipts. (Local runs will need slight modifications of the commands to run)

## Dependencies
The project requires the following Python packages, which are listed in `requirements.txt`:
- requests

## License
This project is licensed under the MIT License.
