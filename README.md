A simple Python script that can list Spark Cores using the Cloud API, 
as well as receive Server Sent Events (SSE) using [Spark.publish()][1]. 

Uses the [sseclient 0.0.8][2] module for processing SSE.

A trivial Spark Core program is also provided for testing.

Sample run:

```
$ python talk_spark.py --at XXXX_ACCESS_TOKEN --list
[{u'connected': True, u'last_heard': u'2015-02-26T02:17:22.450Z', u'last_app': None, u'id': u'xxxxxxx', u'name': u'yyyy'}]
```

```
$ python talk_spark.py --at XXXX_ACCESS_TOKEN --listen
Notification: Yo 4 at 2015-02-26T01:59:02.272Z
Notification: Yo 5 at 2015-02-26T01:59:07.278Z
Notification: Yo 6 at 2015-02-26T01:59:12.281Z
^Cexiting.
```

[1]: http://docs.spark.io/firmware/#spark-publish
[2]: https://pypi.python.org/pypi/sseclient/0.0.8