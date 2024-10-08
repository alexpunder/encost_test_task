from tortoise import fields
from tortoise.models import Model


class Client(Model):
    id = fields.IntField(primary_key=True)
    client_name = fields.TextField()

    class Meta:
        table = 'clients'

    def __str__(self):
        return self.client_name


class Endpoint(Model):
    id = fields.IntField(primary_key=True)
    endpoint_name = fields.TextField()

    class Meta:
        table = 'endpoints'

    def __str__(self):
        return self.endpoint_name


class EndpointStates(Model):
    id = fields.IntField(primary_key=True)
    endpoint = fields.ForeignKeyField(
        'models.Endpoint',
        related_name='endpoint_states',
    )
    client = fields.ForeignKeyField(
        'models.Client',
        related_name='client_states',
    )
    state_name = fields.TextField()
    state_reason = fields.TextField()
    state_start = fields.IntField()
    state_end = fields.IntField(null=True)
    state_id = fields.TextField()
    group_id = fields.TextField()
    reason_group = fields.TextField(null=True)
    info = fields.JSONField(null=True)

    class Meta:
        table = 'endpoint_states'
