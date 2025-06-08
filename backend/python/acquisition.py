import numpy as np

class AcquisitionModule:
    def __init__(self, rgb_shape=(480, 640, 3), depth_shape=(480, 640)):
        self.rgb_shape = rgb_shape
        self.depth_shape = depth_shape

    def get_frames(self):
        """
        Simulates fetching RGB and depth frames and saves them to .npy files.
        Returns the filepaths of the saved frames.
        """
        rgb_frame = np.random.randint(0, 256, size=self.rgb_shape, dtype=np.uint8)
        depth_frame = np.random.rand(*self.depth_shape).astype(np.float32) * 1000  # Simulate depth in mm

        rgb_filepath = "temp_rgb.npy"
        depth_filepath = "temp_depth.npy"

        np.save(rgb_filepath, rgb_frame)
        np.save(depth_filepath, depth_frame)

        return rgb_filepath, depth_filepath

if __name__ == '__main__':
    # Example usage
    acquisition_module = AcquisitionModule()
    rgb_path, depth_path = acquisition_module.get_frames()
    print("RGB frame saved to:", rgb_path)
    print("Depth frame saved to:", depth_path)

    # Verify by loading
    loaded_rgb = np.load(rgb_path)
    loaded_depth = np.load(depth_path)
    print("Loaded RGB Frame Shape:", loaded_rgb.shape)
    print("Loaded Depth Frame Shape:", loaded_depth.shape)
