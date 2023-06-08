from typing import List

from pydantic import BaseModel, constr, FilePath, validator


class SecretModel(BaseModel):
    id: constr(min_length=1, strict=True)
    value: constr(min_length=1, strict=True)


class SecretsModel(BaseModel):
    secrets: List[SecretModel]

    @validator('secrets')
    def secrets_not_empty(cls, v):
        if not v:
            raise ValueError('secrets list must contain at least one element')
        return v


class KeePassSecretsModel(BaseModel):
    file_path: FilePath
    master_password: constr(min_length=30, strict=True)
    group_name: constr(min_length=1, strict=True)


class GcpSecretsModel(BaseModel):
    project_id: constr(min_length=1, strict=True)
