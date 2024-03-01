Command to run the pormetheus docker container - docker run -d -p 9090:9090 -v /home/libintom/prometheus/:/etc/prometheus prom/prometheus --config.file=/etc/prometheus/prometheus.yml --storage.tsdb.path=/prometheus --web.console.libraries=/usr/share/prometheus/console_libraries --web.console.templates=/usr/share/prometheus/consoles --web.enable-lifecycle

curl -X POST http://localhost:9090/-/reload

PROMETHEUS

# Architecture

# PromQL Prometheus Query Language

## 4 Types of Data Types

1. Instant vector
2. Range Vector
3. Scalar
4. String

### Instant Vector
* Set of time series, containing single sample value for each time series
* All sharing the same time stamp

### Range Vector
* Set of time series, containg range of sample value for 

### Scalar

### String



