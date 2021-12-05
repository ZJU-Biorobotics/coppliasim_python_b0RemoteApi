
# vrep_python_b0RemoteApi

## Configuration

### Server
 
Open a new scene, In the [**model Brower→tools**], add **B0 remote Api server.ttm** model to your scene.

### Client

 1.  `pip install msgpack`
 2. Ensure the following library files be in your working directory.(For linux, you can find these files in the CoppeliaSim root folder.)
 ```text
b0.dll
boost_filesystem-vc142-mt-x64-1_73.dll
boost_program_options-vc142-mt-x64-1_73.dll
boost_regex-vc142-mt-x64-1_73.dll
boost_serialization-vc142-mt-x64-1_73.dll
boost_thread-vc142-mt-x64-1_73.dll
libzmq-mt-4_3_3.dll
lz4.dll
zlib1.dll
b0.py
b0RemoteApi.py
```
 3. Run test.py to test if everything is ok.
 
## Run the demo
1. Open the scene scenes/messaging/synchronousImageTransmissionViaRemoteApi.ttt.Do not launch simulation, and make sure that the B0 resolver is running.
2. Run the synchronousImageTransmission.py.
3. This demo realizes the acquisition of images from the server camera 1, and then synchronously transmits the images to the server camera 2.


 

