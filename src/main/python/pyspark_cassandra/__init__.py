# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This module provides python support for Apache Spark's Resillient Distributed Datasets from Apache Cassandra CQL rows
using the Spark Cassandra Connector from https://github.com/datastax/spark-cassandra-connector.
"""

import inspect

import pyspark.context
import pyspark.rdd
import pyspark_cassandra.context

from .context import CassandraSparkContext, convert
from .rdd import CassandraRDD, saveToCassandra, RowFormat


__all__ = [
    "CassandraSparkContext", "CassandraRDD", "RowFormat"
]


# Monkey patch the default SparkContext with Cassandra functionality
pyspark.context.SparkContext = CassandraSparkContext

# Monkey patch the default python RDD so that it can be stored to Cassandra as CQL rows
pyspark.rdd.RDD.saveToCassandra = saveToCassandra

# Monkey patch the sc variable in the caller if any
parent_frame = inspect.currentframe().f_back
if "sc" in parent_frame.f_globals:
	convert(parent_frame.f_globals["sc"])
