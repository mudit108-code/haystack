from canals import component
from canals.serialization import default_from_dict, default_to_dict
from canals.errors import DeserializationError, ComponentError
from haystack.preview.pipeline import Pipeline
from haystack.preview.dataclasses import Document, Answer, GeneratedAnswer, ExtractedAnswer
