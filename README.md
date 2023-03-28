# GitHub Forks Utility
This utility allows you to retrieve information about the forks of a GitHub repository, including the most up-to-date fork, the number of stars and forks, and additional information about the forks.
## Usage
To use this utility, you will need to provide your OpenAI API token and the name of the repository you want to analyze in the format `owner/repo`. Once you have entered these parameters, you can click the "Run" button to retrieve the desired information.

The output will be displayed in the Gradio interface, and you can download a summary of the results in a markdown file by clicking the "Download" button.
## Functionality
This utility uses the GitHub API and OpenAI GPT to analyze forks of a repository and provide various information about them. The following features are currently supported:

- <strong>Most up-to-date fork:</strong> Returns information about the fork with the most recent commit.
- <strong>Number of stars and forks:</strong> Returns the number of stars and forks for each fork.
- <strong>Completeness and future:</strong> Analyzes the README files of the forks and provides information about the most complete and future-filled forks.

## Dependencies
This utility depends on the following Python packages:

- `gradio`: A web interface for interactive machine learning demos.
- `torch`: A deep learning framework.
- `transformers`: A library for natural language processing tasks.
- `PyGithub`: A Python library for accessing the GitHub API.


You can install these dependencies by running `pip install -r requirements.txt`.