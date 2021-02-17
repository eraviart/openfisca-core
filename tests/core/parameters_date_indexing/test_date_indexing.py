import os
import numpy as np


from openfisca_core.tools import assert_near
from openfisca_core.parameters import ParameterNode
from openfisca_core.model_api import *  # noqa

LOCAL_DIR = os.path.dirname(os.path.abspath(__file__))

parameters = ParameterNode(directory_path = LOCAL_DIR)

P = parameters.trimtp_rg('1995-01-01')


def get_message(error):
    return error.args[0]


def test_on_leaf():
    date_de_naissance = np.array(['1930-01-01', '1935-01-01', '1940-01-01', '1945-01-01'], dtype = 'datetime64[D]')
    assert_near(P.nombre_trimestres_cibles_par_generation[date_de_naissance], [150, 152, 157, 160])


# def test_on_node():
#     housing_occupancy_status = np.asarray(['owner', 'owner', 'tenant', 'tenant'])
#     node = P.single[housing_occupancy_status]
#     assert_near(node.z1, [100, 100, 300, 300])
#     assert_near(node['z1'], [100, 100, 300, 300])
#
# def test_wrong_key():
#     zone = np.asarray(['z1', 'z2', 'z2', 'toto'])
#     with pytest.raises(ParameterNotFound) as e:
#         P.single.owner[zone]
#     assert "'rate.single.owner.toto' was not found" in get_message(e.value)
#
#
# def test_inhomogenous():
#     parameters = ParameterNode(directory_path = LOCAL_DIR)
#     parameters.rate.couple.owner.add_child('toto', Parameter('toto', {
#         "values": {
#             "2015-01-01": {
#                 "value": 1000
#                 },
#             }
#         }))

#     P = parameters.rate('2015-01-01')
#     housing_occupancy_status = np.asarray(['owner', 'owner', 'tenant', 'tenant'])
#     with pytest.raises(ValueError) as error:
#         P.couple[housing_occupancy_status]
#     assert "'rate.couple.owner.toto' exists" in get_message(error.value)
#     assert "'rate.couple.tenant.toto' doesn't" in get_message(error.value)
#
#
# def test_inhomogenous_2():
#     parameters = ParameterNode(directory_path = LOCAL_DIR)
#     parameters.rate.couple.tenant.add_child('toto', Parameter('toto', {
#         "values": {
#             "2015-01-01": {
#                 "value": 1000
#                 },
#             }
#         }))

#     P = parameters.rate('2015-01-01')
#     housing_occupancy_status = np.asarray(['owner', 'owner', 'tenant', 'tenant'])
#     with pytest.raises(ValueError) as e:
#         P.couple[housing_occupancy_status]
#     assert "'rate.couple.tenant.toto' exists" in get_message(e.value)
#     assert "'rate.couple.owner.toto' doesn't" in get_message(e.value)


# def test_inhomogenous_3():
#     parameters = ParameterNode(directory_path = LOCAL_DIR)
#     parameters.rate.couple.tenant.add_child('z4', ParameterNode('toto', data = {
#         'amount': {
#             'values': {
#                 "2015-01-01": {'value': 550},
#                 "2016-01-01": {'value': 600}
#                 }
#             }
#         }))

#     P = parameters.rate('2015-01-01')
#     zone = np.asarray(['z1', 'z2', 'z2', 'z1'])
#     with pytest.raises(ValueError) as e:
#         P.couple.tenant[zone]
#     assert "'rate.couple.tenant.z4' is a node" in get_message(e.value)
#     assert re.findall(r"'rate.couple.tenant.z(1|2|3)' is not", get_message(e.value))
