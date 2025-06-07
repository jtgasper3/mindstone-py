# Mindstone Py

## Overview

Mindstone Py is a set of Python scripts that interacts with an OpenAI style API to generate chat completions using qwen2.5/3 model. The application can run locally, in a Docker container, or a [devcontaner](https://containers.dev/) for easy setup. Its examples use identity and access management user cases.

## Conversations

While we are using "conversations" to interact with the AI, it is the python script that is "conversing" with the LLM. There is no direct user interaction being conducted here. This automated style of integration would lend itself to being incorporated into something like Help Desk tooling, where we don't expect the help desk operator to converse with the AI, but to simply request "account troubleshooting" from the application menu and the operator being given the final output/response from the LLM. Another example, would be an automation script that has an AI Agent review the contents of a new GitHub issues and attempt to categorize the issue, then if appropriate write code to fix the issue, then create a pull request with the proposed code.

Another way of thinking about this is that the Python app/script is the "user" of the LLM, not a human operator.

## eVolutions

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


## An LLM Primer for Devs

### State

LLMs are inherently stateless. Chatbots only appear to have conversations because when each input is sent to the chatbot, the whole coversation, including who sent what, is sent to the LLM. This allows the LLM to have the context to generate an appropriate "next" response.

As developers, we can also nudge/edit the LLM's responses being sent as input to "steer" it. There is evident in `v3` where we "suggest" the response it would have given when we perform the 2nd interaction (while also including the previous conversation).

### RAGs

Retrieval-Augmented Generation (RAG) is the process of optimizing the output of a large language model, so it references an authoritative knowledge base outside of its training data sources before generating a response [1].

In other words, we add additional content to the "conversation" so the LLM can have knowledge on things its model was not trained on. This is just additional text inserted into the "prompt".

In practice, this content can be static content, queried from websites and databases, or very commonly queried from a vector database. With vector databases, arbitrary content (text & word documents, pdfs, mp3s) is encoded and inserted the vector database along with the indexing of the specific content. These indexing/vectors are used for content retrieval to more throughly return relavent content using long phrases or sentences to search versus what a SQL LIKE statement is able to find in relational databases.

(We only use static RAG content as vector databases are beyond the scope of this document... and often rely on embedding language models to do the encoding into something the LLM can efficiently use.)

What more understanding, check out AWS's RAG explainer. It's great.

[1: https://aws.amazon.com/what-is/retrieval-augmented-generation/](https://aws.amazon.com/what-is/retrieval-augmented-generation/)

### Agentic AI (giving AI Tools)

Agentic AI focuses on giving LLMs the ability to act autonomously... or as there own agent. We do this by defining a set of "tools" or functions that AI can "use".

In practice, this means providing structured JSON defining the functions, their descriptions, input and output objects. When the LLM "decides" to use a tool, it responds with a JSON object indicating the desired function and function arguments. It is up to the application developer to take that information and they MUST implement the actual function logic. Then they return the output of the function call to the LLM as input into the next step of the conversation.

It should be stressed here. The LLM does not directly call the function logic. It merely makes a request and examines the tool response provided back to it. The application developer is responsible for santizing the input, doing sanity checks, etc. Assume that your LLM is your worst function/API user.

DO NOT TRUST THE LLM WITH SOMETHING DESTRUCTIVE! YOU HAVE BEEN WARNED!

### Additional Context

Along with additional authoritative knowledge (being provided via RAGs), it can be helpful to provide other information within the context. 

For example, the LLM does not know the current date and time. If you are asking the LLM to evaluate things based on the current date and time, like determining if an account has expired, you must tell the LLM the current date and time, as well as passing the account information in the requests.

### Prompt Engineering

I do not like the term "prompt engineering", but here we are.

You ever ask AI something and it drones on and on, well you can control that with prompt engineering.

Prompt engineering is crafting instructions to the AI to get a desired outcome. It maybe telling the LLM to act like a specific actor: "You are... an expert speaker", "...a joke teller", "...the president of a train club", "...an expert system", "...a tea pot". It maybe telling the LLM how to prepare the response: "respond... in a single sentence", "...with bulletpoints", "...in JSON". And then provide other constraints: "only give high confidence answers", "jokes should be offensive to black bears", "responses should be in passive voice".

The more clear the instructions, the better the output will be.

### Models and APIs

While Ollama, Docker, and LLM service providers provide HTTP services to interact with generic models, each model has been trained on specific input/request dataset styles. The JSON object style used by Open AI to train its models may not be identical to that used to train Alibab's models, etc. The response objects will likewise be different.

In these examples, we use raw http requests so there is nothing hidden from the developer. The requests in these examples use the qwen model for integrating tools, etc. Model vendors have libraries that can simply interacting with models, tools, etc.


## License
This project is licensed under the MIT License.
