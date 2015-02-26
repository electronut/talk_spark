A simple Python script that can list Spark Cores using the Cloud API, 
as well as receive Server Sent Events (SSE) using [Spark.publish()][1]. 

Uses the [sseclient 0.0.8][2] module for processing SSE.

A trivial Spark Core program is also provided for testing.

[http://docs.spark.io/firmware/#spark-publish][1]

[1]: http://docs.spark.io/firmware/#spark-publish
[2]: https://pypi.python.org/pypi/sseclient/0.0.8