# 🚨 BreachRadar – Cyber Threat Monitoring with ELK Stack

**BreachRadar** is a simulated real-time threat monitoring dashboard built using the **ELK Stack** (Elasticsearch, Logstash, Kibana, and Filebeat). It mimics a basic SIEM (Security Information and Event Management) system, capable of ingesting log data, identifying threat patterns, and visualizing them for quick analysis.

## Overview

This project demonstrates:
- Ingestion of synthetic security logs (e.g., SQLi, XSS, Port Scans)
- Parsing and structuring of logs using Logstash
- Real-time dashboards for SOC-style monitoring via Kibana

## Tech Stack

- **Docker**
- **Elasticsearch** – for indexing logs
- **Logstash** – for processing and transforming logs
- **Filebeat** – for collecting logs from file sources
- **Kibana** – for visualizing logs and building dashboards

---

## Architecture

```
[Log Files] → [Filebeat] → [Logstash] → [Elasticsearch] → [Kibana]
```

- `test-logs/` folder holds simulated log events in JSON format.
- Filebeat reads logs and forwards to Logstash via Beats protocol on port 5044.
- Logstash filters and outputs to Elasticsearch.
- Kibana queries Elasticsearch to build dashboards.

---

## 📊 Dashboard Features

✅ Real-time updates of log data  
✅ Pie chart of most frequent attack types  
✅ Top source IPs by frequency  
✅ Time-based histogram of log activity  
✅ Filter by keyword: `SQL`, `XSS`, `Port Scan`, `Brute Force`, etc.

---

## Getting Started

1. **Clone the repository**
```bash
git clone https://github.com/mlikespizza/breachradar.git
cd breachradar/elk-stack
```

2. **Start ELK services**
```bash
docker-compose up -d
```

3. **Verify services are running**
```bash
docker-compose ps
```

4. **Open Kibana**
   Navigate to: [http://localhost:5601](http://localhost:5601)

5. **Create Index Pattern**
   - Go to Stack Management → Index Patterns
   - Create index pattern: `test-logs*`
   - Select `@timestamp` as time field

6. **Explore the Dashboard**
   - Navigate to Discover to view incoming logs
   - Create visualizations and dashboards

---

## Sample Log Format

The project includes sample security logs in JSON format:

```json
{"@timestamp":"2025-07-23T08:12:33Z", "message":"Failed login attempt from IP 192.168.1.15 to /admin using username 'admin'"}
{"@timestamp":"2025-07-23T08:13:01Z", "message":"SQL Injection attempt detected in URL parameter from 172.16.0.4 -> /login.php?user=admin'--"}
{"@timestamp":"2025-07-23T08:13:45Z", "message":"Connection attempt to blocked port 23 (Telnet) from external IP 203.0.113.8"}
```
## 🔄 Log Simulator (Python)

This script (`log_generator.py`) generates synthetic security logs and appends them to the monitored `generated.log` file. Logs are ingested in real time by Filebeat and visualized in Kibana.

Run with:

```bash
python log_generator.py

---

## Project Structure

```
breachradar/
├── elk-stack/
│   ├── docker-compose.yml          # Docker services configuration
│   ├── filebeat/
│   │   └── filebeat.yml            # Filebeat configuration
│   ├── logstash/
│   │   ├── config/
│   │   │   └── logstash.yml        # Logstash main config
│   │   └── pipeline/
│   │       └── logstash.conf       # Logstash pipeline config
│   └── test-logs/
│       ├── attack.log              # Sample attack logs
│       ├── breach.log              # Sample breach logs
│       └── sample.log              # Additional sample logs
└── README.md
└── log_generator.py
```

---

## Configuration Details

### Filebeat Configuration
- Monitors `test-logs/*.log` files
- Outputs to Logstash on port 5044 using Beats protocol

### Logstash Configuration
- Receives data via Beats input on port 5044
- Outputs to Elasticsearch index `test-logs`
- Includes stdout debugging output

### Docker Services
- **Elasticsearch**: Port 9200
- **Logstash**: Port 5044
- **Kibana**: Port 5601
- **Filebeat**: Runs as log shipper

---

## Troubleshooting

### Common Issues

1. **Filebeat connection errors**
   - Ensure Logstash is using `beats` input (not `tcp`)
   - Verify port 5044 is correctly mapped in docker-compose.yml

2. **File permissions**
   - Filebeat requires strict permissions on config files
   - The docker-compose includes automatic permission fixing

3. **No data in Kibana**
   - Check if containers are running: `docker-compose ps`
   - Verify logs are being processed: `docker logs logstash`

---

## Future Enhancements

* 🔁 Automate log generation with Python & Redis
* 🔔 Add alerting (e.g., via Elasticsearch Watcher)
* 📦 Deploy to cloud or container orchestrator
* 🎯 Add more sophisticated log parsing and field extraction
* 📊 Create pre-built Kibana dashboards and visualizations

---

## 📚 Learning Goals

* Understand log pipelines in real-world systems
* Work with Elasticsearch queries and Kibana visualizations
* Simulate cyber attack patterns in a controlled setup
* Learn Docker containerization for ELK stack deployment
* Practice SIEM-like threat monitoring workflows

---

## 🧑‍💻 Author

**Marvelous Edoho**  
Aspiring Cybersecurity Engineer | [LinkedIn](https://linkedin.com/in/marvelous-edoho) | [GitHub](https://github.com/mlikespizza)

---

## 🛡️ License

This project is licensed under the MIT License.

---

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements or additional features!

## ⭐ Show Your Support

If this project helped you learn about ELK stack or cybersecurity monitoring, please give it a star!
