"""
Association Pools
"""
from astropy.io.ascii import convert_numpy

from astropy.table import Table

__all__ = ['AssociationPool']

DEFAULT_DELIMITER = '|'
DEFAULT_FORMAT = 'ascii'


class AssociationPool(Table):
    """Association Pool

    An AssociationPool is essentially and astropy Table with the
    following default behaviors:

    - ASCII tables with a default delimiater of `|`
    - All values are read in as strings
    """

    @classmethod
    def read(
            cls,
            filename,
            delimiter=DEFAULT_DELIMITER,
            format=DEFAULT_FORMAT,
            **kwargs
    ):
        """Read in a Pool file
        """
        table = super(AssociationPool, cls).read(
            filename, delimiter=delimiter,
            format=format,
            converters=_ConvertToStr(), **kwargs
        )
        table.meta['pool_file'] = filename
        return table

    def write(self, *args, **kwargs):
        """Write the pool to a file.
        """
        delimiter = kwargs.pop('delimiter', DEFAULT_DELIMITER)
        format = kwargs.pop('format', DEFAULT_FORMAT)
        super(AssociationPool, self).write(
            *args, delimiter=delimiter, format=format, **kwargs
        )


class _ConvertToStr(dict):
    def __getitem__(self, k):
        return [convert_numpy(str)]

    def get(self, k, default=None):
        return self.__getitem__(k)
