import os
import subprocess

# List of protobuf versions to test
protobuf_versions = [
    "3.19.0", "3.19.6", "3.20.0", "3.20.3",
    "3.21.0", "3.21.12", "3.17.3", "3.15.8"
]

# Protobuf test scripts
protobuf_test_cases = [
    # Test 1: Import runtime_version
    """
try:
    from google.protobuf import runtime_version
    print("Successfully imported runtime_version!")
except ImportError as e:
    print("Failed to import runtime_version.")
    raise e
    """,
    # Test 2: Import descriptor
    """
try:
    from google.protobuf import descriptor
    print("Successfully imported descriptor!")
except ImportError as e:
    print("Failed to import descriptor.")
    raise e
    """,
    # Test 3: Import text_format
    """
try:
    from google.protobuf import text_format
    print("Successfully imported text_format!")
except ImportError as e:
    print("Failed to import text_format.")
    raise e
    """,
    # Test 4: Import descriptor_pb2
    """
try:
    from google.protobuf.descriptor_pb2 import FileDescriptorProto
    print("Successfully imported FileDescriptorProto!")
except ImportError as e:
    print("Failed to import FileDescriptorProto.")
    raise e
    """,
    # Test 5: Compile object_detection.protos
    """
try:
    import os
    os.system("protoc object_detection/protos/*.proto --python_out=.")
    print("Successfully compiled .proto files!")
except Exception as e:
    print("Failed to compile .proto files.")
    raise e
    """
]

# Command to uninstall protobuf
def uninstall_protobuf():
    try:
        subprocess.run(["pip", "uninstall", "-y", "protobuf"], check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        print(f"Error uninstalling protobuf: {e}")

# Command to install protobuf and test the import
def install_and_test(version):
    print(f"Testing protobuf version {version}...")
    try:
        # Install the specific version of protobuf
        subprocess.run(["pip", "install", f"protobuf=={version}"], check=True, capture_output=True)

        # Run all test cases
        for i, test in enumerate(protobuf_test_cases, 1):
            print(f"Running Test Case {i} for protobuf {version}...")
            subprocess.run(["python", "-c", test], check=True)
            print(f"Test Case {i} passed for protobuf {version}!")

        print(f"Protobuf version {version} passed all tests!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Protobuf version {version} failed. Error: {e}")
        return False

# Iterate over the protobuf versions
for version in protobuf_versions:
    uninstall_protobuf()
    if install_and_test(version):
        print(f"Found working protobuf version: {version}")
        break
else:
    print("No compatible protobuf version found.")