# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Implements command to remove an SSH Public Key from the OS Login Profile."""

from googlecloudsdk.api_lib.oslogin import client
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.oslogin import flags
from googlecloudsdk.command_lib.oslogin import oslogin_utils
from googlecloudsdk.command_lib.util import gaia


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class Remove(base.Command):
  """Remove an SSH Public Key from an OS Login Profile."""

  def __init__(self, *args, **kwargs):
    super(Remove, self).__init__(*args, **kwargs)

  @staticmethod
  def Args(parser):
    """Set up arguments for this command.

    Args:
      parser: An argparse.ArgumentParser.
    """
    additional_help = (' Key value can either be the SSH key or the '
                       'OS Login fingerprint of the key.')
    flags.AddKeyFlags(parser, 'remove from', additional_help=additional_help)

  def Run(self, args):
    """See ssh_utils.BaseSSHCLICommand.Run."""
    key = flags.GetKeyFromArgs(args)
    oslogin_client = client.OsloginClient(self.ReleaseTrack())
    user_email = gaia.GetAuthenticatedGaiaEmail(oslogin_client.client.http)

    keys = oslogin_utils.GetKeyDictionaryFromProfile(user_email, oslogin_client)
    fingerprint = oslogin_utils.FindKeyInKeyList(key, keys)
    if fingerprint:
      return oslogin_client.DeleteSshPublicKey(user_email, fingerprint)
    else:
      raise client.OsloginKeyNotFoundError('Cannot find requested SSH key.')


Remove.detailed_help = {
    'brief': 'Remove an SSH Public Key from an OS Login Profile.',
    'DESCRIPTION': """\
      *{command}* will take either a string containing an SSH Public
      Key or a filename for an SSH Public key and will remove that key from the
      user's OS Login Profile. The key value passed in can either be the
      full SSH key or the OS Login fingerprint for that key.
    """
}

