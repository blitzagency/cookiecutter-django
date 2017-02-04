import json
from django.core.urlresolvers import reverse
from django.test import TestCase

# from templatecms.models import Copy



def test_foo():
    print(99)
# class RegisterCase(TestCase):

#     def test_empty(self):

#         data = {
#             "data": {
#                 "foo": "bar"
#             }
#         }

#         resp = self.client.post(
#             reverse("admin:templatecms_copy_api_update"),
#             json.dumps(data),
#             content_type="application/json")

#         copy_model = Copy.objects.get(id=1)
#         self.assertEqual({'foo': 'bar'}, copy_model.copy)
#         self.assertEqual(resp.status_code, 200)
