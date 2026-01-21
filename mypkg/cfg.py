# Tests/experiments on a generic class managing configuration data
#
# AUTHOR Sven Schrodt
# SINCE 2026-01-21


class Config:
    """
    Class managing config dats
    """

    
    _cfg = {
        "id": 1234556,
        # ....
    }

    def __init__(self, cfg=None):
        """
        Initialize (meta) data

        :param self:
        :param file: origin of feature data
        """
        if cfg is not None:
            self.inject(cfg)
        
        
    def inject(self, cfg):
        '''
        Injecting configuration data -> will be merged with existing config
        
        :param self: 
        :param cfg: dict with (new) configuration attributes
        '''

        self._cfg = self._cfg | cfg
        return self

    def __str__(self):
        pass


if __name__ == "__main__":
    foo = Config()

    print(foo.inject({'bar': 'foo', 'id': 666})._cfg)