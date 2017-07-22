# coding: utf8


class Mapping(dict):
    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, key):
        if key in self:
            value = self[key]
            if isinstance(value, (tuple, list)):
                cls = type(value)
                return cls((
                    self.__class__(v) if isinstance(v, dict) else v
                    for v in value
                ))
            elif isinstance(value, dict):
                return self.__class__(value)
            else:
                return value
        raise AttributeError(
            '{cls} object has no attribute {key!r}'.format(
                cls=self.__class__, key=key)
        )

    def __getitem__(self, key):
        value = super().__getitem__(key)
        if isinstance(value, (tuple, list)):
            cls = type(value)
            return cls((
                self.__class__(v) if isinstance(v, dict) else v
                for v in value
            ))
        elif isinstance(value, dict):
            return self.__class__(value)
        else:
            return value
