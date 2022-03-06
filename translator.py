from dataclasses import dataclass
from typing import Protocol


class Translator(Protocol):
    def translate(self, phrase: str) -> str:
        ...


class TranslatorChooser(Protocol):
    def get_translator(self, source_language: str, target_language: str) -> Translator:
        ...


@dataclass
class Request:
    phrase: str
    source_language: str
    target_language: str


@dataclass
class Response:
    translated_phrase: str
    

@dataclass
class TranslationUseCase:
    translator_chooser: TranslatorChooser

    def translate_phrase(self, request: Request) -> Response:
        translator = self.translator_chooser.get_translator(
            source_language=request.source_language,
            target_language=request.target_language,
        )
        translation = translator.translate(request.phrase)
        return Response(
            translated_phrase=translation,
        )
