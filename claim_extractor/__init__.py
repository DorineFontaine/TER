from typing import Dict


class Claim:

    def __init__(self):
        """
        Default constructor, see other constructor to build object from dictionary
        """
        self.source = ""
        self.claim = str("")
        self.body = str("")
        self.referred_links = ""
        self.title = str("")
        self.date = ""
        self.url = ""
        self.tags = ""
        self.author = ""
        self.datePublished = ""
        self.sameAs = ""
        self.source_url = ""
        self.rating_value = ""
        self.worst_rating = ""
        self.best_rating = ""
        self.alternate_name = ""

    def generate_dictionary(self):
        if isinstance(self.referred_links, list):
            self.referred_links = ",".join(self.referred_links)
        dictionary = {'rating_ratingValue': self.rating_value, 'rating_worstRating': self.worst_rating,
                      'rating_bestRating': self.best_rating, 'rating_alternateName': self.alternate_name,
                      'creativeWork_author_name': self.author, 'creativeWork_datePublished': self.datePublished,
                      'creativeWork_author_sameAs': self.sameAs, 'claimReview_author_name': self.source,
                      'claimReview_author_url': self.source_url, 'claimReview_url': self.url,
                      'claimReview_claimReviewed': self.claim, 'claimReview_datePublished': self.date,
                      'extra_body': self.body.replace("\n", ""), 'extra_refered_links': self.referred_links,
                      'extra_title': self.title, 'extra_tags': self.tags}
        return dictionary

    @classmethod
    def from_dictionary(cls, dictionary: Dict[str, str]) -> 'Claim':
        """
        Build claim instance from dictionary generated by the generate_dictionary method, mainly used for round tripping
        from cache.
        :param dictionary: The dictionary generated by generate_dictionary
        """
        claim = Claim()
        if 'claimReview_author_name' in dictionary.keys():
            claim.source = dictionary['claimReview_author_name']
        else:
            claim.source = ""
        claim.claim = dictionary["claimReview_claimReviewed"]
        claim.body = dictionary['extra_body']
        claim.referred_links = dictionary['extra_refered_links']
        claim.title = dictionary['extra_title']
        claim.date = dictionary['claimReview_datePublished']
        claim.url = dictionary['claimReview_url']
        claim.tags = dictionary['extra_tags']
        claim.author = dictionary['creativeWork_author_name']
        claim.datePublished = dictionary['creativeWork_datePublished']
        claim.sameAs = dictionary['creativeWork_author_sameAs']
        claim.source_url = dictionary['claimReview_author_url']
        claim.rating_value = dictionary['rating_ratingValue']
        claim.worst_rating = dictionary['rating_worstRating']
        claim.best_rating = dictionary['rating_bestRating']
        claim.alternate_name = dictionary['rating_alternateName']

        return claim

    def set_rating_value(self, string_value):
        if string_value:
            string_value = str(string_value).replace('"', "")
            self.rating_value = string_value
        return self

    def setWorstRating(self, str_):
        if str_:
            str_ = str(str_).replace('"', "")
            self.worst_rating = str_
        return self

    def set_best_rating(self, str_):
        if str_:
            str_ = str(str_).replace('"', "")
            self.best_rating = str_
        return self

    def setAlternateName(self, alternate_name):
        alternate_name = str(alternate_name).replace('"', "")
        # split sentence

        if "." in alternate_name:
            split_name = alternate_name.split(".")
            if len(split_name) > 0:
                self.alternate_name = split_name[0]

        return self

    def setSource(self, str_):
        self.source = str_
        return self

    def setAuthor(self, str_):
        self.author = str_
        return self

    def setSameAs(self, str_):
        self.sameAs = str_
        return self

    def setDatePublished(self, str_):
        self.datePublished = str_
        return self

    def setClaim(self, str_):
        self.claim = str(str_)
        return self

    def setBody(self, str_):
        self.body = str(str_)
        return self

    def set_refered_links(self, str_):
        self.referred_links = str_
        return self

    def setTitle(self, str_):
        self.title = str(str_)
        return self

    def setDate(self, str_):
        self.date = str_
        return self

    def setUrl(self, str_):
        self.url = str(str_)
        return self

    def set_tags(self, str_):
        self.tags = str_


class Configuration:

    def __init__(self):
        self.maxClaims = 0
        self.within = "15mi"
        self.output = "output.csv"
        self.website = ""
        self.until = None
        self.since = None
        self.html = False
        self.entity = False
        self.input = None
        self.rdf = None
        self.avoid_urls = []
        self.update_db = False
        self.entity_link = False
        self.normalize_credibility = True
        self.parser_engine = "lxml"

    def setSince(self, since):
        self.since = since
        return self

    def setUntil(self, until):
        self.until = until
        return self

    def setMaxClaims(self, maxClaims):
        self.maxTweets = maxClaims
        return self

    def setOutput(self, output):
        self.output = output
        return self

    def setWebsite(self, website):
        self.website = website
        return self
