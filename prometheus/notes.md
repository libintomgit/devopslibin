

#### Static scrape config for bmt-fe
    - job_name: bmt-fe
      metrics_path: /metrics
      scrape_interval: 3s
      static_configs:
        - targets: ['bmt-fe.bmt-ns:8000']
          labels:
            appname: 'bmt-fe'