import os
import subprocess
import tarfile

base_url = "https://huggingface.co/datasets/OpenDILabCommunity/LMDrive/resolve/main/data/"
towns = ['Town01', 'Town02', 'Town03','Town04''Town05', 'Town06', 'Town07']
directories = [
    "routes_town01_tiny_w9_09_30_11_21_32",
    "routes_town01_tiny_w0_09_30_14_13_54",
    "routes_town01_tiny_w10_08_25_22_13_53",
    "routes_town01_tiny_w12_08_27_07_42_31",
    "routes_town01_tiny_w15_08_27_08_21_38",
    "routes_town01_tiny_w19_08_27_09_10_19",
    "routes_town01_tiny_w3_08_27_11_41_48",
    "routes_town01_tiny_w5_09_30_05_41_36",
    "routes_town02_tiny_w11_08_26_19_29_47",
    "routes_town02_tiny_w15_08_26_18_03_16",
    "routes_town02_tiny_w0_10_01_18_26_50",
    "routes_town02_tiny_w12_10_02_20_25_59",
    "routes_town02_tiny_w17_10_01_18_02_27",
    "routes_town02_tiny_w20_08_26_19_20_03",
    "routes_town02_tiny_w4_10_01_22_43_50",
    "routes_town02_tiny_w6_10_02_21_52_09",
    "routes_town03_tiny_w10_08_20_04_55_35",
    "routes_town03_tiny_w13_08_20_10_04_33",
    "routes_town03_tiny_w14_10_04_16_01_40",
    "routes_town03_tiny_w16_08_22_03_18_14",
    "routes_town03_tiny_w18_08_22_06_08_51",
    "routes_town03_tiny_w2_08_20_19_07_24",
    "routes_town03_tiny_w4_08_22_03_43_55",
    "routes_town03_tiny_w6_08_22_02_19_53",
    "routes_town04_tiny_w0_10_17_10_20_07",
    "routes_town04_tiny_w11_10_06_12_16_48",
    "routes_town04_tiny_w12_10_06_12_46_22",
    "routes_town04_tiny_w15_10_06_05_31_38",
    "routes_town04_tiny_w17_10_06_08_47_39",
    "routes_town04_tiny_w20_10_05_15_42_09",
    "routes_town04_tiny_w2_10_06_20_58_02",
    "routes_town04_tiny_w4_10_06_21_30_20",
    "routes_town05_tiny_w10_10_07_22_49_03",
    "routes_town05_tiny_w12_10_07_22_33_24",
    "routes_town05_tiny_w15_10_07_23_11_43",
    "routes_town05_tiny_w18_10_07_18_50_19",
    "routes_town05_tiny_w20_10_08_12_50_02",
    "routes_town05_tiny_w2_10_17_23_32_00",
    "routes_town05_tiny_w3_10_18_02_38_10",
    "routes_town05_tiny_w6_10_08_01_01_02",
    "routes_town06_tiny_w0_10_17_22_50_55",
    "routes_town06_tiny_w11_10_17_22_10_18",
    "routes_town06_tiny_w13_10_10_01_22_42",
    "routes_town06_tiny_w15_10_08_14_56_05",
    "routes_town06_tiny_w19_10_08_18_18_43",
    "routes_town06_tiny_w3_10_09_17_35_08",
    "routes_town06_tiny_w5_10_18_06_17_59",
    "routes_town06_tiny_w8_10_10_00_23_40",
    "routes_town07_tiny_w12_09_08_09_31_23",
    "routes_town07_tiny_w14_09_08_10_26_33",
    "routes_town07_tiny_w16_09_08_17_14_22",
    "routes_town07_tiny_w19_09_08_23_34_57",
    "routes_town07_tiny_w1_09_08_23_55_19",
    "routes_town07_tiny_w4_09_08_06_11_31",
    "routes_town07_tiny_w6_09_08_11_46_07",
    "routes_town07_tiny_w9_09_08_12_04_20"]

output_dir = "/content/datasets"
extension = "tar.gz"

for dir in directories:
    # Extract the town name from the directory name (e.g., "Town01", "Town02", etc.)
    town_number = dir.split('_')[1][-2:]  # Gets '01', '02', etc.
    town_id = f"Town{town_number.capitalize()}"  # Construct 'Town01', 'Town02', etc.
    if town == "town01":
      town_id = towns[0]
      download_url = f"{base_url}{town_id}/{dir}.{extension}"
      download_command = f"wget -P {output_dir} {download_url}"
      subprocess.run(download_command, shell=True, check=True)
      tar_path = os.path.join(output_dir, f"{dir}.tar.gz")
      with tarfile.open(tar_path, "r:gz") as tar:
        tar.extractall(path=output_dir)
    elif town == "town02":
      town_id = towns[1]
      download_url = f"{base_url}{town_id}/{dir}.{extension}"
      download_command = f"wget -P {output_dir} {download_url}"
      subprocess.run(download_command, shell=True, check=True)
      tar_path = os.path.join(output_dir, f"{dir}.tar.gz")
      with tarfile.open(tar_path, "r:gz") as tar:
        tar.extractall(path=output_dir)
    elif town == "town03":
      town_id = towns[2]
      download_url = f"{base_url}{town_id}/{dir}.{extension}"
      download_command = f"wget -P {output_dir} {download_url}"
      subprocess.run(download_command, shell=True, check=True)
      tar_path = os.path.join(output_dir, f"{dir}.tar.gz")
      with tarfile.open(tar_path, "r:gz") as tar:
        tar.extractall(path=output_dir)
    elif town == "town04":
      town_id = towns[3]
      download_url = f"{base_url}{town_id}/{dir}.{extension}"
      download_command = f"wget -P {output_dir} {download_url}"
      subprocess.run(download_command, shell=True, check=True)
      tar_path = os.path.join(output_dir, f"{dir}.tar.gz")
      with tarfile.open(tar_path, "r:gz") as tar:
        tar.extractall(path=output_dir)
    elif town == "town05":
      town_id = towns[4]
      download_url = f"{base_url}{town_id}/{dir}.{extension}"
      download_command = f"wget -P {output_dir} {download_url}"
      subprocess.run(download_command, shell=True, check=True)
      tar_path = os.path.join(output_dir, f"{dir}.tar.gz")
      with tarfile.open(tar_path, "r:gz") as tar:
        tar.extractall(path=output_dir)
    elif town == "town06":
      town_id = towns[5]
      download_url = f"{base_url}{town_id}/{dir}.{extension}"
      download_command = f"wget -P {output_dir} {download_url}"
      subprocess.run(download_command, shell=True, check=True)
      tar_path = os.path.join(output_dir, f"{dir}.tar.gz")
      with tarfile.open(tar_path, "r:gz") as tar:
        tar.extractall(path=output_dir)
    elif town == "town07":
      town_id = towns[6]
      download_url = f"{base_url}{town_id}/{dir}.{extension}"
      download_command = f"wget -P {output_dir} {download_url}"
      subprocess.run(download_command, shell=True, check=True)
      tar_path = os.path.join(output_dir, f"{dir}.tar.gz")
      with tarfile.open(tar_path, "r:gz") as tar:
        tar.extractall(path=output_dir)