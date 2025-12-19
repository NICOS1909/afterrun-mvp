from .base import Importer


class GPXImporter(Importer):
    def parse(self, filepath):
        # TODO: implement GPX parsing
        return {"type": "gpx", "path": filepath}
