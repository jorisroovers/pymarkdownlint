import fnmatch
import os


class MarkdownFileFinder(object):
    @staticmethod
    def find_files(path, filter="*.md"):
        """ Finds files with an (optional) given extension in a given path. """
        if os.path.isfile(path):
            return [path]

        if os.path.isdir(path):
            matches = []
            for root, dirnames, filenames in os.walk(path):
                for filename in fnmatch.filter(filenames, filter):
                    matches.append(os.path.join(root, filename))
            return matches
