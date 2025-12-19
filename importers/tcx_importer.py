from .base import Importer


class TCXImporter(Importer):
    def parse(self, filepath):
        # TODO: implement TCX parsing
        return {"type": "tcx", "path": filepath}
