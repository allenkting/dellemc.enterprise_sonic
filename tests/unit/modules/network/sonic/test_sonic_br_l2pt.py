from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.dellemc.enterprise_sonic.tests.unit.compat.mock import (
    patch,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.modules import (
    sonic_br_l2pt,
)
from ansible_collections.dellemc.enterprise_sonic.tests.unit.modules.utils import (
    set_module_args,
)
from .sonic_module import TestSonicModule


class TestSonicBrL2PTModule(TestSonicModule):
    module = sonic_br_l2pt

    @classmethod
    def setUpClass(cls):
        cls.mock_facts_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.br_l2pt.br_l2pt.edit_config"
        )
        cls.mock_config_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.br_l2pt.br_l2pt.edit_config"
        )
        cls.mock_utils_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils.edit_config"
        )
        cls.mock_get_interface_naming_mode = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils.get_device_interface_naming_mode"
        )
        cls.fixture_data = cls.load_fixtures('sonic_br_l2pt.yaml')

    def setUp(self):
        try:
            super(TestSonicBrL2PTModule, self).setUp()
            self.facts_edit_config = self.mock_facts_edit_config.start()
            self.config_edit_config = self.mock_config_edit_config.start()
            self.facts_edit_config.side_effect = self.facts_side_effect
            self.config_edit_config.side_effect = self.config_side_effect
            self.get_interface_naming_mode = self.mock_get_interface_naming_mode.start()
            self.get_interface_naming_mode.return_value = 'native'
            self.utils_edit_config = self.mock_utils_edit_config.start()
            self.utils_edit_config.side_effect = self.facts_side_effect
            print(f"Mocks initialized:\n{self.facts_edit_config}\n{self.config_edit_config}\n{self.utils_edit_config}")
        except Exception as e:
            print(f"Error in setUp: {e}")
            raise

    def tearDown(self):
        super(TestSonicBrL2PTModule, self).tearDown()
        self.mock_facts_edit_config.stop()
        self.mock_config_edit_config.stop()
        self.mock_get_interface_naming_mode.stop()
        self.mock_utils_edit_config.stop()

    def test_sonic_br_l2pt_merged_01(self):
        set_module_args(self.fixture_data['merged_01']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['merged_01']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['merged_01']['config_requests'])

        print('FACTS GET REQS: ' + str(self.fixture_data['merged_01']['facts_get_requests']))
        print('CONFIG REQS: ' + str(self.fixture_data['merged_01']['config_requests']))
        result = self.execute_module(changed=True)
        self.validate_config_requests()
