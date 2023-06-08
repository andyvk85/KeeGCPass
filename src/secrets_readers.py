from abc import ABC, abstractmethod

from google.cloud import secretmanager_v1 as sm
from pykeepass import PyKeePass

from .validation_models import SecretsModel, GcpSecretsModel, SecretModel, KeePassSecretsModel

class SecretsReader(ABC):
    @abstractmethod
    def read_secrets(self) -> SecretsModel:
        pass


class GcpSecretsReader(SecretsReader):
    def __init__(self, config: GcpSecretsModel, client: sm.SecretManagerServiceClient = None):
        self.project_id = config.project_id
        self.client = client or sm.SecretManagerServiceClient()

    def read_secrets(self) -> SecretsModel:
        print('reading Secrets from GCP project "{}"'
              .format(self.project_id))

        secrets = []

        project_path = self.client.common_project_path(self.project_id)
        request = sm.ListSecretsRequest()
        request.parent = project_path

        response = self.client.list_secrets(request)

        for secret in response:
            secret_name = self.client.parse_secret_path(secret.name)['secret']
            latest_version_path = self.client.secret_version_path(self.project_id, secret_name, 'latest')
            latest_version = self.client.access_secret_version(name=latest_version_path)
            secret_value = latest_version.payload.data.decode('UTF-8')
            secrets.append(SecretModel(id=secret_name, value=secret_value))

        print(f'read: {len(secrets)} Secrets')

        return SecretsModel(secrets=secrets)


class KeePassSecretsReader(SecretsReader):
    def __init__(self, config: KeePassSecretsModel):
        self.file_path = str(config.file_path)
        self.master_password = config.master_password
        self.group_name = config.group_name

    def read_secrets(self) -> SecretsModel:
        print('reading Secrets from KeePass Group "{}" in KeePass Store "{}"'
              .format(self.group_name, self.file_path))

        secrets = []

        with PyKeePass(self.file_path, self.master_password) as kp:
            child_group = kp.find_groups(name=self.group_name, first=True)

            if child_group is None:
                raise TypeError('The KeePass Group named "{}" could not be found in KeePass Store "{}"'
                                .format(self.group_name, self.file_path))

            for entry in child_group.entries:
                secrets.append(SecretModel(id=entry.title, value=entry.password))

        print(f'read: {len(secrets)} Secrets')

        return SecretsModel(secrets=secrets)
