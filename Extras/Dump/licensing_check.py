
data = '{"statusResp":{"statusCode":"S007","message":"Success","snStatus":"Active","warrantyStart":"2016-05-18","warrantyEnd":"2016-08-31","companyBPID":"0002210887","siteBPID":"0002210888","contractStart":"2016-05-18","contractEnd":"2021-12-31","product":"FDvM300","version":"1","serialNumber":"320000024","licenses":{"type":"capacity","package":"ONTAP-SEL-M300_STD","capacity":"50","endDate":"2021-12-31"}},"Signature":"X9EgloVMFUfGPMpkUkVrg9lzK5g9qIDNIomO8laci5KGEmvr3opp32v0LgEeiCkGX1wrtzp1b0VMkA5pIXm666gGM+D1GLgi+e+ZdEdNRvXBO9BLtXZbIaUzNuHLdjRLqiolCyBebDcW/lC/xp+pGfJtXtHIJBuikcjGyAqIe4KlV9InimDZF5X+07WbuBZEUgY3Q3UdAgZsPZVmE0lLekutUuMlz15fFm+vnaSMjfEVhm5QID5Z4ZJklBKbigjXpnikQ1Dc1YLOsSbF4uVt4vdFXE5t39AmLFJc+J+2aI5HGI6A9670+oYANeQqCYkuAJgZEvFhKAH0JstUB6oCkQ\u003d\u003d","trackingId":"0904lsvcw"}'

import json

a = json.dumps({"keys": [data]})

print(a)
