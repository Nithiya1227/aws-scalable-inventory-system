# Automated & Scalable Inventory Management System on AWS

A production-ready, highly available Inventory Management application built with **Python Flask** and architected on **AWS** using best practices for scalability, security, and automation.

## 🚀 Architecture Overview
This project demonstrates a 3-tier cloud architecture designed to handle traffic spikes and ensure zero downtime.

### Key Components:
- **Compute:** EC2 (Ubuntu) instances managed by an Auto Scaling Group (ASG).
- **Load Balancing:** Application Load Balancer (ALB) for intelligent traffic distribution.
- **Database:** Persistent MySQL database for inventory records.
- **Automation:** CloudWatch Alarms & Scaling Policies to scale fleet from **3 to 5 nodes**.
- **Monitoring:** SNS Notifications for real-time infrastructure alerts.

---

## 🛠️ Tech Stack
- **Cloud:** Amazon Web Services (AWS)
- **Backend:** Python (Flask)
- **Database:** MySQL
- **Networking:** VPC, Security Groups, Public/Private Subnets

---

## 📸 Project Screenshots

### 1. Dashboard UI
![App Dashboard](screenshots/dashboard.png)
*Inventory Management System Interface accessible via ALB DNS.*

### 2. Auto-Scaling in Action (3 to 5 Instances)
![Scaling Proof](screenshots/scaling_instances.png)
*CloudWatch triggered an alarm during high load, scaling the fleet from 3 to 5 running instances.*

### 3. Monitoring & Alerts
![CloudWatch Alarm](screenshots/cloudwatch.png)
*CloudWatch 'In Alarm' state and SNS Email notifications.*

---

## 🔧 Implementation Steps

1. **Application Setup:** Developed a Flask app with MySQL integration for CRUD operations.
2. **Infrastructure:** Launched EC2 instances and configured a custom VPC with secure Security Groups.
3. **Availability:** Deployed an Application Load Balancer (ALB) to route traffic to Target Groups.
4. **Elasticity:** Created an Auto Scaling Group (ASG) with a dynamic scaling policy (CPU > 70%).
5. **Testing:** Performed a stress test to verify the auto-scaling trigger and SNS alert system.

---

## 🛡️ Security Best Practices
- Implemented **Security Group Hardening** (Web instances only accept traffic from the ALB).
- Database layer isolated with restricted access rules.
- Environment variables used for sensitive credentials.
