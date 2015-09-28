__author__ = 'ryu'

import json
from pandas import DataFrame

obj = """
{"name": "Wes",
"places_lived": ["United States", "Spain", "Germany"],
"pet": null,
"siblings": [{"name": "Scott", "age": 25, "pet": "Zuko"},
{"name": "Katie", "age": 33, "pet": "Cisco"}]
}
"""

result = json.loads(obj)
print result['siblings']

asjson = json.dumps(result)
siblings = DataFrame(result['siblings'], columns=['name', 'age'])
