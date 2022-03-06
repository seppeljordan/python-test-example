from unittest import TestCase
from dataclasses import dataclass
from translator import TranslationUseCase, Request
from typing import Dict, Tuple


class TranslatorTests(TestCase):
    def setUp(self) -> None:
        pass

    def test_can_translate_hello_world_from_english_to_german(self) -> None:
        chooser = TestTranslatorChooser(translator_mapping={
            ('en', 'de'): Translator()
        })
        translator = chooser.get_translator('en', 'de')
        use_case = TranslationUseCase(
            translator_chooser=chooser,
        )
        response = use_case.translate_phrase(
            request = Request(
                phrase="Hello, World!",
                source_language="en",
                target_language="de",                
            )
        )
        self.assertEqual(
            response.translated_phrase,
            translator.translate("Hello, World!")
        )


class Translator:
    def translate(self, phrase: str) -> str:
        return phrase + " translated"


@dataclass
class TestTranslatorChooser:
    translator_mapping: Dict[Tuple[str, str], Translator]
    
    def get_translator(self, source_language: str, target_language: str) -> Translator:
        return self.translator_mapping[(source_language, target_language)]
