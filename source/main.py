import time
import json

from source.driver.container import get_container

from source.topics.service import Topics

from config import get_config


def main():
    config = get_config()
    chrome_driver = get_container().driver
    service = Topics(driver=chrome_driver)
    with service as bot:
        bot.main_page(link=config.base_url)
        bot.sign_in(config.email, config.password)
        bot.get_topics("Keratin straightening")
        article_links = bot.get_current_article()
        filtered_articles = []
        for article in article_links:
            # Split the URL at the '?' and take the first part to remove query parameters
            clean_article = article.split('?')[0]
            # Check if the URL is likely an article link and not a profile or other page
            if '/@' not in clean_article or clean_article.count('/') > 3:
                filtered_articles.append(clean_article)

        unique_filtered_articles = list(set(filtered_articles))

        articles_dict = {'articles_2': unique_filtered_articles}

        with open('filtered_articles.json', 'w') as json_file:
            json.dump(articles_dict, json_file, indent=4)

        time.sleep(1000)

