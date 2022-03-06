from translator import TranslationUseCase, Request, Translator
from dataclasses import dataclass
from typing import Dict, Tuple
import argparse


@dataclass
class DictionaryTranslator:
    translations: Dict[str, str]

    def translate(self, phrase: str) -> str:
        return self.translations[phrase]


@dataclass
class CliChooser:
    translators: Dict[Tuple[str, str], DictionaryTranslator]
    
    def get_translator(self, source_language: str, target_language: str) -> Translator:
        return self.translators[(source_language, target_language)]


def get_request_from_user_input() -> Request:
    parser = argparse.ArgumentParser(description="Translates hello world")
    parser.add_argument("--source", default="en")
    parser.add_argument("--target", default="de")
    parser.add_argument("phrase")
    arguments = parser.parse_args()
    return Request(
        source_language=arguments.source,
        target_language=arguments.target,
        phrase=arguments.phrase,
    )


def get_translation_dictionaries() -> Dict[Tuple[str, str], DictionaryTranslator]:
    return {
        ('en', 'de'): DictionaryTranslator(translations={
            'Hello, World!': "Hallo, Welt!",
        })
    }


def main() -> None:
    request = get_request_from_user_input()
    translators = get_translation_dictionaries()
    chooser = CliChooser(translators=translators)
    use_case = TranslationUseCase(
        translator_chooser=chooser
    )
    response = use_case.translate_phrase(request)
    print(response)


if __name__ == "__main__":
    main()
