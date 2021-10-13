- RED/USE METRICS
  - Utilization, Saturation, Errors
    - Service scoped
    - how managable is the workload by the service
      - workload: population of requests over a period of time
  - Rate, Errors, Duration: 
    - Request scoped
  - Together, they comprise minimaly complete, maximally useful observability

NEW RELIC: SITE RELIABILITY ENGINEERING

- "what happens when you ask a dev to design operations functions"
  - 50% ops, 50% engineering
- what to aim for?
  - at some point, uptime limited by external factors (ISPs)
  - comes at a tradeoff for rapid development - young services have a lower standard
- the four golden signals:
  - latency
  - traffic
  - errors
  - saturation
- SLOs, SLAs
  - error budgets (cool idea)