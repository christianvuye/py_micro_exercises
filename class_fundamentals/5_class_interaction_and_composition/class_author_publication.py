"""
Create a publishing system where Authors and Publications track each other.

Requirements for Author class:
- Initialize with name, author_id, and empty list of publications
- Create method add_publication(publication) that adds to author's list
- Create method get_publication_count() that returns number of publications
- Create method get_author_summary() with name and publication titles

Requirements for Publication class:
- Initialize with title, publication_id, and empty list of authors
- Create method add_author(author) that adds to publication's author list
- Create method remove_author(author_name) that removes author by name
- Create method get_publication_info() with title and author names

Critical Requirement:
- When an author adds a publication, the publication should automatically add that author
- When a publication adds an author, the author should automatically add that publication
- Prevent infinite loops and duplicate relationships

Test your system:
author1 = Author("Jane Smith", "A001")
pub1 = Publication("Python Basics", "P001")

# Test bidirectional sync from both directions
author1.add_publication(pub1)
print(f"Author has {author1.get_publication_count()} publications")  # Should print 1
print(f"Publication has {len(pub1.authors)} authors")                # Should print 1

author2 = Author("John Doe", "A002")
pub1.add_author(author2)
print(f"Author2 has {author2.get_publication_count()} publications") # Should print 1
print(f"Publication has {len(pub1.authors)} authors")                # Should print 2
"""


class Author:
    def __init__(self, name, author_id):
        self.name = name
        self.author_id = author_id
        self.publications = []

    def add_publication(self, publication):
        # if you do this:
        # self.publications.append(publication)
        # publication.add_author(self)

        # you will get this:
        # maximum recursion depth exceeded?
        # When calling add_author it also calls add_publication recursively and it keeps looping infinitely

        # so check first if the publication/author don't already exist in each others lists!
        if publication not in self.publications:
            self.publications.append(publication)
            publication.add_author(self)

    def get_publication_count(self):
        return len(self.publications)

    def get_author_summary(self):
        publication_titles = (
            "No titles publised"
            if len(self.publications) == 0
            else [publication.title for publication in self.publications]
        )
        return f"Author name: {self.name}, publications: {publication_titles}"


class Publication:
    def __init__(self, title, publication_id):
        self.title = title
        self.publication_id = publication_id
        self.authors = []

    def add_author(self, author):
        # avoid making the same mistake as above, do not do this:
        # self.authors.append(author)
        # author.add_publication(self)

        # instead:
        if author not in self.authors:
            self.authors.append(author)
            author.add_publication(self)

    def remove_author(
        self, author_name
    ):  # shouldnt this also work bidirectionally? Have a remove publication method?
        for author in self.authors:
            if author.name == author_name:
                self.authors.remove(author)
                break

    # yes, it should and the other class too
    # def remove_author(self, author_name):  # Bidirectional removal
    # for author in self.authors:
    # if author.name == author_name:
    # self.authors.remove(author)
    # author.remove_publication(self.title)  # Clear other side
    # break

    def get_publication_info(self):
        return f"Publication title: {self.title}, author names: {[author.name for author in self.authors]}"


author1 = Author("Jane Smith", "A001")
pub1 = Publication("Python Basics", "P001")

# Test bidirectional sync from both directions
author1.add_publication(pub1)
print(f"Author has {author1.get_publication_count()} publications")  # Should print 1
print(f"Publication has {len(pub1.authors)} authors")  # Should print 1

author2 = Author("John Doe", "A002")
pub1.add_author(author2)
print(f"Author2 has {author2.get_publication_count()} publications")  # Should print 1
print(f"Publication has {len(pub1.authors)} authors")  # Should print 2
