import gradio as gr
import requests
import pandas as pd
from transformers import pipeline

def get_fork_info(api_token, repo):
    # Get the list of forks for the specified repo using the GitHub API
    headers = {'Authorization': f'token {api_token}'}
    url = f'https://api.github.com/repos/{repo}/forks'
    response = requests.get(url, headers=headers)
    forks = response.json()

    # Extract the name, owner, and size of each fork using a list comprehension
    fork_info = [{'name': fork['name'], 'owner': fork['owner']['login'], 'size': fork['size'], 'updated_at': fork['updated_at'], 'stargazers_count': fork['stargazers_count'], 'forks_count': fork['forks_count'], 'description': fork['description']} for fork in forks]

    # Sort the forks by size in descending order and select the five largest and five smallest forks
    largest_forks = sorted(fork_info, key=lambda x: x['size'], reverse=True)[:5]
    smallest_forks = sorted(fork_info, key=lambda x: x['size'])[:5]

    # Sort the forks by updated_at in descending order and select the most up-to-date fork
    most_recent_fork = sorted(fork_info, key=lambda x: x['updated_at'], reverse=True)[0]

    # Select the fork with the most stargazers and the most forks
    most_popular_fork = sorted(fork_info, key=lambda x: (x['stargazers_count'], x['forks_count']), reverse=True)[0]

    # Select the fork with the longest description
    longest_description_fork = sorted(fork_info, key=lambda x: len(x['description']), reverse=True)[0]

    return {
        'largest_forks': largest_forks,
        'smallest_forks': smallest_forks,
        'most_recent_fork': most_recent_fork,
        'most_popular_fork': most_popular_fork,
        'longest_description_fork': longest_description_fork,
    }

def format_output(output_dict):
    return (
        f"Largest forks:\n\n{pd.DataFrame(output_dict['largest_forks'])[['name', 'owner', 'size']]}".replace(
            '\n', '\n\n'
        )
        + f"\n\nSmallest forks:\n\n{pd.DataFrame(output_dict['smallest_forks'])[['name', 'owner', 'size']]}".replace(
            '\n', '\n\n'
        )
        + f"\n\nMost up-to-date fork: {output_dict['most_recent_fork']['name']} ({output_dict['most_recent_fork']['owner']})\n\nMost popular fork: {output_dict['most_popular_fork']['name']} ({output_dict['most_popular_fork']['owner']})\n\nLongest description fork: {output_dict['longest_description_fork']['name']} ({output_dict['longest_description_fork']['owner']})"
    )

api_key = "<your OpenAI API token here>"
repo = "rspsi/rspsi"

model = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B", device=0)

def chatbot(api_token, repo):
    output_dict = get_fork_info(api_token, repo)
    output_str = format_output(output_dict)
    prompt = "GitHub repository: " + repo + "\n\n" + output_str + "\n\n"
