import hashlib

def generate_md5_file(file_path):
    # Create an MD5 hash object
    md5_hash = hashlib.md5()
    
    # Open the file in binary mode and read in chunks
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
    
    # Return the hexadecimal digest of the hash
    return md5_hash.hexdigest()

# Example usage
if __name__ == "__main__":
    for i in range(1, 47):
        file_path = "//home/egoitz/Segu_Repo/Irudiak/imagen/imagen" + str(i) + ".jpg" # Update this path to your actual file location
        print(file_path)
        hashed_file = generate_md5_file(file_path)
        print(f"MD5 hash of file '{file_path}': {hashed_file}")
        
        if hashed_file == "e5ed313192776744b9b93b1320b5e268":
            print(f"Found the correct hash for file '{file_path}'")
        else:
            print(f"Hash for file '{file_path}' is incorrect")

# Irudi zuzena 22.ena da, mezu sekretuak StegoSuite erabiliz aterata honela dio: "Al Fascismo no se le discute, se le destruye." Buenaventura Durruti