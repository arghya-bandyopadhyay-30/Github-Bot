# Automated Historical Commit Project

This project is designed to create a series of historical commits with random timestamps to simulate a realistic commit history. It allows developers to add custom commits to a Git repository for a specific range of dates, effectively enhancing the repository's commit history for demonstration or learning purposes.

## Features
- **Randomized Date Commits**: Generate and commit historical data with random dates between a specified start and end period.
- **Custom Timestamps**: Each commit includes a custom timestamp to make the history look more realistic.
- **Automated Pull and Push**: Automatically pull the latest changes and push new commits individually to the remote repository.
- **Error Handling**: Includes retries for push failures to mitigate conflicts or network issues.
- **Rebase Before Push**: Rebase changes before each push to ensure local changes are in sync with the remote repository.
- **Detailed Logging**: Logs each step for better traceability and debugging.

## How to Use

### Prerequisites
- Python 3.x
- GitPython library
- A Git repository to work with

### Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/arghya-bandyopadhyay-30/github-bot.git
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Configuration
- Set up your Git credentials using SSH for easier authentication.
- Update the repository path and file path in the script as needed.

### Running the Script
To run the script and create historical commits:

```sh
python src/main.py
```

This script will:
- Generate random dates within a given range.
- Write those dates to a JSON file (`data.json`).
- Commit the changes with the specified timestamp and push to the remote repository.

## Important Notes
- **Security Warning**: Do not embed sensitive information directly in scripts or URLs for security reasons. Use Git credential helper or SSH instead.
- **Network and Permission Issues**: Ensure you have the appropriate permissions for the repository.

## Example Use Cases
- **Demo Repositories**: Create demo repositories with realistic commit histories for presentations or tutorials.
- **Learning**: Practice working with Git, particularly with historical commits, rebasing, and error handling.
- **Version Control Simulation**: Test version control workflows by simulating a series of historical changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! If you have suggestions for improvements, please open an issue or submit a pull request.

## Contact
For any questions or feedback, please reach out via GitHub issues.
