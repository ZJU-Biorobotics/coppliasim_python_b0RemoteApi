import b0RemoteApi
import time

with b0RemoteApi.RemoteApiClient('b0RemoteApi_pythonClient','b0RemoteApi') as client:    

    client.simxStartSimulation(client.simxServiceCall())
    startTime = time.time()
    while time.time() < startTime + 5:
        continue
    client.simxStopSimulation(client.simxServiceCall())
