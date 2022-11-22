from ariadne import ObjectType
from ariadne import UnionType

query = ObjectType("Query")
union = UnionType("TestUnion")


@union.type_resolver
def resolve_error_type(obj, *_):
    if obj['subtype'] == 'account.partner':
        return "Partner"
    if obj['subtype'] == 'account.network':
        return "Network"
    if obj['subtype'] == 'account.publisher':
        return "Publisher"

    return None


@query.field("hello")
def resolve_hello(*_):
    return [
        {
            'subtype': 'account.publisher',
            'name': 'Beatka',
            'value_test_publisher': 2137
        },
        {
            'subtype': 'account.network',
            'name': 'Stanisław',
            'value_test_network': True
        },
        {
            'subtype': 'account.partner',
            'name': 'Andrzej',
            'value_test_partner': "TestStringValu źćżżźćąś∂Ń"
        },
        {
            'subtype': 'account.network',
            'name': 'Jarosław',
            'value_test_network': False
        },
    ]