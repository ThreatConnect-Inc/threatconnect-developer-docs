# -*- coding: utf-8 -*-
"""Playbook App Template."""
# first-party
from args import Args


class PlaybookApp:
    """Playbook App Class."""

    def __init__(self, _tcex):
        """Initialize class properties."""
        self.tcex = _tcex
        self.args = None
        self.exit_message = 'Success'

        # automatically parse args on init
        self.parse_args()

    def parse_args(self):
        """Parse CLI args."""
        Args(self.tcex.parser)
        self.args = self.tcex.args

    def run(self):
        """Run the App main logic."""
        self.tcex.log.info('No run logic provided.')

    def setup(self):
        """Perform prep/setup logic."""
        # run legacy method
        if hasattr(self, 'start'):
            self.tcex.log.warning('calling legacy start method')
            self.start()  # pylint: disable=no-member
        self.tcex.log.trace('setup')

    def teardown(self):
        """Perform cleanup/teardown logic."""
        # run legacy method
        if hasattr(self, 'done'):
            self.tcex.log.warning('calling legacy done method')
            self.done()  # pylint: disable=no-member
        self.tcex.log.trace('teardown')

    def write_output(self):
        """Write the Playbook output variables."""
        self.tcex.log.info('No output variables written.')
