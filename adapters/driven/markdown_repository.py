import os
from typing import List

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from domain.ports.source_repository_port import SourceRepositoryPort

file_path = os.path.abspath(__file__)
current_folder = os.path.dirname(file_path)
sample_file = os.path.join(current_folder,
                           "markdown_repository/sample_text.md")  # we use this sample file for demo, this can be easily replaced by having an upload function


class MarkdownRepository(SourceRepositoryPort):

    def __init__(self, file_path=sample_file):
        """
        Initialize the MarkdownRepository with a file path.

        :param file_path: Path to the markdown file.
        """
        self.file_path = file_path
        self.paragraphs = self.load_paragraphs(file_path)
        self.vectorizer, self.tfidf_matrix = self.build_tfidf_index(self.paragraphs)

    def load_paragraphs(self, filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
        # Split into paragraphs (empty line separator assumed)
        paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
        return paragraphs

    def build_tfidf_index(self, paragraphs):
        vectorizer = TfidfVectorizer(stop_words="english")
        tfidf_matrix = vectorizer.fit_transform(paragraphs)
        return vectorizer, tfidf_matrix

    def query_on_source(self, query: str) -> List:
        """
        Query the markdown content
        Simple Vector Search using TF-IDF and cosine similarity. This could be replaced by sentence transformers or other advanced methods.
        """
        # Implement the logic to query markdown content

        query_vec = self.vectorizer.transform([query])
        similarity = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        top_indices = np.argsort(similarity)[::-1]

        results = []
        for idx in top_indices:
            results.append((similarity[idx], self.paragraphs[idx]))
        return results


if __name__ == "__main__":
    repo = MarkdownRepository()
    query_result = repo.query_on_source("What is portable magic?", top_n=5)
    for score, paragraph in query_result:
        print(f"Score: {score:.4f}, Paragraph: {paragraph[:100]}...")  # Print first 100 chars of each paragraph
