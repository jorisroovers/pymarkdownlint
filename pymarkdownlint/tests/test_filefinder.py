from pymarkdownlint.tests.base import BaseTestCase

from pymarkdownlint.filefinder import MarkdownFileFinder

import os


class FileFinderTests(BaseTestCase):
    def test_find_files(self):
        sample_dir = self.get_sample_path()
        sample1 = os.path.join(sample_dir, "sample1.md")
        sample2 = os.path.join(sample_dir, "sample2.md")
        files = MarkdownFileFinder.find_files(sample_dir)
        self.assertListEqual(files, [sample1, sample2])

        files = MarkdownFileFinder.find_files(sample_dir, filter="*.txt")
        txt1 = os.path.join(sample_dir, "ignored-sample1.txt")
        txt2 = os.path.join(sample_dir, "ignored-sample2.txt")
        self.assertListEqual(files, [txt1, txt2])
