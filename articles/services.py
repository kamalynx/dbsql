import logging

import httpx


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def submit_to_indexnow(url: str, key: str, key_location: str):
    with httpx.Client(http2=True, timeout=120) as client:
        response = client.get('https://api.indexnow.org/indexnow', params={'key': key, 'url': url, 'keyLocation': key_location})

    logger.info(response)
    return response


if __name__ == '__main__':
    print(submit_to_indexnow(key='10db37c5e7a59f9fe0a686a8527b428e', url='https://dbsql.ru/mariadb/overview-of-the-median-function-in-mariadb/'))
