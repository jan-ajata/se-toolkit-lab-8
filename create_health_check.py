#!/usr/bin/env python3
"""Create a scheduled health check via nanobot webchat."""

import asyncio
import json
import sys

import websockets

ACCESS_KEY = "aidar"
# Connect directly to nanobot webchat port (now exposed)
WS_URL = f"ws://localhost:8765?access_key={ACCESS_KEY}"


async def create_health_check():
    """Connect to nanobot and create a 15-minute health check."""
    try:
        print(f"Connecting to {WS_URL}...")
        async with websockets.connect(WS_URL) as ws:
            print("WebSocket connected!")
            # Wait for connection established message
            try:
                init_msg = await asyncio.wait_for(ws.recv(), timeout=10)
                print(f"Connected: {init_msg}")
            except asyncio.TimeoutError:
                print("No initial message received, continuing...")
            
            # Send message to create health check
            create_msg = {
                "type": "message",
                "content": "Use your cron tool to add a health check. Action: add, every_seconds: 900, message: Check for backend errors in the last 15 minutes and post a summary here."
            }
            await ws.send(json.dumps(create_msg))
            print("Sent: Create health check request")
            
            # Receive responses
            for _ in range(15):  # Wait for up to 15 responses
                try:
                    response = await asyncio.wait_for(ws.recv(), timeout=60)
                    print(f"Response: {response}")
                    
                    # Check if job was created
                    if "job" in response.lower() or "created" in response.lower() or "scheduled" in response.lower():
                        print("\n✓ Health check created!")
                        
                        # Wait a moment then list scheduled jobs
                        await asyncio.sleep(2)
                        list_msg = {
                            "type": "message",
                            "content": "List scheduled jobs using cron tool action: list"
                        }
                        await ws.send(json.dumps(list_msg))
                        print("\nSent: List scheduled jobs request")
                        
                        # Get job list response
                        for _ in range(5):
                            try:
                                job_response = await asyncio.wait_for(ws.recv(), timeout=30)
                                print(f"Jobs: {job_response}")
                                if "no scheduled" not in job_response.lower() and "job" in job_response.lower():
                                    print("\n✓ Job confirmed!")
                                    return True
                            except asyncio.TimeoutError:
                                break
                        return True
                except asyncio.TimeoutError:
                    print("Timeout waiting for response")
                    break
            
            return False
            
    except Exception as e:
        print(f"Error: {e}")
        return False


if __name__ == "__main__":
    result = asyncio.run(create_health_check())
    sys.exit(0 if result else 1)
