from parsera import Parsera
from config import get_config
from model_setup import get_custom_llm
import pandas as pd

def main():
    openai_api_key, model_name = get_config()
    llm = get_custom_llm(openai_api_key, model_name)

    url = "https://news.ycombinator.com/"
    elements = {
        "Title": "News title",
        "Points": "Number of points",
        "Comments": "Number of comments",
    }

    scrapper = Parsera(model=llm)
    result = scrapper.run(url=url, elements=elements)
    print(result)
    print("Raw scraped data:", result)
    
    df = pd.DataFrame(result)
    print("Scraped Data in DataFrame:")
    print(df)

if __name__ == "__main__":
    main()
