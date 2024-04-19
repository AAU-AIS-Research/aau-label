from typing import List, Protocol

from PIL.Image import Image

from ..model import Label


class LabelParser(Protocol):
    file_extension: str

    def parse(self, label_file: str, image: Image) -> List[Label]:
        raise NotImplementedError
