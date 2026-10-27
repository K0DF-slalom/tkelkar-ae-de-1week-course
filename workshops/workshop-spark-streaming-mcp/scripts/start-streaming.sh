#!/bin/bash

# =============================================================================
# Spark Streaming Helper Script
# =============================================================================
# This script simplifies starting the streaming job with proper configuration.
#
# Usage:
#   ./start-streaming.sh [socket|file|rate]
# =============================================================================

set -e

SOURCE_TYPE=${1:-socket}
VALID_SOURCES="socket file rate"

if [[ ! " $VALID_SOURCES " =~ " $SOURCE_TYPE " ]]; then
    echo "Error: Invalid source type '$SOURCE_TYPE'"
    echo "Usage: $0 [socket|file|rate]"
    exit 1
fi

echo "=============================================="
echo "Starting Spark Streaming Job"
echo "Source Type: $SOURCE_TYPE"
echo "=============================================="

# Submit the job to Spark
spark-submit \
    --master spark://spark-master:7077 \
    --deploy-mode client \
    --driver-memory 1g \
    --executor-memory 1g \
    --executor-cores 1 \
    --conf spark.sql.streaming.checkpointLocation=/tmp/spark-checkpoints \
    --conf spark.jars=/opt/spark/jars/postgresql-42.7.1.jar \
    --conf spark.driver.extraClassPath=/opt/spark/jars/postgresql-42.7.1.jar \
    --conf spark.executor.extraClassPath=/opt/spark/jars/postgresql-42.7.1.jar \
    /app/src/stream_processor.py "$SOURCE_TYPE"
