import spacy


class Tokenizer:
    def __init__(self, name: str = "ru_core_news_sm"):
        self.nlp = spacy.load(name)

    def __call__(self, text: str) -> list:
        doc = self.nlp(text)
        return [
            token.lemma_ for token in doc if not token.is_stop and not token.is_punct
        ]
