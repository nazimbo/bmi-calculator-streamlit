# Deployment Guide

This guide covers deploying the BMI Calculator application to various platforms and environments.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Local Development](#local-development)
- [Docker Deployment](#docker-deployment)
- [Streamlit Cloud](#streamlit-cloud)
- [AWS Deployment](#aws-deployment)
- [Google Cloud Platform](#google-cloud-platform)
- [Azure Deployment](#azure-deployment)
- [Environment Configuration](#environment-configuration)
- [Security Considerations](#security-considerations)
- [Monitoring and Logging](#monitoring-and-logging)

---

## Prerequisites

- Python 3.9+ (recommended: 3.11)
- Git
- Docker (for containerized deployment)
- Cloud provider account (for cloud deployments)

---

## Local Development

### Quick Start

```bash
# Clone the repository
git clone <repository-url>
cd bmi-calculator-streamlit

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

The application will be available at `http://localhost:8501`

### Development with Hot Reload

Streamlit automatically reloads when you save changes to the code. No additional configuration needed.

---

## Docker Deployment

### Using Docker

**Build the image:**

```bash
docker build -t bmi-calculator:latest .
```

**Run the container:**

```bash
docker run -p 8501:8501 \
  --name bmi-calculator \
  --rm \
  bmi-calculator:latest
```

**Access the application:**
Open http://localhost:8501 in your browser.

### Using Docker Compose

**Start the application:**

```bash
docker-compose up -d
```

**View logs:**

```bash
docker-compose logs -f
```

**Stop the application:**

```bash
docker-compose down
```

**Health check:**

```bash
curl http://localhost:8501/_stcore/health
```

### Production Docker Configuration

For production deployments, consider:

1. **Use multi-stage builds** (already implemented in Dockerfile)
2. **Run as non-root user** (already implemented)
3. **Set resource limits** (configured in docker-compose.yml)
4. **Enable health checks** (already implemented)
5. **Use secrets management** for sensitive data

Example with secrets:

```bash
docker run -p 8501:8501 \
  --name bmi-calculator \
  --env-file .env.production \
  --restart unless-stopped \
  bmi-calculator:latest
```

---

## Streamlit Cloud

[Streamlit Cloud](https://streamlit.io/cloud) provides free hosting for Streamlit apps.

### Deployment Steps

1. **Push your code to GitHub**

```bash
git push origin main
```

2. **Sign up for Streamlit Cloud**
   - Visit https://streamlit.io/cloud
   - Sign in with GitHub

3. **Deploy your app**
   - Click "New app"
   - Select your repository
   - Choose `app.py` as the main file
   - Click "Deploy"

4. **Configure settings** (optional)
   - Set environment variables
   - Configure custom domain
   - Set up authentication

### Environment Variables

Set these in Streamlit Cloud settings:

```
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
```

### Custom Domain

In Streamlit Cloud settings:
1. Navigate to "Settings" > "General"
2. Add your custom domain
3. Update DNS records as instructed

---

## AWS Deployment

### Option 1: AWS Elastic Beanstalk

**1. Install AWS EB CLI:**

```bash
pip install awsebcli
```

**2. Initialize Elastic Beanstalk:**

```bash
eb init -p docker bmi-calculator
```

**3. Create environment:**

```bash
eb create bmi-calculator-env
```

**4. Deploy:**

```bash
eb deploy
```

**5. Open application:**

```bash
eb open
```

### Option 2: AWS ECS with Fargate

**1. Create ECR repository:**

```bash
aws ecr create-repository --repository-name bmi-calculator
```

**2. Build and push Docker image:**

```bash
# Login to ECR
aws ecr get-login-password --region us-east-1 | \
  docker login --username AWS --password-stdin \
  <account-id>.dkr.ecr.us-east-1.amazonaws.com

# Build and tag
docker build -t bmi-calculator .
docker tag bmi-calculator:latest \
  <account-id>.dkr.ecr.us-east-1.amazonaws.com/bmi-calculator:latest

# Push
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/bmi-calculator:latest
```

**3. Create ECS cluster:**

```bash
aws ecs create-cluster --cluster-name bmi-cluster
```

**4. Create task definition:**

See `aws/task-definition.json` for example.

**5. Create service:**

```bash
aws ecs create-service \
  --cluster bmi-cluster \
  --service-name bmi-calculator \
  --task-definition bmi-calculator \
  --desired-count 1 \
  --launch-type FARGATE
```

### Option 3: AWS App Runner

**1. Create App Runner service:**

```bash
aws apprunner create-service \
  --service-name bmi-calculator \
  --source-configuration '{
    "ImageRepository": {
      "ImageIdentifier": "<account-id>.dkr.ecr.us-east-1.amazonaws.com/bmi-calculator:latest",
      "ImageConfiguration": {
        "Port": "8501"
      }
    }
  }'
```

---

## Google Cloud Platform

### Cloud Run Deployment

**1. Install Google Cloud SDK:**

```bash
# Follow instructions at: https://cloud.google.com/sdk/install
```

**2. Build and push to Container Registry:**

```bash
# Configure Docker for GCP
gcloud auth configure-docker

# Build and push
gcloud builds submit --tag gcr.io/PROJECT_ID/bmi-calculator

# Or using Docker directly:
docker build -t gcr.io/PROJECT_ID/bmi-calculator .
docker push gcr.io/PROJECT_ID/bmi-calculator
```

**3. Deploy to Cloud Run:**

```bash
gcloud run deploy bmi-calculator \
  --image gcr.io/PROJECT_ID/bmi-calculator \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --port 8501 \
  --memory 512Mi \
  --cpu 1
```

**4. Get the service URL:**

```bash
gcloud run services describe bmi-calculator \
  --platform managed \
  --region us-central1 \
  --format 'value(status.url)'
```

### GCP Compute Engine

**1. Create VM instance:**

```bash
gcloud compute instances create bmi-calculator \
  --image-family=debian-11 \
  --image-project=debian-cloud \
  --machine-type=e2-small \
  --zone=us-central1-a
```

**2. SSH into instance:**

```bash
gcloud compute ssh bmi-calculator --zone=us-central1-a
```

**3. Install Docker and deploy:**

```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Run container
sudo docker run -d -p 80:8501 \
  --name bmi-calculator \
  --restart always \
  gcr.io/PROJECT_ID/bmi-calculator
```

---

## Azure Deployment

### Azure App Service

**1. Install Azure CLI:**

```bash
# Follow instructions at: https://docs.microsoft.com/cli/azure/install-azure-cli
```

**2. Login to Azure:**

```bash
az login
```

**3. Create resource group:**

```bash
az group create --name bmi-calculator-rg --location eastus
```

**4. Create App Service plan:**

```bash
az appservice plan create \
  --name bmi-calculator-plan \
  --resource-group bmi-calculator-rg \
  --sku B1 \
  --is-linux
```

**5. Create web app:**

```bash
az webapp create \
  --resource-group bmi-calculator-rg \
  --plan bmi-calculator-plan \
  --name bmi-calculator \
  --runtime "PYTHON|3.11"
```

**6. Deploy code:**

```bash
az webapp up \
  --name bmi-calculator \
  --resource-group bmi-calculator-rg
```

### Azure Container Instances

**1. Create container registry:**

```bash
az acr create \
  --resource-group bmi-calculator-rg \
  --name bmicalcregistry \
  --sku Basic
```

**2. Build and push image:**

```bash
az acr build \
  --registry bmicalcregistry \
  --image bmi-calculator:latest .
```

**3. Create container instance:**

```bash
az container create \
  --resource-group bmi-calculator-rg \
  --name bmi-calculator \
  --image bmicalcregistry.azurecr.io/bmi-calculator:latest \
  --cpu 1 --memory 0.5 \
  --registry-login-server bmicalcregistry.azurecr.io \
  --registry-username <username> \
  --registry-password <password> \
  --dns-name-label bmi-calculator \
  --ports 8501
```

---

## Environment Configuration

### Environment Variables

Create `.env` file (never commit this):

```bash
# Streamlit Configuration
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Application Configuration
DEFAULT_LANGUAGE=en
LOG_LEVEL=INFO

# Security (if adding authentication)
# SECRET_KEY=your-secret-key-here
```

### Production Configuration

For production, use `.env.production`:

```bash
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
STREAMLIT_THEME_BASE=light
LOG_LEVEL=WARNING
```

---

## Security Considerations

### HTTPS/TLS

**Always use HTTPS in production:**

1. **Streamlit Cloud**: HTTPS enabled by default
2. **Docker/Cloud**: Use reverse proxy (nginx, Caddy, Traefik)
3. **Cloud platforms**: Enable HTTPS in platform settings

**Example nginx configuration:**

```nginx
server {
    listen 80;
    server_name yourdomain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com;

    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Security Headers

Add security headers in reverse proxy:

```nginx
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-Content-Type-Options "nosniff" always;
add_header X-XSS-Protection "1; mode=block" always;
add_header Referrer-Policy "no-referrer-when-downgrade" always;
add_header Content-Security-Policy "default-src 'self' http: https: data: blob: 'unsafe-inline'" always;
```

### Authentication

For private deployments, add authentication:

1. **Streamlit Cloud**: Built-in authentication
2. **Self-hosted**: Use reverse proxy authentication (OAuth, Basic Auth)
3. **Cloud platforms**: Use platform authentication features

---

## Monitoring and Logging

### Application Logs

**Docker:**

```bash
docker logs -f bmi-calculator
```

**Docker Compose:**

```bash
docker-compose logs -f
```

**Cloud platforms**: Use platform-specific logging services:
- AWS: CloudWatch
- GCP: Cloud Logging
- Azure: Application Insights

### Health Monitoring

**Health check endpoint:**

```bash
curl http://your-domain/_stcore/health
```

**Set up monitoring:**

1. **Uptime monitoring**: UptimeRobot, Pingdom
2. **Application monitoring**: DataDog, New Relic
3. **Log aggregation**: Elasticsearch, Splunk

### Metrics to Monitor

- Response time
- Error rate
- CPU/Memory usage
- Request count
- User sessions

---

## Troubleshooting

### Common Issues

**1. Port already in use:**

```bash
# Find process using port 8501
lsof -i :8501
# Kill process
kill -9 <PID>
```

**2. Docker build fails:**

```bash
# Clean Docker cache
docker system prune -a
# Rebuild without cache
docker build --no-cache -t bmi-calculator .
```

**3. Module not found:**

```bash
# Ensure requirements are installed
pip install -r requirements.txt
# Check Python path
python -c "import sys; print(sys.path)"
```

**4. Memory issues:**

Increase Docker memory limit:

```bash
docker run -p 8501:8501 -m 1g bmi-calculator:latest
```

---

## Performance Tuning

### Caching

The application uses Streamlit's caching:
- `@st.cache_data` for data operations
- `@st.cache_resource` for heavy resources

### Resource Limits

**Docker:**

```yaml
deploy:
  resources:
    limits:
      cpus: '1.0'
      memory: 512M
```

**Cloud platforms**: Set instance size appropriately
- Small: 0.5 CPU, 512MB RAM
- Medium: 1 CPU, 1GB RAM
- Large: 2 CPU, 2GB RAM

---

## Backup and Disaster Recovery

### Backup Strategy

1. **Code**: Version controlled in Git
2. **Logs**: Backed up to S3/Cloud Storage (optional)
3. **Configuration**: Stored in version control (excluding secrets)

### Disaster Recovery

1. **Container registry**: Keep multiple image versions
2. **Infrastructure as Code**: Use Terraform/CloudFormation
3. **Monitoring**: Set up alerts for downtime

---

## Support

For issues or questions:
- GitHub Issues: <repository-url>/issues
- Documentation: See README.md, TESTING.md, SECURITY.md

---

## License

This project is licensed under the MIT License. See LICENSE file for details.
