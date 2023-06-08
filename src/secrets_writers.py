from abc import abstractmethod, ABC
from typing import List

from google.cloud import secretmanager_v1 as sm
from google.cloud.secretmanager_v1 import SecretVersion
from pykeepass import PyKeePass

from .validation_models import KeePassSecretsModel, GcpSecretsModel, SecretsModel


class SecretsWriter(ABC):
    @abstractmethod
    def write_secrets(self, data: SecretsModel):
        pass


class GcpSecretsWriter(SecretsWriter):
    def __init__(self, config: GcpSecretsModel, client: sm.SecretManagerServiceClient = None):
        super().__init__()
        self.project_id = config.project_id
        self.client = client or sm.SecretManagerServiceClient()

    def write_secrets(self, data: SecretsModel) -> List[SecretVersion]:
        print('writing "{}" Secrets to GCP Project "{}"'
              .format(len(data.secrets), self.project_id))

        responses = []

        for secret in data.secrets:
            resource_name = self.client.secret_path(self.project_id, secret.id)
            print(f'{resource_name}')

            payload = sm.SecretPayload()
            payload.data = secret.value.encode('UTF-8')

            request = sm.AddSecretVersionRequest()
            request.parent = resource_name
            request.payload = payload

            response = self.client.add_secret_version(request)
            responses.append(response)

            print(f'created: "{response.name}"')

        return responses


class KeePassSecretsWriter(SecretsWriter):
    def __init__(self, config: KeePassSecretsModel):
        super().__init__()
        self.file_path = config.file_path
        self.master_password = config.master_password
        self.group_name = config.group_name

    def write_secrets(self, data: SecretsModel) -> None:
        print('writing "{}" Secrets to KeePass Group "{}" in KeePass Store "{}"'
              .format(len(data.secrets), self.group_name, self.file_path))

        with PyKeePass(self.file_path, self.master_password) as kp:
            child_group = kp.add_group(kp.root_group, self.group_name)

            for secret in data.secrets:
                kp.add_entry(
                    destination_group=child_group,
                    title=secret.id,
                    username='',
                    password=secret.value,
                )
                print(f'created: "{secret.id}"')

            kp.save()
