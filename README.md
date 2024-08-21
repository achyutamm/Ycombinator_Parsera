# Ycombinator_Parsera

Ycombinator_Parsera is a Python-based web scraping tool designed to extract data from Hacker News (Y Combinator) using a custom language model. This project leverages the OpenAI API to interpret and extract relevant data points such as news titles, points, and comments.

## Features

- Scrapes titles, points, and comments from Hacker News.
- Utilizes OpenAI's API for custom language model processing.
- Outputs data into a structured format using Pandas DataFrame.
- Saves the scraped data to a CSV file for further analysis.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher installed on your machine.
- An OpenAI API key with access to the desired model (e.g., `gpt-3.5-turbo`).
- Required Python packages listed in the `requirements.txt` file.

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/achyutamm/Ycombinator_Parsera.git
    cd Ycombinator_Parsera
    ```

2. Install the necessary dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your OpenAI API key by configuring the `get_config()` function in `config.py`:

    ```python
    def get_config():
        openai_api_key = "your-openai-api-key"
        model_name = "gpt-3.5-turbo"
        return openai_api_key, model_name
    ```

4. Ensure you have the `Parsera` class, as well as the `get_custom_llm` function in the respective modules.

## Usage

To run the scraper and save the output to a CSV file:

1. Run the `main.py` script:

    ```bash
    python src/main.py
    ```

2. The script will scrape the data from Hacker News and print it in a structured DataFrame format.

3. The scraped data will also be saved to `scraped_data.csv` in the root directory.

## Example Output

The following is an example of the scraped data displayed as a DataFrame:

| Title                                                           | Points       | Comments       |
|-----------------------------------------------------------------|--------------|----------------|
| I've Built My First Successful Side Project, and I Hate It      | 59 points    | 10 comments    |
| PS4 Emulator for Windows, Linux, macOS                          | 268 points   | 115 comments   |
| Show HN: Handwriter.ttf – Handwriting Synthesis with Harfbuzz WASM | 10 points  | 2 comments     |
| The Discovery of the Celendrical Date Line                      | 8 points     | 2 comments     |
| Zen, a Arc-like open-source browser based on the Firefox engine | 447 points   | 200 comments   |

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgements

- [OpenAI](https://www.openai.com/) for providing the API.
- [Pandas](https://pandas.pydata.org/) for data manipulation and analysis.
- [Hacker News](https://news.ycombinator.com/) for the content source.
