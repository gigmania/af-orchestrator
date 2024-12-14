my_airflow_project/
├── airflow/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── chart/ 
│       ├── Chart.yaml
│       ├── templates/
│       │   ├── deployment.yaml
│       │   ├── service.yaml
│       │   ├── ingress.yaml 
│       │   └── ... 
│       └── values.yaml 
├── dags/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── my_dag.py 
└── ... (other project files, e.g., CI/CD pipelines) 
