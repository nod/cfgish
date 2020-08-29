
from configparser import ConfigParser
from os import environ, path

ENV_PREFIX = 'CFG_'

class Configurator:
    _values = None
    _cfgfile = None
    def __init__(self, cfgish_rcfile=None, **overrides):
        # create our values dict by copying the overrides
        self._values = dict(**overrides)
        if cfgish_rcfile is not None:
            self._load_cfg_values(cfgish_rcfile)

    def _load_cfg_values(self, cfg_rcfile):
        '''
        attempts to load from a config file if specified
        '''
        if path.isfile(cfg_rcfile):
            self._cfgfile = ConfigParser()
            self._cfgfile.read(cfg_rcfile)
        else:
            raise FileNotFoundError('config file specified but not found')

    def _name_to_env_key(self, name):
        return "{}{}".format(ENV_PREFIX, name.replace(':','_').upper())

    def get(self, name):
        # first, check our overrides
        if name in self._values:
            return self._values.get(name)
        # next we check our environment
        envkey = self._name_to_env_key(name)
        if envkey in environ:
            return self.environ.get(envkey)
        # next check our config file
        if self._cfgfile is not None:
            return self._cfgfile.get(*name.split(':'))

    def set(self, name, val):
        self._values[name] = val


