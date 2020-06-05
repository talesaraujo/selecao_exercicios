#!/usr/bin/env python3
import unittest 
import os, zipfile, shutil

from renomear import apply_changes


class TestRenomear(unittest.TestCase):

    def setUp(self):
        """
        Unzips a sample set with images into a test folder
        """
        self.zipped_file = "img_samples.zip"
        self.target_folder = "test_folder"

        with zipfile.ZipFile(self.zipped_file, 'r') as zip_ref:
            zip_ref.extractall(self.target_folder)


    def test_sequential_filenames_do_match(self):
        """
        Tests whether every folder actually matches the number sequence
        """
        apply_changes(self.target_folder)

        for index, _file in enumerate(sorted(os.listdir())):
            file_name, _ = os.path.splitext(_file)
            self.assertEqual(index+1, int(file_name))


    def tearDown(self):
        """
        Undo the changes
        """
        old_path = os.path.join(os.getcwd(), "..", self.target_folder)
        shutil.rmtree(old_path)


if __name__ == "__main__":
    unittest.main()
