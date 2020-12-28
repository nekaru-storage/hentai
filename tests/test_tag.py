import unittest
from urllib.parse import urljoin

from hentai import Hentai, Tag, Option

class TestTag(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_response = Hentai(177013)

    def test_get(self):
        self.assertEqual(Tag.get(self.test_response.language, 'name'), "english, translated", msg=f"Language Tag: {self.test_response.language}")
    
    def test_get_exception(self):
        with self.assertRaises(ValueError) as context:
            Tag.get(self.test_response.language, 'upload_date')
        self.assertTrue('DNE', context.exception)

    def test_list(self):
        characters = Tag.list(Option.Character)
        for character in characters:
            if character.name == 'holo':
                self.assertEqual(character.id, 33918)
                self.assertEqual(character.type, 'character')
                self.assertEqual(character.name, 'holo')
                self.assertEqual(character.url, urljoin(Hentai.HOME, '/character/holo/'))
                self.assertEqual(character.count, 160)
                break

    def test_list_first_exception(self):
        with self.assertRaises(ValueError) as context:
            Tag.list(Option.Epos)
        self.assertTrue('Epos Option is not supported', context.exception)

    def test_list_second_exception(self):
        with self.assertRaises(NotImplementedError) as context:
            Tag.list(Option.Category)
        self.assertTrue('Category Exception is not implemented', context.exception)
