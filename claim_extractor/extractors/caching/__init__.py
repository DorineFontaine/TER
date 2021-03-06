from typing import Dict, Optional

import requests
from redis import Redis

from claim_extractor import Claim

redis = Redis(decode_responses=True)


def get(url: str, headers: Dict[str, str] = None, timeout: int = None):
    page_text = redis.get(url)
    try:
        if not page_text:
            result = requests.get(url, headers=headers, timeout=timeout)
            if result.status_code < 400:
                page_text = result.text
                redis.set(url, page_text)
            else:
                return None
    except requests.exceptions.ReadTimeout:
        page_text = None
    except requests.exceptions.MissingSchema:
        page_text = None
    except requests.exceptions.ConnectTimeout:
        page_text = None
    return page_text


def post(url: str, headers: Dict[str, str] = None, data: Dict[str, str] = None, timeout: int = None):
    page_text = redis.get(url)
    try:
        if not page_text:
            result = requests.post(url, headers=headers, data=data, timeout=timeout)
            if result.status_code < 400:
                page_text = result.text
                redis.set(url, page_text)
            else:
                return None
    except requests.exceptions.ReadTimeout:
        page_text = None
    except requests.exceptions.MissingSchema:
        page_text = None
    return page_text


def head(url: str, headers: Dict[str, str] = None, timeout: int = None):
    page_text = redis.get(url)
    try:
        if not page_text:
            result = requests.head(url)
            if 3 <= result.status_code / 100 < 4:
                url = result.headers['Location']
                x = {'url': url, 'status_code': 200, 'text': ''}
            elif result.status_code < 300:
                x = {'url': result.url, 'status_code': result.status_code}
            else:
                x = {'url': url, 'status_code': result.status_code}
        else:
            x = {'url': url, 'status_code': 200}
        return x
    except requests.exceptions.ReadTimeout:
        page_text = None
    except requests.exceptions.MissingSchema:
        page_text = None

    x = {'url': url, 'status_code': 1000}

    return x


def get_claim_from_cache(url: str) -> Optional[Claim]:
    result = redis.hgetall("___cached___claim___" + url)
    if result:
        claim = Claim.from_dictionary(result)
        return claim
    else:
        return None


def cache_claim(claim: Claim):
    if claim is not None:
        dictionary = claim.generate_dictionary()
        url = claim.url
        if url is not None and dictionary is not None:
            redis.hmset("___cached___claim___" + url, dictionary)
