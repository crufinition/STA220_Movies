import kagglehub

# Download latest version
path = kagglehub.dataset_download("mohammedalsubaie/movies")

print("Path to dataset files:", path)