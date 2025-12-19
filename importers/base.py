from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def parse(self, filepath):
        raise NotImplementedError
