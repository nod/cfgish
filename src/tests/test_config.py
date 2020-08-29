
'''
test our configuration module
'''

from os import path
from unittest import TestCase

import cfgish

fixtures_path = path.join(
    path.abspath(path.dirname(__file__)),
    "fixtures"
    )


class TestConfig(TestCase):

    def setUp(self):
        pass

    def testOverrides(self):
        fakeval = 999
        c = cfgish.Configurator(feh=fakeval)
        self.assertEqual(c.get('feh'), fakeval)

class TestConfigFile(TestCase):
    def setUp(self):
        self.old_env_prefix = cfgish.ENV_PREFIX

    def tearDown(self):
        cfgish.ENV_PREFIX = self.old_env_prefix

    def testConfigFile(self):
        rcfile = path.join(fixtures_path, "cfgrc")
        c = cfgish.Configurator(rcfile)
        self.assertEqual(c.get("s3:access_key"), 'access')

    def testEnvKeys(self):
        ''' ensure we create env names properly '''
        c = cfgish.Configurator()
        self.assertEqual(
            'CFG_S3_ACCESS_KEY',
            c._name_to_env_key('s3:access_key')
            )
        # now test overriding env prefix
        cfgish.ENV_PREFIX = 'BLIPPY_'
        self.assertEqual(
            'BLIPPY_S3_ACCESS_KEY',
            c._name_to_env_key('s3:access_key')
            )

