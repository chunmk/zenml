#  Copyright (c) maiot GmbH 2020. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.

# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. currentmodule:: ce_cli.cli
.. moduleauthor:: maiot GmbH <support@maiot.io>
"""

import click

from zenml.cli.utils import pass_config
from zenml.utils.logger import set_verbosity


@click.group()
@click.option("--verbose", "-v", default=0, count=True,
              help="Enable verbose output.")
@pass_config
def cli(info, verbose: int):
    """maiot ZenML"""
    info.load()
    set_verbosity(verbose)


if __name__ == '__main__':
    cli()
