from flask import jsonify
from src import app
import json

def test_hello_world(test_client):
        """
        GIVEN a healthy app
        WHEN call hello world
        THEN get hello world greeting message
        """
        response = test_client.get('/')
        assert response.status_code == 200
        assert response.json["message"] == "Hello World!"

def test_healthy(test_client):
        """
        GIVEN a healthy app
        WHEN call to check health
        THEN get message that application is healthy
        """
        response = test_client.get('/health')
        assert response.status_code == 200
        assert response.json["status"] == "Application healthcheck successful"

def test_toggle_health(test_client):
        """
        GIVEN a healthy app
        WHEN call to toggle health status
        THEN get message that application health status is toggled
        """
        response = test_client.get('/toggle-health')
        assert response.status_code == 200
        assert response.json["message"] == "health set to False"

def test_unhealthy(test_client):
        """
        GIVEN a unhealthy app
        WHEN call to check health
        THEN get message that application is unhealthy
        """
        response = test_client.get('/health')
        assert response.status_code == 503
        assert response.json["status"] == "Application healthcheck failed"