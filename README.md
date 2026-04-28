# 📡 gRPC Publish/Subscribe - Notification System

This project implements a **Publish/Subscribe (Pub/Sub)** communication paradigm using **gRPC** and **Python**. It was developed as a practical application for Distributed Systems, focusing on Remote Procedure Calls (RPC) and real-time data streaming.

## 🚀 Project Overview
The application simulates a **Cryptocurrency Price Alert System**:
- **Publishers:** Send price updates or news to specific topics (e.g., BTC, ETH).
- **Subscribers:** Subscribe to topics of interest and receive real-time notifications via **Server-side Streaming**.
- **Server (Broker):** Manages subscriptions and distributes messages efficiently without direct coupling between sender and receiver.

## 🛠️ Tech Stack
- **Python 3**
- **gRPC:** High-performance RPC framework.
- **Protocol Buffers (Protobuf):** Language-neutral, efficient binary serialization.
- **HTTP/2:** Enabling long-lived connections and multiplexing.

## 📋 Prerequisites
In your Linux/WSL environment, ensure you have Python and the virtual environment module installed:
```bash
sudo apt update
sudo apt install python3-full
