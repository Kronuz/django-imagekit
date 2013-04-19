class BoundImageKitMeta(object):
    def __init__(self, instance, spec_fields):
        self.instance = instance
        self.spec_fields = spec_fields
        self.source_hashes = {}

    @property
    def spec_files(self):
        return [getattr(self.instance, n) for n in self.spec_fields]


class ImageKitMeta(object):
    def __init__(self, spec_fields=None):
        self.spec_fields = list(spec_fields) if spec_fields else []

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            ik = BoundImageKitMeta(instance, self.spec_fields)
            instance.__dict__['_ik'] = ik
            return ik
